# ESA OpenAPI overview (2024-09-10) - Site Management, Configuration, DNS & Cache

API index for site management, configuration, DNS records, and cache rules. For parameter details see official docs.

## Site Management

- CreateSite - 添加站点
- ListSites - 列出站点 (支持分页和过滤)
- GetSite - 获取站点详情
- DeleteSite - 删除站点
- CheckSiteName - 检查站点名称可用性
- VerifySite - 验证站点所有权
- UpdateSiteAccessType - 更新接入方式 (CNAME/NS)
- UpdateSiteCoverage - 更新覆盖区域
- GetSiteCurrentNS - 获取当前NS服务器
- UpdateSiteVanityNS - 更新自定义NS
- UpdateSitePause - 暂停/恢复站点代理
- GetSitePause - 获取站点代理状态
- UpdateSiteNameExclusive - 设置站点独占
- GetSiteNameExclusive - 获取站点独占状态
- ActivateVersionManagement - 启用版本管理
- DeactivateVersionManagement - 禁用版本管理

## Site Configuration

- GetIPv6 - 获取IPv6配置
- UpdateIPv6 - 更新IPv6配置

## DNS Records

NS access: supports all record types. CNAME access: only `CNAME` and `A/AAAA`, and proxy (acceleration) cannot be disabled.

- CreateRecord - 创建DNS记录
- ListRecords - 列出DNS记录 (支持Type, RecordName, Proxied过滤)
- GetRecord - 获取DNS记录详情
- UpdateRecord - 更新DNS记录
- DeleteRecord - 删除DNS记录
- BatchCreateRecords - 批量创建DNS记录
- ExportRecords - 导出DNS记录

## Cache Rules

- CreateCacheRule - 创建缓存规则
- ListCacheRules - 列出缓存规则
- GetCacheRule - 获取缓存规则详情
- UpdateCacheRule - 更新缓存规则
- DeleteCacheRule - 删除缓存规则

## References

- Official API list: https://next.api.aliyun.com/document/ESA/2024-09-10/overview
- API metadata: https://api.aliyun.com/meta/v1/products/ESA/versions/2024-09-10/api-docs.json
