# MySQL DDL Executor

Execute DDL (Data Definition Language) operations on MySQL databases with user approval.

**Parameters:**
- **sql_statement**: The DDL SQL statement to execute
- **description**: A human-readable description of what the modification will do

**Supported Operations (DDL ONLY):**
- CREATE INDEX / CREATE UNIQUE INDEX
- DROP INDEX
- CREATE TABLE / DROP TABLE
- ALTER TABLE (add/drop columns, constraints, modify columns, etc.)
- CREATE VIEW / DROP VIEW
- CREATE PROCEDURE / DROP PROCEDURE
- CREATE FUNCTION / DROP FUNCTION
- CREATE TRIGGER / DROP TRIGGER

**NOT Supported - DO NOT USE THIS TOOL FOR:**
- ❌ **SELECT queries** - Use `Select` tool instead
- ❌ **INSERT, UPDATE, DELETE** - These are DML operations, not DDL
- ❌ **SHOW statements** - Use `Show` tool instead
- ❌ **DESCRIBE statements** - Use `Desc` tool instead
- ❌ **DROP DATABASE, CREATE DATABASE** - Blocked for safety
- ❌ **Any query that reads data** - This tool is ONLY for schema modifications

**When to Use:**
- When you need to modify database schema (add indexes, alter tables, etc.)
- When creating or dropping database objects (tables, views, procedures, etc.)

**When NOT to Use:**
- For reading data - use `Select`, `Show`, or `Desc` tools instead
- For DML operations (INSERT/UPDATE/DELETE) - not supported by this tool

**Safety Features:**
- User approval required for all modifications
- DDL operations only (no DML: INSERT/UPDATE/DELETE)
- Blocks dangerous operations like DROP DATABASE
- Validates SQL statement type before execution

**IMPORTANT: Execute ONE DDL operation at a time.** If you need to perform multiple DDL changes, call this tool once, wait for the result, then decide whether to proceed with the next operation. Do NOT batch multiple DDL calls in a single response.

---

## 中文翻译

### MySQL DDL 执行器

在获得用户批准后，对 MySQL 数据库执行 DDL（数据定义语言）操作。

**参数：**
- **sql_statement**：要执行的 DDL SQL 语句
- **description**：用易于理解的语言描述此次修改将执行什么操作

**支持的操作（仅限 DDL）：**
- CREATE INDEX / CREATE UNIQUE INDEX（创建索引 / 创建唯一索引）
- DROP INDEX（删除索引）
- CREATE TABLE / DROP TABLE（创建表 / 删除表）
- ALTER TABLE（添加或删除列、约束，修改列等）
- CREATE VIEW / DROP VIEW（创建视图 / 删除视图）
- CREATE PROCEDURE / DROP PROCEDURE（创建存储过程 / 删除存储过程）
- CREATE FUNCTION / DROP FUNCTION（创建函数 / 删除函数）
- CREATE TRIGGER / DROP TRIGGER（创建触发器 / 删除触发器）

**不支持的操作——请勿将此工具用于：**
- ❌ **SELECT 查询**——请改用 `Select` 工具
- ❌ **INSERT、UPDATE、DELETE**——这些是 DML 操作，不是 DDL
- ❌ **SHOW 语句**——请改用 `Show` 工具
- ❌ **DESCRIBE 语句**——请改用 `Desc` 工具
- ❌ **DROP DATABASE、CREATE DATABASE**——出于安全考虑已禁止
- ❌ **任何读取数据的查询**——此工具仅用于修改数据库模式

**使用场景：**
- 需要修改数据库模式（添加索引、修改表等）时
- 创建或删除数据库对象（表、视图、存储过程等）时

**不应使用的场景：**
- 读取数据——请改用 `Select`、`Show` 或 `Desc` 工具
- DML 操作（INSERT/UPDATE/DELETE）——此工具不支持

**安全特性：**
- 所有修改都需要用户批准
- 仅允许 DDL 操作（不允许 DML：INSERT/UPDATE/DELETE）
- 阻止 DROP DATABASE 等危险操作
- 执行前验证 SQL 语句类型

**重要：每次只执行一个 DDL 操作。** 如果需要执行多项 DDL 修改，请先调用此工具一次，等待结果后再决定是否继续下一项操作。不要在单次回复中批量发起多个 DDL 调用。
