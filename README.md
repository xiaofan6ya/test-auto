# test-auto

GH Sentinel 自动监控与审查闭环测试仓库。

本仓库故意保留一个缺陷，用于验证「issue → LLM 审查 → 下派 DeepSeek Harness → 回收 → 验收 → 致谢」整条固定循环。

## 已知问题

`calc.divide(1, 0)` 会抛出未处理的 `ZeroDivisionError`，见 issue #1。
