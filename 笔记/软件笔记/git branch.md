---
up:
  - "[[软件笔记]]"
tags:
  - 软件笔记
  - Git
---

# git branch

> 创建、查看、删除分支，实现并行开发。

## 常用命令

| 命令 | 说明 |
|------|------|
| `git branch` | 列出本地分支 |
| `git branch -a` | 列出本地 + 远程分支 |
| `git branch <name>` | 创建分支（不切换） |
| `git branch -d <name>` | 删除已合并的分支 |
| `git branch -D <name>` | 强制删除分支 |
| `git branch -m <新名>` | 重命名当前分支 |

## 示例

```bash
git branch feature/login   # 创建
git branch -d feature/login  # 删除
```

## 要点

- `HEAD` 指向当前所在分支，切换分支就是移动 HEAD
- 删除前用 `-d`（安全，未合并不让删），确认丢弃才用 `-D`
- 创建分支后需配合 checkout / switch 切换过去
