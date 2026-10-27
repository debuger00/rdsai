Analyze SQL query execution plan using MySQL EXPLAIN. **ONLY supports DML statements: SELECT, INSERT, UPDATE, DELETE.**

**When to use:**
- Analyze slow SELECT queries to understand index usage and join order
- Check execution plan before running INSERT/UPDATE/DELETE on large tables
- Performance tuning and query optimization
- Debugging query performance issues

**Supported SQL Types (DML ONLY):**
- ✅ **SELECT** - Query execution plans
- ✅ **INSERT** - Insert operation plans
- ✅ **UPDATE** - Update operation plans
- ✅ **DELETE** - Delete operation plans

**NOT Supported - DO NOT USE THIS TOOL FOR:**
- ❌ **SHOW statements** - These are MySQL administrative commands, NOT DML. Use `Show` tool instead
- ❌ **DDL statements** (CREATE, ALTER, DROP, etc.) - Use **DDLExecutor** tool instead
- ❌ **SET commands** - Execute directly in REPL
- ❌ **USE database** - Execute directly in REPL
- ❌ **Any non-DML statement** - This tool ONLY works with DML (SELECT/INSERT/UPDATE/DELETE)

**Important:** EXPLAIN only works with DML statements that access/modify table data. SHOW statements are administrative commands and cannot be analyzed with EXPLAIN.

**Parameters:**
- **sql**: The SQL DML statement to analyze (must be SELECT, INSERT, UPDATE, or DELETE only)

Returns execution plan showing tables accessed, indexes used, join order, and estimated row counts.

---

## 中文翻译

使用 MySQL EXPLAIN 分析 SQL 查询执行计划。**仅支持 DML 语句：SELECT、INSERT、UPDATE、DELETE。**

**使用场景：**
- 分析慢 SELECT 查询，了解索引使用情况和连接顺序
- 在大表上执行 INSERT/UPDATE/DELETE 之前检查执行计划
- 性能调优和查询优化
- 排查查询性能问题

**支持的 SQL 类型（仅限 DML）：**
- ✅ **SELECT**——查询执行计划
- ✅ **INSERT**——插入操作计划
- ✅ **UPDATE**——更新操作计划
- ✅ **DELETE**——删除操作计划

**不支持的操作——请勿将此工具用于：**
- ❌ **SHOW 语句**——它们是 MySQL 管理命令，不是 DML。请改用 `Show` 工具
- ❌ **DDL 语句**（CREATE、ALTER、DROP 等）——请改用 **DDLExecutor** 工具
- ❌ **SET 命令**——请直接在 REPL 中执行
- ❌ **USE database**——请直接在 REPL 中执行
- ❌ **任何非 DML 语句**——此工具仅适用于 DML（SELECT/INSERT/UPDATE/DELETE）

**重要说明：** EXPLAIN 仅适用于访问或修改表数据的 DML 语句。SHOW 语句属于管理命令，无法使用 EXPLAIN 分析。

**参数：**
- **sql**：要分析的 SQL DML 语句（必须且只能是 SELECT、INSERT、UPDATE 或 DELETE）

返回执行计划，展示访问的表、使用的索引、连接顺序和预估行数。
