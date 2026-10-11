---
up:
  - "[[软件笔记]]"
tags:
  - 软件笔记
  - Git
---

# git status 与 log

> 查看当前工作区状态与提交历史，是最高频的两个查看命令。

## 常用命令

| 命令 | 说明 |
|------|------|
| `git status` | 查看工作区与暂存区状态 |
| `git status -s` | 简短格式输出 |
| `git log` | 查看提交历史 |
| `git log --oneline` | 每条提交一行显示 |
| `git log --graph` | 图形化显示分支结构 |
| `git log -n 5` | 只看最近 5 条 |

## 示例

```bash
git status
git log --oneline --graph -n 10
```

## 要点

- 每次提交前先用 `status` 确认哪些文件被改、哪些已暂存
- `log --oneline --graph` 组合能直观看出分支合并关系
- 按 `q` 退出 log 的分页视图
