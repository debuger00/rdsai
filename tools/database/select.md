Execute SELECT queries for database diagnostics and system table analysis.

**IMPORTANT: This tool ONLY allows queries on system tables. User table queries are NOT permitted to prevent slow queries and performance issues.**

**When to use:**
- Query system tables ONLY: information_schema, performance_schema, sys, mysql
- InnoDB diagnostics: transactions, locks, buffer pool stats, metrics
- Performance analysis: query statistics, wait events, I/O metrics
- Query logs: slow_log, general_log
- Schema metadata: query information_schema for table/index metadata (but NOT user table data)

**DO NOT use for:**
- ❌ Querying user-created tables (e.g., `SELECT * FROM orders`)
- ❌ Querying user data from any database
- ❌ Any queries that may access business data

**Parameters:**
- **select_statement**: The complete SELECT statement to execute. MUST query system tables only (information_schema, performance_schema, sys, mysql). Include FROM, WHERE, JOIN, GROUP BY, ORDER BY, LIMIT, etc.

**Examples:**
- `SELECT * FROM information_schema.INNODB_TRX` - Active transactions
- `SELECT * FROM information_schema.INNODB_LOCKS` - Current locks
- `SELECT * FROM information_schema.INNODB_BUFFER_POOL_STATS` - Buffer pool statistics
- `SELECT * FROM performance_schema.events_statements_summary_by_digest ORDER BY sum_timer_wait DESC LIMIT 10`
- `SELECT * FROM mysql.slow_log ORDER BY start_time DESC LIMIT 100`
- `SELECT * FROM information_schema.TABLES WHERE table_schema='mydb'` - Table metadata (NOT table data)
- `SELECT * FROM sys.schema_table_statistics WHERE table_schema='mydb'` - Statistics (NOT table data)

**Note:** Only SELECT queries on system tables allowed. User table queries are blocked to prevent slow queries. Use Show for SHOW statements, Desc for DESCRIBE statements, and DDLExecutor for DDL operations.

---

## 中文翻译

执行 SELECT 查询，用于数据库诊断和系统表分析。

**重要：此工具仅允许查询系统表。为避免慢查询和性能问题，不允许查询用户表。**

**使用场景：**
- 仅查询系统表：information_schema、performance_schema、sys、mysql
- InnoDB 诊断：事务、锁、缓冲池统计信息、指标
- 性能分析：查询统计信息、等待事件、I/O 指标
- 查询日志：slow_log、general_log
- 模式元数据：查询 information_schema 以获取表或索引的元数据（但不能查询用户表数据）

**请勿用于：**
- ❌ 查询用户创建的表（例如 `SELECT * FROM orders`）
- ❌ 查询任何数据库中的用户数据
- ❌ 任何可能访问业务数据的查询

**参数：**
- **select_statement**：要执行的完整 SELECT 语句。必须仅查询系统表（information_schema、performance_schema、sys、mysql）。应包含 FROM、WHERE、JOIN、GROUP BY、ORDER BY、LIMIT 等子句。

**示例：**
- `SELECT * FROM information_schema.INNODB_TRX`——活跃事务
- `SELECT * FROM information_schema.INNODB_LOCKS`——当前的锁
- `SELECT * FROM information_schema.INNODB_BUFFER_POOL_STATS`——缓冲池统计信息
- `SELECT * FROM performance_schema.events_statements_summary_by_digest ORDER BY sum_timer_wait DESC LIMIT 10`
- `SELECT * FROM mysql.slow_log ORDER BY start_time DESC LIMIT 100`
- `SELECT * FROM information_schema.TABLES WHERE table_schema='mydb'`——表元数据（不是表数据）
- `SELECT * FROM sys.schema_table_statistics WHERE table_schema='mydb'`——统计信息（不是表数据）

**注意：** 仅允许对系统表执行 SELECT 查询。为避免慢查询，用户表查询会被阻止。SHOW 语句请使用 Show，DESCRIBE 语句请使用 Desc，DDL 操作请使用 DDLExecutor。
