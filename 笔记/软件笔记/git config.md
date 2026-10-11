---
up:
  - "[[软件笔记]]"
tags:
  - 软件笔记
  - Git
---

# git config

> 配置 Git 的用户身份、别名与行为。

## 常用命令

| 命令 | 说明 |
|------|------|
| `git config --global user.name "名字"` | 设置用户名 |
| `git config --global user.email "邮箱"` | 设置邮箱 |
| `git config --list` | 查看全部配置 |
| `git config --global alias.st status` | 设置命令别名 |

## 示例

```bash
git config --global user.name "Alice"
git config --global user.email "alice@example.com"
git config --global alias.co checkout
```

## 要点

- 三个作用域：`--system`（本机）< `--global`（当前用户）< `--local`（当前仓库）
- 提交前必须配置 name 和 email，否则无法提交
- 别名能简化常用命令，如 `st` = `status`
