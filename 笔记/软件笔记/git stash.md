---
up:
  - "[[软件笔记]]"
tags:
  - 软件笔记
  - Git
---

# git stash

> 把未提交的改动暂存起来，让工作区回到干净状态。

## 常用命令

| 命令 | 说明 |
|------|------|
| `git stash` | 暂存当前改动 |
| `git stash -u` | 连未跟踪文件一起暂存 |
| `git stash list` | 查看暂存列表 |
| `git stash pop` | 恢复最近一次并删除记录 |
| `git stash apply` | 恢复但不删除记录 |
| `git stash drop` | 删除某条暂存记录 |

## 示例

```bash
git stash            # 暂存
git switch main      # 干净切换
git stash pop        # 回来后恢复
```

## 要点

- 适合「改到一半需要切分支」的场景
- `pop` 会同时移除记录，`apply` 只恢复不移除
- 多次 stash 会堆叠，用 `stash list` 查看
