---
up:
  - "[[软件笔记]]"
tags:
  - 软件笔记
  - Git
---

# git rebase

> 把当前分支的提交「变基」到另一分支顶端，使历史呈线性。

## 常用命令

| 命令 | 说明 |
|------|------|
| `git rebase <branch>` | 将当前分支变基到指定分支 |
| `git rebase -i HEAD~n` | 交互式整理最近 n 次提交 |
| `git rebase --continue` | 解决冲突后继续 |
| `git rebase --abort` | 放弃变基 |

## 示例

```bash
git switch feature/login
git rebase main
# 冲突解决后
git add .
git rebase --continue
```

## 要点

- rebase 会改写提交历史，只用于自己的本地分支
- 已 push 的分支不要 rebase，否则协作者会混乱
- 与 merge 的区别：merge 保留分叉，rebase 拉直线性历史
