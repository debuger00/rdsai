Execute MySQL DESCRIBE/DESC statements for viewing table structure and column information.

**When to use:**
- Viewing table column structure: `DESCRIBE table_name`, `DESC table_name`
- Getting CREATE TABLE statement: `SHOW CREATE TABLE table_name`
- Viewing column details: `SHOW COLUMNS FROM table_name`

**Parameters:**
- **desc_statement**: The complete DESCRIBE, DESC, or SHOW CREATE TABLE/SHOW COLUMNS statement to execute. The model should construct the full statement including the table name.

**Examples:**
- `DESCRIBE users`
- `DESC orders`
- `SHOW CREATE TABLE products`
- `SHOW COLUMNS FROM customers`

**Note:** This tool only accepts DESCRIBE/DESC/SHOW CREATE TABLE/SHOW COLUMNS statements. Use Select for SELECT queries and DDLExecutor for DDL operations.

---

## 中文翻译

执行 MySQL DESCRIBE/DESC 语句，用于查看表结构和列信息。

**使用场景：**
- 查看表的列结构：`DESCRIBE table_name`、`DESC table_name`
- 获取 CREATE TABLE 语句：`SHOW CREATE TABLE table_name`
- 查看列的详细信息：`SHOW COLUMNS FROM table_name`

**参数：**
- **desc_statement**：要执行的完整 DESCRIBE、DESC 或 SHOW CREATE TABLE/SHOW COLUMNS 语句。模型应构造包含表名的完整语句。

**示例：**
- `DESCRIBE users`
- `DESC orders`
- `SHOW CREATE TABLE products`
- `SHOW COLUMNS FROM customers`

**注意：** 此工具仅接受 DESCRIBE/DESC/SHOW CREATE TABLE/SHOW COLUMNS 语句。SELECT 查询请使用 Select，DDL 操作请使用 DDLExecutor。
