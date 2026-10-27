Manage task breakdown and progress tracking for complex database operations.

**When to use:**
- Multi-table correlation analysis (e.g., cross-table performance diagnosis)
- Complex performance troubleshooting workflows
- Schema design or migration tasks with multiple steps
- Any task with 3+ distinct subtasks or milestones

**DO NOT use for:**
- Simple questions (e.g., "What indexes does table X have?")
- Single-tool operations (e.g., "Show slow queries from today")
- Tasks with only 1-2 steps
- Direct instructions that can be executed immediately

**Parameters:**
- **todos**: List of todo items, each with:
  - **title**: Brief description of the subtask
  - **status**: One of "Pending", "In Progress", or "Done"

**Usage notes:**
- Update the entire list each time (this is a replace operation, not append)
- Mark items "Done" as you complete them
- Keep only one item "In Progress" at a time
- Be flexible: start without todos for simple tasks, add them if complexity emerges

---

## 中文翻译

管理复杂数据库操作的任务拆解和进度跟踪。

**使用场景：**
- 多表关联分析（例如跨表性能诊断）
- 复杂的性能排查流程
- 包含多个步骤的模式设计或迁移任务
- 任何包含 3 个或更多独立子任务或里程碑的任务

**请勿用于：**
- 简单问题（例如“表 X 有哪些索引？”）
- 只需一个工具的操作（例如“显示今天的慢查询”）
- 仅有 1–2 个步骤的任务
- 可以立即执行的直接指令

**参数：**
- **todos**：待办事项列表，每项包含：
  - **title**：子任务的简短描述
  - **status**：取值为 "Pending"（待处理）、"In Progress"（进行中）或 "Done"（已完成）之一

**使用说明：**
- 每次更新整个列表（这是替换操作，不是追加操作）
- 完成事项后，将其标记为 "Done"
- 同一时间仅保留一个状态为 "In Progress" 的事项
- 灵活使用：简单任务开始时无需创建待办事项；如果任务变得复杂，再添加待办事项
