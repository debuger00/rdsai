Execute analytical SQL SELECT queries on MySQL or DuckDB databases for data analysis, exploration, and statistical insights.

**Primary Use:**
This tool is designed for data analysis queries that explore patterns, calculate statistics, perform aggregations, and generate insights from data. Use it for analytical queries that help understand data characteristics, trends, and relationships.

**Supported:**
- SELECT queries (including WITH/CTE, JOINs, aggregations, window functions, GROUP BY, ORDER BY)
- Statistical analysis: COUNT, SUM, AVG, MIN, MAX, STDDEV, etc.
- Data exploration: filtering, sorting, grouping, pivoting
- Both MySQL and DuckDB engines (check `<database_context>` for current engine and use appropriate SQL syntax)

**When to use:**
- Data analysis and exploration queries
- Statistical calculations and aggregations
- Trend analysis and pattern discovery
- Data profiling and summary statistics
- Cross-table analysis with JOINs
- Complex analytical queries with CTEs and window functions

**NOT Supported - DO NOT USE FOR:**
- DML (INSERT, UPDATE, DELETE) or DDL (CREATE, ALTER, DROP) - Use DDLExecutor for MySQL DDL
- EXPLAIN - Use MySQLExplain tool instead
- SHOW statements - Use MySQLShow tool instead
- DESCRIBE statements - Use MySQLDesc tool instead
- System table queries for diagnostics - Use MySQLSelect tool instead

**Parameters:**
- **sql**: SQL SELECT query to execute for data analysis. **CRITICAL**: MUST check `<database_context>` for the current database engine (MySQL or DuckDB) and generate SQL using the correct syntax for that engine. Do NOT mix syntax from different engines. Focus on analytical queries that provide insights, statistics, or data exploration.

**Examples:**
- `SELECT COUNT(*) as total, AVG(price) as avg_price FROM products WHERE category='electronics'`
- `SELECT category, SUM(sales) as total_sales FROM orders GROUP BY category ORDER BY total_sales DESC`
- `SELECT customer_id, COUNT(*) as order_count, SUM(amount) as total_spent FROM orders GROUP BY customer_id HAVING order_count > 5`
- `WITH monthly_sales AS (SELECT DATE_FORMAT(order_date, '%Y-%m') as month, SUM(amount) as sales FROM orders GROUP BY month) SELECT * FROM monthly_sales ORDER BY month`

Returns query results as structured data (columns and rows) with execution time. Large result sets are truncated for display.

---

## 中文翻译

在 MySQL 或 DuckDB 数据库上执行分析型 SQL SELECT 查询，用于数据分析、探索和统计洞察。

**主要用途：**
此工具专为数据分析查询设计，可用于探索规律、计算统计指标、执行聚合并从数据中提取洞察。适用于帮助理解数据特征、趋势和关联关系的分析型查询。

**支持的功能：**
- SELECT 查询（包括 WITH/CTE、JOIN、聚合、窗口函数、GROUP BY、ORDER BY）
- 统计分析：COUNT、SUM、AVG、MIN、MAX、STDDEV 等
- 数据探索：筛选、排序、分组、透视
- MySQL 和 DuckDB 两种引擎（检查 `<database_context>` 中的当前引擎，并使用相应的 SQL 语法）

**使用场景：**
- 数据分析和探索查询
- 统计计算和聚合
- 趋势分析和规律发现
- 数据概况分析和汇总统计
- 使用 JOIN 进行跨表分析
- 使用 CTE 和窗口函数进行复杂分析查询

**不支持的操作——请勿用于：**
- DML（INSERT、UPDATE、DELETE）或 DDL（CREATE、ALTER、DROP）——MySQL DDL 请使用 DDLExecutor
- EXPLAIN——请改用 MySQLExplain 工具
- SHOW 语句——请改用 MySQLShow 工具
- DESCRIBE 语句——请改用 MySQLDesc 工具
- 用于诊断的系统表查询——请改用 MySQLSelect 工具

**参数：**
- **sql**：用于数据分析的 SQL SELECT 查询。**关键要求**：必须检查 `<database_context>` 中的当前数据库引擎（MySQL 或 DuckDB），并使用该引擎的正确语法生成 SQL。不得混用不同引擎的语法。应专注于提供洞察、统计结果或数据探索的分析型查询。

**示例：**
- `SELECT COUNT(*) as total, AVG(price) as avg_price FROM products WHERE category='electronics'`
- `SELECT category, SUM(sales) as total_sales FROM orders GROUP BY category ORDER BY total_sales DESC`
- `SELECT customer_id, COUNT(*) as order_count, SUM(amount) as total_spent FROM orders GROUP BY customer_id HAVING order_count > 5`
- `WITH monthly_sales AS (SELECT DATE_FORMAT(order_date, '%Y-%m') as month, SUM(amount) as sales FROM orders GROUP BY month) SELECT * FROM monthly_sales ORDER BY month`

以结构化数据（列和行）的形式返回查询结果，并附带执行时间。较大的结果集在显示时会被截断。
