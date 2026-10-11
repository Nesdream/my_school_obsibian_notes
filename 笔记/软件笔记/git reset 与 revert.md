---
up:
  - "[[软件笔记]]"
tags:
  - 软件笔记
  - Git
---

# git reset 与 revert

> 回退提交：reset 移动指针（改写历史），revert 生成反向提交（保留历史）。

## 常用命令

| 命令 | 说明 |
|------|------|
| `git reset --soft HEAD~1` | 撤销最近提交，改动留在暂存区 |
| `git reset --mixed HEAD~1` | 撤销提交，改动回到工作区（默认） |
| `git reset --hard HEAD~1` | 撤销提交并丢弃所有改动 |
| `git revert <commit>` | 生成一个新提交来撤销指定提交 |

## 示例

```bash
git reset --soft HEAD~1     # 撤销提交但保留改动
git revert abc1234          # 安全撤销某次已推送的提交
```

## 要点

- `--hard` 会永久丢失未提交改动，务必确认后再用
- 已推送的提交用 `revert`（安全），不要用 reset 改写公开历史
- `reset` 参数区别：soft 留暂存区、mixed 留工作区、hard 全丢
