---
up:
  - "[[软件笔记]]"
tags:
  - 软件笔记
  - Git
---

# .gitignore

> 用规则文件忽略无需版本管理的文件（依赖、日志、密钥等）。

## 常用规则

| 写法 | 说明 |
|------|------|
| `*.log` | 忽略所有 .log 文件 |
| `node_modules/` | 忽略整个目录 |
| `!important.log` | 反向保留（不忽略） |
| `/build` | 只忽略根目录的 build |

## 示例

```gitignore
# 依赖与构建产物
node_modules/
dist/
*.log

# 敏感文件
.env
```

## 要点

- `.gitignore` 放在仓库根目录即可生效
- 只对未跟踪文件生效；已跟踪文件需先 `git rm --cached <file>` 移除
- 可用 `git check-ignore <file>` 验证某文件是否被忽略
