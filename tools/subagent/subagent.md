Delegate task to specialized subagent for execution.

This tool allows the main agent to delegate complex tasks to specialized subagents that have dedicated system prompts and tool sets for specific domains.

Subagents are automatically discovered from the prompts directory. Each subagent has its own configuration file (e.g., `sysbench_agent.yaml`) and can have custom execution logic if needed.

## Parameters

- **subagent** (required): The subagent to delegate to. Available subagents are automatically discovered. Common subagents include:
  - `sysbench`: Database performance testing and benchmarking
- **task_description** (required): Detailed description of the task to be performed.
- **parameters** (optional): Additional parameters for the subagent (specific to each subagent type):
  - For sysbench: `test_type`, `threads`, `time`, `tables`, `table_size`, etc.

## Examples

Delegate performance test:
```
subagent: "sysbench"
task_description: "Execute performance test with 100 threads for 60 seconds"
parameters: {"threads": 100, "time": 60, "test_type": "oltp_read_write"}
```

---

## 中文翻译

将任务委派给专门的子智能体执行。

此工具允许主智能体将复杂任务委派给专门的子智能体。这些子智能体具有针对特定领域的专用系统提示词和工具集。

子智能体会从 prompts 目录中自动发现。每个子智能体都有自己的配置文件（例如 `sysbench_agent.yaml`），并可根据需要拥有自定义执行逻辑。

### 参数

- **subagent**（必填）：接收委派任务的子智能体。可用子智能体会自动发现。常见子智能体包括：
  - `sysbench`：数据库性能测试和基准测试
- **task_description**（必填）：待执行任务的详细描述。
- **parameters**（可选）：子智能体的附加参数（具体取决于子智能体类型）：
  - 对于 sysbench：`test_type`、`threads`、`time`、`tables`、`table_size` 等。

### 示例

委派性能测试：
```
subagent: "sysbench"
task_description: "使用 100 个线程执行性能测试，持续 60 秒"
parameters: {"threads": 100, "time": 60, "test_type": "oltp_read_write"}
```
