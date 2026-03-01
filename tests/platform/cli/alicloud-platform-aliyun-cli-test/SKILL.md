---
name: alicloud-platform-aliyun-cli-test
description: Minimal smoke test for generic Alibaba Cloud aliyun CLI skill. Validate CLI install, auth profile, and one read-only API call.
---

Category: test

# 通用 aliyun CLI 最小可用测试

## 前置条件

- 已安装 `aliyun` CLI。
- 已配置可用 profile（默认 `default`）。
- 目标技能：`skills/platform/cli/alicloud-platform-aliyun-cli/`。

## 测试步骤

1) 执行版本保障脚本：`python skills/platform/cli/alicloud-platform-aliyun-cli/scripts/ensure_aliyun_cli.py --interval-hours 24`。
2) 执行 `aliyun version`。
3) 执行 `aliyun configure list`。
4) 执行一个只读 API（示例）：`aliyun ecs DescribeRegions`。

## 期望结果

- CLI 可执行并返回版本信息。
- `configure list` 显示有效凭证/profile（或明确缺失提示）。
- 只读 API 返回 JSON（或明确权限错误）。
