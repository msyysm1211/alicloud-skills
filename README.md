# ESA Skills

阿里云边缘安全加速（Edge Security Acceleration, ESA）AI 编程助手技能集。

本仓库为 AI 编程助手（Qoder / Claude Code / Cursor 等）提供 ESA 产品的技能定义，使 AI 能够理解 ESA 的 API 体系并辅助完成站点管理、DNS 配置、缓存规则等操作。

## 目录结构

```
esa-skills/
├── SKILL.md                        # 技能主文档（入口）
├── agents/
│   └── openai.yaml                 # OpenAI Agent 配置
├── references/                     # API 参考文档
│   ├── api_overview.md             # API 全景总览
│   ├── endpoints.md                # Endpoint 地址
│   ├── sites.md                    # 站点管理 API
│   ├── dns-records.md              # DNS 记录 API
│   ├── cache.md                    # 缓存规则 API
│   ├── sources.md                  # 源站配置 API
│   ├── rule-generation-guide.md    # 规则表达式生成指南
│   ├── rule-match-fields.md        # 规则匹配字段参考
│   ├── rule-operators.md           # 规则运算符参考
│   └── rule-examples.md            # 规则表达式示例
├── scripts/                        # Python 运维脚本
│   ├── list_sites.py               # 列出所有站点
│   ├── check_site_status.py        # 检查站点状态
│   ├── list_dns_records.py         # 列出 DNS 记录
│   └── summary_sites_by_plan.py    # 按套餐汇总站点
└── README.md
```

## 覆盖能力

| 能力 | 说明 | 主要 API |
|------|------|----------|
| 站点管理 | 创建、查询、删除、验证站点 | CreateSite, ListSites, GetSite, DeleteSite, VerifySite |
| DNS 记录 | 增删改查 DNS 记录 | CreateRecord, ListRecords, UpdateRecord, DeleteRecord |
| 缓存规则 | 全局缓存、条件缓存规则配置 | CreateCacheRule, ListCacheRules, UpdateCacheRule |
| 源站配置 | 源站回源管理 | 详见 references/sources.md |
| 规则表达式 | ESA 统一规则引擎语法 | 支持 eq/ne/in/contains/starts_with/ends_with/matches |

## 快速开始

### 1. 环境准备

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install alibabacloud_esa20240910 alibabacloud_tea_openapi alibabacloud_credentials
```

### 2. 配置凭证

通过环境变量设置 AccessKey：

```bash
export ALICLOUD_ACCESS_KEY_ID="your-ak"
export ALICLOUD_ACCESS_KEY_SECRET="your-sk"
```

或通过共享凭证文件 `~/.alibabacloud/credentials`：

```ini
[default]
type = access_key
access_key_id = your-ak
access_key_secret = your-sk
```

### 3. 运行脚本

```bash
# 列出所有 ESA 站点
python scripts/list_sites.py

# JSON 格式输出
python scripts/list_sites.py --json

# 检查站点状态
python scripts/check_site_status.py --site-id <site_id>

# 列出站点 DNS 记录
python scripts/list_dns_records.py --site-id <site_id>

# 按套餐汇总站点
python scripts/summary_sites_by_plan.py
```

## AI 编程助手集成

### Qoder / Claude Code

将本仓库克隆到项目中，或将 `SKILL.md` 放置在 `.qoder/skills/alibabacloud-esa/` 目录下：

```bash
# 方式一：作为项目 skill
mkdir -p .qoder/skills/alibabacloud-esa
cp -r <this-repo>/* .qoder/skills/alibabacloud-esa/

# 方式二：直接引用
# AI 助手会自动识别 SKILL.md 并获取 ESA 操作能力
```

### 使用示例

与 AI 编程助手的典型对话：

- "帮我列出所有 ESA 站点"
- "为站点配置全局不缓存，访问 /static/ 目录时缓存 7 天"
- "添加一条 CNAME 记录指向源站"
- "检查站点 qoder.example.com 的状态"

## 技术栈

- **产品**: 阿里云 ESA（边缘安全加速）
- **API 版本**: 2024-09-10
- **SDK**: alibabacloud_esa20240910 (Python)
- **API 风格**: RPC
- **Endpoint**: esa.cn-hangzhou.aliyuncs.com

## 相关链接

- [ESA 产品文档](https://help.aliyun.com/zh/esa/)
- [ESA API 参考](https://help.aliyun.com/zh/esa/developer-reference/)
- [OpenAPI Explorer](https://api.aliyun.com/api/ESA/2024-09-10)
