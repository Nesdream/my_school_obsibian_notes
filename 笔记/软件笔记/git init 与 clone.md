---
up:
  - "[[软件笔记]]"
tags:
  - 软件笔记
  - Git
---

# git init 与 clone

> 创建新仓库或复制已有仓库，是使用 Git 的第一步。

## 常用命令

| 命令 | 说明 |
|------|------|
| `git init` | 在当前目录初始化新仓库 |
| `git init <目录>` | 在指定目录初始化 |
| `git clone <url>` | 克隆远程仓库到本地 |
| `git clone <url> <目录>` | 克隆到指定目录名 |
| `git clone --depth 1 <url>` | 浅克隆，只取最近一次提交 |

## 示例

```bash
# 初始化新仓库
git init
git add .
git commit -m "初始提交"

# 克隆已有仓库
git clone https://github.com/user/repo.git
```

## 要点

- `init` 之后仓库仍是空的，需要 `add` + `commit` 才会产生第一个提交
- `clone` 会自动把远程仓库设为 `origin`，无需手动配置
- 历史很大时可先用 `--depth 1` 浅克隆加速
