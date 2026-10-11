---
up:
  - "[[软件笔记]]"
tags:
  - 软件笔记
  - Git
---

# git checkout 与 switch

> 切换分支或恢复文件；switch 是切换分支的专用新命令。

## 常用命令

| 命令 | 说明 |
|------|------|
| `git switch <branch>` | 切换到已有分支 |
| `git switch -c <name>` | 创建并切换新分支 |
| `git checkout <branch>` | 切换分支（旧写法） |
| `git checkout -b <name>` | 创建并切换（旧写法） |
| `git checkout -- <file>` | 丢弃工作区中文件的改动 |

## 示例

```bash
git switch main
git switch -c feature/pay
git checkout -- README.md   # 放弃未提交改动
```

## 要点

- 切换分支建议用 `switch`（语义清晰），`checkout` 保留兼容
- `checkout -- <file>` 会直接丢弃改动且无法找回，慎用
- 切换前若有未提交改动，Git 会阻止或提示，先 commit 或 stash
