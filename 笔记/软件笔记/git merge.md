---
up:
  - "[[软件笔记]]"
tags:
  - 软件笔记
  - Git
---

# git merge

> 把另一个分支的改动合并到当前分支。

## 常用命令

| 命令 | 说明 |
|------|------|
| `git merge <branch>` | 将指定分支合并进当前分支 |
| `git merge --no-ff <branch>` | 保留合并提交（不做快进） |
| `git merge --abort` | 放弃合并，回到合并前状态 |

## 示例

```bash
git switch main
git merge feature/login
```

## 要点

- 无分叉时默认「快进合并」，不产生合并提交；`--no-ff` 可强制保留分支历史
- 冲突时 Git 会标记冲突文件，手动解决后 `git add` + `git commit`
- 想撤销冲突中的合并，用 `git merge --abort`
