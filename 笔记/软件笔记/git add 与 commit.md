---
up:
  - "[[软件笔记]]"
tags:
  - 软件笔记
  - Git
---

# git add 与 commit

> 把改动加入暂存区（add），再提交进版本历史（commit）。

## 常用命令

| 命令 | 说明 |
|------|------|
| `git add <file>` | 将指定文件加入暂存区 |
| `git add .` | 加入当前目录所有改动 |
| `git add -A` | 加入全部改动（含删除） |
| `git add -p` | 交互式分块选择要暂存的内容 |
| `git commit -m "说明"` | 提交暂存区内容 |
| `git commit -am "说明"` | 暂存已跟踪文件并提交（不含未跟踪文件） |
| `git commit --amend` | 修改最近一次提交 |

## 示例

```bash
git add README.md
git add .
git commit -m "feat: 添加使用说明"
```

## 要点

- Git 有三个区域：工作区 → 暂存区 → 仓库，`add` 和 `commit` 分两步完成
- `commit -am` 只对已跟踪文件生效，新文件仍需先 `git add`
- `--amend` 用于修正上一次提交的说明或漏加的文件
