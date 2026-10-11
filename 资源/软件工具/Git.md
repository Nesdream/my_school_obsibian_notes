---
up:
  - "[[资源]]"
  - "[[软件工具]]"
软件工具描述: 开源的分布式版本控制系统，用于跟踪文件变更与多人协作开发
tags:
  - 开发工具
aliases:
  - Git
官网: https://git-scm.com/
GitHub: https://github.com/git/git
平台: Windows / macOS / Linux
---

# Git

> [!链接]
> [官网](https://git-scm.com/)
> [GitHub](https://github.com/git/git)
> [下载](https://git-scm.com/downloads)

## 一句话总结

Git 是 Linus Torvalds 开发的分布式版本控制系统，用于跟踪文件变更、协同开发与代码管理，是软件开发的事实标准工具，适合所有需要版本管理的个人与团队。是团队开发的必备工具。

## 核心价值

- **分布式**：每个本地仓库都有完整历史，可离线提交，不依赖中央服务器
- **分支强大**：轻量分支、快速合并，支持并行开发与灵活工作流（如 Git Flow）
- **生态完善**：与 GitHub / GitLab / Gitee 等平台深度集成，社区资源丰富

## 功能特性

| 模块 | 说明 |
|------|------|
| 版本管理 | 快照式记录每次提交，可随时回退、对比、追溯历史 |
| 分支与合并 | 轻量分支、merge / rebase，支持并行开发 |
| 暂存区 | 通过 staging area 精细控制提交内容 |
| 协作 | 远程仓库、push / pull / fetch、PR 工作流 |
| 进阶 | 标签、钩子（hooks）、子模块、reflog、cherry-pick 等 |

## 平台支持

- Windows：Git for Windows（含 Git Bash）
- macOS：Xcode Command Line Tools / Homebrew
- Linux：各发行版包管理器（apt / dnf / pacman 等）

## 安装方式

- 安装包：官网下载对应平台安装包
- 包管理器：`brew install git`（macOS）、`apt install git`（Debian/Ubuntu）、`winget install Git.Git`（Windows）等
- 源码编译：从源码构建（进阶用户）

## 系统要求

- 最低配置：极低，几乎任何现代系统均可运行
- 推荐配置：无特殊要求；配合 SSH / GPG 签名更佳

## 如何使用

### 基本工作流

1. 初始化仓库：`git init` 或克隆 `git clone <url>`
2. 添加变更：`git add <file>`（加入暂存区）
3. 提交：`git commit -m "说明"`
4. 推送：`git push`（到远程仓库）
5. 拉取更新：`git pull`

### 常用命令速查

| 命令 | 作用 |
|------|------|
| `git status` | 查看工作区状态 |
| `git log` | 查看提交历史 |
| `git branch` | 查看 / 创建分支 |
| `git checkout` / `git switch` | 切换分支 |
| `git merge` / `git rebase` | 合并分支 |
| `git stash` | 暂存未提交改动 |
| `git reset` / `git revert` | 回退操作 |
| `git remote -v` | 查看远程仓库 |

**使用建议：**

- 提交前先 `git status` + `git diff` 检查改动
- 遵循规范的提交信息（如 Conventional Commits）
- 用 `.gitignore` 排除生成物、依赖与敏感文件

## 注意事项

- **不要提交敏感信息**：密钥、令牌、密码一旦入库，历史中难以彻底清除
- **大文件慎用 Git**：二进制大文件用 Git LFS 或外部存储
- **避免直接改历史**：`git push --force`、rebase 已推送的分支会影响协作者
- **配置身份**：首次使用先 `git config --global user.name / user.email`

## 相关链接

- 官网：https://git-scm.com/
- GitHub：https://github.com/git/git
- 下载：https://git-scm.com/downloads
- 文档：《Pro Git》https://git-scm.com/book/
- 使用笔记：[[笔记/软件笔记/Git 汇总|Git 汇总]]

## 社区生态

- 社区 / 论坛：GitHub Discussions、Stack Overflow
- 贡献方式：Git 邮件列表（git@vger.kernel.org）提交补丁
- 相关资源：Git Book（免费电子书）、GitHub Skills 交互式教程

## 替代品

- SVN（集中式版本控制）
- Mercurial（Hg）
- Fossil
