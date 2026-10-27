Execute sysbench performance tests. This tool runs the actual benchmark and collects performance metrics.

**When to use:**
- After preparing test data with SysbenchPrepare
- Performance benchmarking and load testing
- Comparing performance under different configurations
- Stress testing database systems

**Prerequisites:**
- Test data must be prepared using SysbenchPrepare
- Database connection must be established
- sysbench must be installed and available in PATH

**Parameters:**
- **test_type**: Test type (default: oltp_read_write). Must match the test_type used in SysbenchPrepare.
- **threads**: Number of concurrent threads (default: 1, max: 1000)
- **time**: Test duration in seconds (default: 60 if not specified, max: 3600). Either time or events must be specified.
- **events**: Total number of events to execute (alternative to time). Either time or events must be specified.
- **rate**: Target transactions per second for rate limiting (optional)
- **report_interval**: Report interval in seconds (default: 10, max: 300)
- **tables**: Number of tables to use (default: 1, max: 100). Must match or be less than tables prepared.
- **table_size**: Table size in rows (optional). If not specified, uses existing tables from prepare.

**Performance Metrics:**
The tool reports:
- **TPS**: Transactions per second
- **QPS**: Queries per second
- **Latency**: Average latency in milliseconds

**Important:**
- Running performance tests can put significant load on the database
- Use appropriate thread counts and durations
- Monitor database resources during testing
- Consider running during maintenance windows for production systems


---

## 中文翻译

执行 sysbench 性能测试。此工具运行实际的基准测试并收集性能指标。

**使用场景：**
- 使用 SysbenchPrepare 准备测试数据之后
- 性能基准测试和负载测试
- 比较不同配置下的性能
- 对数据库系统进行压力测试

**前提条件：**
- 必须已使用 SysbenchPrepare 准备测试数据
- 必须已建立数据库连接
- 必须已安装 sysbench，且可通过 PATH 访问

**参数：**
- **test_type**：测试类型（默认：oltp_read_write）。必须与 SysbenchPrepare 中使用的 test_type 一致。
- **threads**：并发线程数（默认：1，最大：1000）
- **time**：测试持续时间，单位为秒（未指定时默认为 60，最大：3600）。必须指定 time 或 events 之一。
- **events**：要执行的事件总数（可代替 time）。必须指定 time 或 events 之一。
- **rate**：用于限速的目标每秒事务数（可选）
- **report_interval**：报告间隔，单位为秒（默认：10，最大：300）
- **tables**：要使用的表数量（默认：1，最大：100）。必须等于或少于已准备的表数量。
- **table_size**：表的行数（可选）。如果未指定，则使用准备阶段创建的现有表。

**性能指标：**
此工具报告以下指标：
- **TPS**：每秒事务数
- **QPS**：每秒查询数
- **Latency**：平均延迟，单位为毫秒

**重要说明：**
- 运行性能测试可能给数据库带来较大负载
- 使用合适的线程数和测试时长
- 测试期间监控数据库资源
- 对于生产系统，考虑在维护窗口期间运行测试
