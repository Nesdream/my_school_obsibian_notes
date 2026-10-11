---
up:
  - "[[资源]]"
  - "[[软件工具]]"
软件工具描述: 基于 Mihomo（Clash Meta）内核的跨平台图形化代理客户端，Clash for Windows 的社区延续版
tags:
  - 翻墙软件
  - 网络代理
aliases:
  - Clash Verge
  - Clash Verge Rev
官网: https://clash-verge-rev.github.io/
GitHub: https://github.com/clash-verge-rev/clash-verge-rev
平台: Windows / macOS / Linux
---

# Clash Verge Rev

> [!链接]
> [官网](https://clash-verge-rev.github.io/)
> [GitHub](https://github.com/clash-verge-rev/clash-verge-rev)
> [下载](https://github.com/clash-verge-rev/clash-verge-rev/releases)

## 一句话总结

Clash Verge Rev 是 Clash for Windows 的社区延续版，基于 Tauri + Mihomo（Clash Meta）内核的跨平台代理客户端，提供图形化界面管理订阅、节点与分流规则，适合需要可视化配置 Clash 的用户。

## 核心价值

- **轻量高效**：Tauri + Rust 构建，比 Electron 客户端资源占用更低、更流畅
- **协议全面**：内置 Mihomo 内核，兼容 Clash YAML，支持 Hysteria2、VLESS Reality、TUIC v5 等新协议
- **开箱即用**：订阅导入、节点测速、系统代理、TUN 模式一站式完成

## 功能特性

| 模块 | 说明 |
|------|------|
| 订阅管理 | 导入 / 更新 / 切换多个机场订阅，支持本地与远程配置 |
| 节点选择 | 手动切换，或按 url-test / fallback 自动择优 |
| 分流模式 | 规则 / 全局 / 直连三种模式 |
| 系统代理 | 一键接管 HTTP / HTTPS 流量 |
| TUN 模式 | 虚拟网卡接管全流量（含 UDP / ICMP） |
| 其他 | 开机自启、延迟测试、局域网共享、代理链等 |

## 平台支持

- Windows：x64 / x86 / arm64，提供 .exe 安装包
- macOS：Apple Silicon（aarch64）/ Intel（x64），提供 .dmg
- Linux：x64 / arm64，提供 .deb / .rpm
- 移动端：不支持（可用 Clash Meta for Android 等替代）

## 安装方式

- 安装包：GitHub Releases 下载对应平台安装包（推荐，仅用官方渠道）
- 包管理器：部分平台可通过 winget / Homebrew 等社区包安装
- 源码编译：pnpm + Tauri 自行构建（开发者）

## 系统要求

- 最低配置：64 位系统；Windows 需 WebView2 Runtime，macOS 需 Intel 或 Apple Silicon
- 推荐配置：TUN 模式需管理员权限或开启服务模式

## 如何使用

### 首次使用四步

1. **获取订阅**：在服务商后台复制 Clash 订阅链接（优先 Meta / Mihomo / Verge 兼容的 HTTPS 链接）
2. **导入配置**：左侧「订阅」→ 粘贴链接 → 导入 → 单击订阅卡片设为激活
3. **选择节点**：左侧「代理」→ 选择分组与节点，可点测速初筛
4. **开启代理**：「设置」→ 打开「系统代理」开关（可选开启开机自启）

### 代理模式

- **规则（Rule）**：日常首选，国内直连、国外走代理，省流量不影响国内网速
- **全局（Global）**：所有流量走代理，适合需要统一出口的场景
- **直连（Direct）**：不走代理，用于暂停代理或排查

### 系统代理 vs TUN 模式

| 对比项 | 系统代理 | TUN 模式 |
|--------|----------|----------|
| 接管范围 | HTTP / HTTPS 为主 | 全流量（含 UDP / ICMP） |
| 是否依赖应用支持 | 是 | 否，全局接管 |
| 性能开销 | 低 | 中等 |
| 权限要求 | 较低 | 需服务模式 / 管理员权限 |
| 适用场景 | 浏览器、支持代理的应用 | 命令行、游戏、语音、不读系统代理的软件 |

### 开启 TUN 模式

1. 「设置」→ 系统设置 → 开启「虚拟网卡模式」
2. 提示需要服务模式时，点击「安装服务」并授权
3. 确认内核切换到服务模式后，再打开 TUN 开关
4. 开启 TUN 后可关闭系统代理，避免重复设置

**使用建议：**

- 日常先开「系统代理 + 规则模式」，浏览器和多数应用够用即可
- 命令行工具（Git、包管理器）、游戏、语音不走代理时，再单独开 TUN
- 排查问题时一次只改一层（订阅 / DNS / TUN / 端口），避免混淆

## 注意事项

- **仅从官方下载**：只从 GitHub Releases 获取安装包，避免二传、网盘打包或不明镜像
- **订阅链接勿外泄**：订阅 URL 常含令牌 / 隐私参数，不要公开粘贴
- **TUN 与 VPN 冲突**：开启 TUN 前先退出 WireGuard / OpenVPN / 游戏加速器等，避免多虚拟网卡互相干扰
- **Windows 白屏**：多为缺少 WebView2 Runtime，安装后重启，或用带 Fixed_webview2 的版本
- **macOS 提示损坏**：终端执行 `sudo xattr -rd com.apple.quarantine /Applications/Clash Verge.app`（路径以实际为准）
- **开启 TUN 后 DNS 变化**：系统 DNS 可能被改为 223.6.6.6，关闭 TUN 即恢复

## 相关链接

- 官网：https://clash-verge-rev.github.io/
- GitHub：https://github.com/clash-verge-rev/clash-verge-rev
- 下载：https://github.com/clash-verge-rev/clash-verge-rev/releases
- 文档：官方 Wiki / GitHub Discussions

## 社区生态

- 社区 / 论坛：GitHub Issues / Discussions
- 贡献方式：GitHub 提交 issue、PR，参与翻译与文档
- 插件 / 扩展：支持外部规则集（geosite / geoip）与自定义配置

## 替代品

- Clash for Windows（原版，已停止维护）
- FlClash
- Mihomo Party
- Clash N
