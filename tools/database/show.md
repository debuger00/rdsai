Execute SHOW statements for various database information queries.

**When to use:**
- Querying system variables: `SHOW VARIABLES`, `SHOW VARIABLES LIKE 'pattern'`, `SHOW GLOBAL VARIABLES`
- Viewing process list: `SHOW PROCESSLIST`
- Checking table status: `SHOW TABLE STATUS`, `SHOW TABLE STATUS FROM database_name`
- Viewing indexes: `SHOW INDEX FROM table_name`
- Checking InnoDB status: `SHOW ENGINE INNODB STATUS`
- Checking replication status: `SHOW REPLICA STATUS` (MySQL 8.0.22+) or `SHOW SLAVE STATUS` (older versions)
- Viewing table structure: `SHOW CREATE TABLE table_name`
- Other SHOW commands as needed

**Parameters:**
- **show_statement**: The complete SHOW statement to execute. The model should construct the full statement including all necessary clauses (LIKE, FROM, etc.).

**Examples:**
- `SHOW VARIABLES LIKE 'max_connections'`
- `SHOW GLOBAL VARIABLES LIKE '%timeout%'`
- `SHOW PROCESSLIST`
- `SHOW TABLE STATUS FROM mydb`
- `SHOW INDEX FROM users`
- `SHOW CREATE TABLE orders`
- `SHOW ENGINE INNODB STATUS`
- `SHOW REPLICA STATUS`

**Note:** This tool only accepts SHOW statements. Use Select for SELECT queries and DDLExecutor for DDL operations.

---

## 中文翻译

执行 SHOW 语句，用于查询各类数据库信息。

**使用场景：**
- 查询系统变量：`SHOW VARIABLES`、`SHOW VARIABLES LIKE 'pattern'`、`SHOW GLOBAL VARIABLES`
- 查看进程列表：`SHOW PROCESSLIST`
- 检查表状态：`SHOW TABLE STATUS`、`SHOW TABLE STATUS FROM database_name`
- 查看索引：`SHOW INDEX FROM table_name`
- 检查 InnoDB 状态：`SHOW ENGINE INNODB STATUS`
- 检查复制状态：`SHOW REPLICA STATUS`（MySQL 8.0.22+）或 `SHOW SLAVE STATUS`（旧版本）
- 查看表结构：`SHOW CREATE TABLE table_name`
- 按需执行其他 SHOW 命令

**参数：**
- **show_statement**：要执行的完整 SHOW 语句。模型应构造包含所有必要子句（LIKE、FROM 等）的完整语句。

**示例：**
- `SHOW VARIABLES LIKE 'max_connections'`
- `SHOW GLOBAL VARIABLES LIKE '%timeout%'`
- `SHOW PROCESSLIST`
- `SHOW TABLE STATUS FROM mydb`
- `SHOW INDEX FROM users`
- `SHOW CREATE TABLE orders`
- `SHOW ENGINE INNODB STATUS`
- `SHOW REPLICA STATUS`

**注意：** 此工具仅接受 SHOW 语句。SELECT 查询请使用 Select，DDL 操作请使用 DDLExecutor。
