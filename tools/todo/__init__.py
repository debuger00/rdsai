from pathlib import Path
from typing import Literal, override

from loop.toolset import BaseTool, ToolOk, ToolReturnType
from pydantic import BaseModel, Field

from tools.utils import load_desc

## 让大模型 把复杂任务拆成 代办事项， 并把当前进度展示给用户

class Todo(BaseModel):
    """
        -title : 任务名
        -status: 当前状态 pending, in 
    """
    title: str = Field(description="The title of the todo", min_length=1)
    status: Literal["Pending", "In Progress", "Done"] = Field(description="The status of the todo")


class Params(BaseModel):
    todos: list[Todo] = Field(description="The updated todo list")


class TodoList(BaseTool[Params]):
    name: str = "TodoList"
    description: str = load_desc(Path(__file__).parent / "todo_list.md")# 加载skills.md 或者说时
    params: type[Params] = Params

    @override
    async def __call__(self, params: Params) -> ToolReturnType:
        rendered = ""
        for todo in params.todos:
            match todo.status:
                case "Done":
                    rendered += f"- ~~{todo.title}~~ [{todo.status}]\n"
                case "In Progress":
                    rendered += f"- **{todo.title}** [{todo.status}]\n"
                case _:
                    rendered += f"- {todo.title} [{todo.status}]\n"
        return ToolOk(output="", message="Todo list updated", brief=rendered)
