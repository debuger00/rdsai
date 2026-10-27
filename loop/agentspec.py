from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field

"""
读取 Agent 的 YAML 配置，
处理配置继承和路径，检查必要字段，
最后返回一份完整的配置对象。
"""

def get_agents_dir() -> Path:
    loop_dir = Path(__file__).parent
    return loop_dir.parent / "prompts"


DEFAULT_AGENT_FILE = get_agents_dir() / "default_agent.yaml"


class AgentSpec(BaseModel):
    """Agent specification."""

    extend: str | None = Field(default=None, description="Agent file to extend")
    name: str | None = Field(default=None, description="Agent name")  # required
    system_prompt_path: Path | None = Field(default=None, description="System prompt path")  # required
    system_prompt_args: dict[str, str] = Field(default_factory=dict, description="System prompt arguments")
    tools: list[str] | None = Field(default=None, description="Tools")
    exclude_tools: list[str] | None = Field(default=None, description="Tools to exclude")


@dataclass(frozen=True, slots=True, kw_only=True)
class ResolvedAgentSpec:
    """Resolved agent specification."""

    name: str
    system_prompt_path: Path
    system_prompt_args: dict[str, str]
    tools: list[str]
    exclude_tools: list[str]


def load_agent_spec(agent_file: Path) -> ResolvedAgentSpec:
    """
    Load agent specification from file.

    Raises:
        FileNotFoundError: If the agent spec file is not found.
        AgentSpecError: If the agent spec is not valid.
    """
    agent_spec = _load_agent_spec(agent_file)
    assert agent_spec.extend is None, "agent extension should be recursively resolved"
    if agent_spec.name is None:
        raise AgentSpecError("Agent name is required")
    if agent_spec.system_prompt_path is None:
        raise AgentSpecError("System prompt path is required")
    agent_spec.tools = agent_spec.tools or []
    return ResolvedAgentSpec(
        name=agent_spec.name,
        system_prompt_path=agent_spec.system_prompt_path,
        system_prompt_args=agent_spec.system_prompt_args,
        tools=agent_spec.tools,
        exclude_tools=agent_spec.exclude_tools or [],
    )


def _load_agent_spec(agent_file: Path) -> AgentSpec:
    # 读取当前 Agent 配置，并递归合并它通过 extend 指定的父配置。
    # 先检查路径是否存在、是否为文件，避免把目录当作 YAML 文件读取。
    if not agent_file.exists():
        raise AgentSpecError(f"Agent spec file not found: {agent_file}")
    if not agent_file.is_file():
        raise AgentSpecError(f"Agent spec path is not a file: {agent_file}")
    # 使用 UTF-8 读取 YAML；将 YAML 解析错误转换为配置异常，并保留原始异常链。
    try:
        with open(agent_file, encoding="utf-8") as f:
            data: dict[str, Any] = yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise AgentSpecError(f"Invalid YAML in agent spec file: {e}") from e

    # 未声明版本时按版本 1 处理，目前仅支持这一版本。
    version = data.get("version", 1)
    if version != 1:
        raise AgentSpecError(f"Unsupported agent spec version: {version}")

    # 取出 agent 节点，通过 Pydantic 模型校验字段并填充默认值。
    agent_spec = AgentSpec(**data.get("agent", {}))
    # 提示词的相对路径以当前 YAML 所在目录为基准，而不是程序的工作目录。
    if agent_spec.system_prompt_path is not None:
        agent_spec.system_prompt_path = (agent_file.parent / agent_spec.system_prompt_path).absolute()
    if agent_spec.extend:
        # extend 为 default 时使用内置配置，否则按当前 YAML 的目录解析父配置路径。
        if agent_spec.extend == "default":
            base_agent_file = DEFAULT_AGENT_FILE
        else:
            base_agent_file = (agent_file.parent / agent_spec.extend).absolute()
        # 递归加载父配置，使多层继承先从最底层父配置开始合并。
        base_agent_spec = _load_agent_spec(base_agent_file)
        # 子配置显式提供的名称和提示词路径覆盖父配置；为 None 时沿用父配置。
        if agent_spec.name is not None:
            base_agent_spec.name = agent_spec.name
        if agent_spec.system_prompt_path is not None:
            base_agent_spec.system_prompt_path = agent_spec.system_prompt_path
        for k, v in agent_spec.system_prompt_args.items():
            # 提示词参数按键合并：保留父配置的其他参数，同名参数以子配置为准。
            base_agent_spec.system_prompt_args[k] = v
        # 工具列表和排除列表整体替换，不做追加；显式传入 [] 可以清空继承的列表。
        if agent_spec.tools is not None:
            base_agent_spec.tools = agent_spec.tools
        if agent_spec.exclude_tools is not None:
            base_agent_spec.exclude_tools = agent_spec.exclude_tools
        # 以合并后的父配置对象作为最终结果。
        agent_spec = base_agent_spec
    # 返回配置对象；必要字段的最终检查由外层 load_agent_spec 完成。
    return agent_spec


class AgentSpecError(Exception):
    """Agent specification error."""

    pass
