Clean up test data created by sysbench. This tool removes test tables and data from the database.

**When to use:**
- After completing performance tests
- Freeing up database space
- Cleaning up test environment
- Before running new tests with different configurations

**Prerequisites:**
- Test data must exist (created by SysbenchPrepare)
- Database connection must be established
- sysbench must be installed and available in PATH

**Parameters:**
- **test_type**: Test type (default: oltp_read_write). Must match the test_type used in SysbenchPrepare.
- **tables**: Number of tables to cleanup (optional). If not specified, cleans up all tables created by sysbench.

**Note:** Cleanup operations are irreversible. All test data will be permanently deleted.

**Best Practice:** Always cleanup test data after benchmarking to free up resources and avoid confusion with production data.


---

## 中文翻译

清理 sysbench 创建的测试数据。此工具会从数据库中删除测试表和数据。

**使用场景：**
- 完成性能测试后
- 释放数据库空间
- 清理测试环境
- 使用不同配置运行新测试之前

**前提条件：**
- 必须存在测试数据（由 SysbenchPrepare 创建）
- 必须已建立数据库连接
- 必须已安装 sysbench，且可通过 PATH 访问

**参数：**
- **test_type**：测试类型（默认：oltp_read_write）。必须与 SysbenchPrepare 中使用的 test_type 一致。
- **tables**：要清理的表数量（可选）。如果未指定，则清理 sysbench 创建的所有表。

**注意：** 清理操作不可逆。所有测试数据都将被永久删除。

**最佳实践：** 基准测试结束后，应始终清理测试数据，以释放资源并避免与生产数据混淆。
