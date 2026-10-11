---
up:
  - "[[软件笔记]]"
tags:
  - 软件笔记
  - Git
---

# git remote、fetch、pull 与 push

> 与远程仓库交互：管理地址、拉取更新、推送本地提交。

## 常用命令

| 命令 | 说明 |
|------|------|
| `git remote -v` | 查看远程仓库地址 |
| `git remote add origin <url>` | 添加远程仓库 |
| `git fetch` | 拉取远程更新但不合并 |
| `git pull` | 拉取并合并到当前分支（fetch + merge） |
| `git push` | 推送本地提交到远程 |
| `git push -u origin main` | 首次推送并设置上游分支 |

## 示例

```bash
git remote add origin https://github.com/user/repo.git
git push -u origin main
git pull
```

## 要点

- `fetch` 只下载不改工作区，`pull` = fetch + merge，改动前建议先 fetch 查看
- `push -u` 设置上游后，之后只需 `git push`
- push 前先 pull 同步，避免因落后被拒绝
