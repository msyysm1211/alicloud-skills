---
name: alicloud-platform-aliyun-cli
description: Alibaba Cloud generic CLI skill for installing, configuring, and using aliyun CLI to call OpenAPI actions across products. Use when users need command-line operations on Alibaba Cloud resources (list/query/create/update/delete), credential/profile setup, region/endpoint selection, or API discovery from CLI.
---

Category: tool

# 阿里云通用 CLI（aliyun）技能

## 目标

- 使用官方 `aliyun` CLI 执行阿里云 OpenAPI 操作。
- 提供安装、配置、API 发现、执行与排错的标准流程。

## 快速流程

1. 先执行版本保障脚本（先检查，再决定是否更新）。
2. 若未安装或到检查周期，脚本自动下载官方最新包安装。
3. 配置凭证与默认 Region（建议 `default` profile）。
4. 用 `aliyun <product> --help` / `aliyun <product> <ApiName> --help` 确认参数。
5. 先执行只读查询，再执行变更操作。

## 版本保障（实用方案）

优先使用本技能自带脚本，避免“每次都下载”的时间浪费：

```bash
python skills/platform/cli/alicloud-platform-aliyun-cli/scripts/ensure_aliyun_cli.py
```

默认行为：

- 检查周期：24 小时（可通过环境变量修改）。
- 周期内且版本满足要求：跳过下载。
- 超过周期/未安装/低于最低版本：自动下载官方最新安装包并覆盖安装。

可选控制项（环境变量）：

- `ALIYUN_CLI_CHECK_INTERVAL_HOURS=24`：检查周期。
- `ALIYUN_CLI_FORCE_UPDATE=1`：强制更新（忽略周期）。
- `ALIYUN_CLI_MIN_VERSION=3.2.9`：最低版本门槛。
- `ALIYUN_CLI_INSTALL_DIR=~/.local/bin`：安装目录。

手动参数示例：

```bash
python skills/platform/cli/alicloud-platform-aliyun-cli/scripts/ensure_aliyun_cli.py \
  --interval-hours 24 \
  --min-version 3.2.9
```

## 安装（Linux 示例）

```bash
curl -fsSL https://aliyuncli.alicdn.com/aliyun-cli-linux-latest-amd64.tgz -o /tmp/aliyun-cli.tgz
mkdir -p ~/.local/bin
tar -xzf /tmp/aliyun-cli.tgz -C /tmp
mv /tmp/aliyun ~/.local/bin/aliyun
chmod +x ~/.local/bin/aliyun
~/.local/bin/aliyun version
```

## 配置凭证

```bash
aliyun configure set \
  --profile default \
  --mode AK \
  --access-key-id <AK> \
  --access-key-secret <SK> \
  --region cn-hangzhou
```

查看已配置 profile：

```bash
aliyun configure list
```

## 命令结构

- 通用形式：`aliyun <product> <ApiName> --Param1 value1 --Param2 value2`
- REST 形式：`aliyun <product> [GET|POST|PUT|DELETE] <PathPattern> --body '...json...'`

## API 发现与参数确认

```bash
aliyun help
aliyun ecs --help
aliyun ecs DescribeRegions --help
```

## 常用只读示例

```bash
# ECS：列地域
aliyun ecs DescribeRegions

# ECS：列实例（按地域）
aliyun ecs DescribeInstances --RegionId cn-hangzhou

# SLS：列 Project（按 endpoint）
aliyun sls ListProject --endpoint cn-hangzhou.log.aliyuncs.com --size 100
```

## 常见问题

- `InvalidAccessKeyId.NotFound` / `SignatureDoesNotMatch`：检查 AK/SK 与 profile。
- `MissingRegionId`：补充 `--region` 或在 profile 中配置默认 Region。
- 调用 SLS 报 endpoint 错误：显式传 `--endpoint <region>.log.aliyuncs.com`。

## 执行建议

- 所有任务开始前先运行 `ensure_aliyun_cli.py`。
- 未明确资源范围时，先查询再变更。
- 涉及删除/覆盖类操作前，先输出将要变更的资源清单。
- 批量操作优先先小范围验证一条。

## 参考

- 官方文档来源清单：`references/sources.md`
