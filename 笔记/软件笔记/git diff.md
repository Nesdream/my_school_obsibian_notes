---
up:
  - "[[软件笔记]]"
tags:
  - 软件笔记
  - Git
---

# git diff

> 查看文件改动的具体差异，用于提交前检查或对比版本。

## 常用命令

| 命令 | 说明 |
|------|------|
| `git diff` | 工作区 vs 暂存区 |
| `git diff --staged` | 暂存区 vs 最近提交 |
| `git diff HEAD` | 工作区 + 暂存区 vs 最近提交 |
| `git diff <commit1> <commit2>` | 对比两个提交 |
| `git diff <file>` | 只看某个文件的差异 |

## 示例

```bash
# 提交前完整检查
git diff
git diff --staged

# 对比两个提交
git diff HEAD~1 HEAD
```

## 要点

- `git diff` 只看还没 `add` 的改动；`--staged` 才看已暂存的改动
- 提交前建议 `diff` + `status` 一起看，避免误提交
