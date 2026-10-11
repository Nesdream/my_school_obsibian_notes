---
up:
  - "[[软件笔记]]"
tags:
  - 软件笔记
  - Git
---

# git 链接 GitHub

> 把本地 Git 仓库关联到 GitHub 远程仓库并推送。

## 常用命令

| 命令 | 说明 |
|------|------|
| `git remote add origin <url>` | 关联远程仓库 |
| `git remote -v` | 查看已关联的远程地址 |
| `git push -u origin main` | 首次推送并设置上游 |
| `ssh-keygen -t ed25519 -C "邮箱"` | 生成 SSH 密钥 |

## 示例

### HTTPS 方式

```bash
git remote add origin https://github.com/user/repo.git
git push -u origin main
```

### SSH 方式

```bash
ssh-keygen -t ed25519 -C "you@example.com"
# 把公钥粘贴到 GitHub → Settings → SSH and GPG keys
git remote add origin git@github.com:user/repo.git
git push -u origin main
```

## 要点

- GitHub 新建空仓库会给出 HTTPS 和 SSH 两种地址，任选其一
- HTTPS 每次推送需输入账号 / 访问令牌（PAT）；SSH 配好密钥后免密
- 首次推送用 `-u` 设置上游，之后只需 `git push`
- 推送前本地要有提交：`git init` → `git add` → `git commit`
