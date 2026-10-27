Prepare test data for sysbench performance testing. This tool creates tables and inserts test data into the database.

**When to use:**
- Before running performance tests with SysbenchRun
- Setting up test environment for benchmarking
- Creating test data for load testing

**Prerequisites:**
- Database connection must be established
- sysbench must be installed and available in PATH
- Database user must have CREATE, INSERT, and SELECT privileges

**Parameters:**
- **test_type**: Test type (default: oltp_read_write). Common types:
  - `oltp_read_write`: OLTP read-write workload
  - `oltp_read_only`: OLTP read-only workload
  - `select`: Simple SELECT queries
  - `insert`: INSERT operations
  - `update_index`: UPDATE operations with index
  - `delete`: DELETE operations
- **tables**: Number of tables to create (default: 1, max: 100)
- **table_size**: Number of rows per table (default: 10000, max: 100000000)
- **threads**: Number of threads for data preparation (default: 1, max: 32)

**Note:** Data preparation can take time depending on table_size and tables. Large datasets may require several minutes.

**Example workflow:**
1. Use SysbenchPrepare to create test data
2. Use SysbenchRun to execute performance tests
3. Use SysbenchCleanup to remove test data


---

## 中文翻译

为 sysbench 性能测试准备测试数据。此工具会在数据库中创建表并插入测试数据。

**使用场景：**
- 使用 SysbenchRun 运行性能测试之前
- 搭建基准测试环境
- 为负载测试创建测试数据

**前提条件：**
- 必须已建立数据库连接
- 必须已安装 sysbench，且可通过 PATH 访问
- 数据库用户必须拥有 CREATE、INSERT 和 SELECT 权限

**参数：**
- **test_type**：测试类型（默认：oltp_read_write）。常见类型：
  - `oltp_read_write`：OLTP 读写负载
  - `oltp_read_only`：OLTP 只读负载
  - `select`：简单 SELECT 查询
  - `insert`：INSERT 操作
  - `update_index`：涉及索引的 UPDATE 操作
  - `delete`：DELETE 操作
- **tables**：要创建的表数量（默认：1，最大：100）
- **table_size**：每张表的行数（默认：10000，最大：100000000）
- **threads**：数据准备使用的线程数（默认：1，最大：32）

**注意：** 数据准备所需时间取决于 table_size 和 tables。大型数据集可能需要数分钟。

**工作流程示例：**
1. 使用 SysbenchPrepare 创建测试数据
2. 使用 SysbenchRun 执行性能测试
3. 使用 SysbenchCleanup 删除测试数据
