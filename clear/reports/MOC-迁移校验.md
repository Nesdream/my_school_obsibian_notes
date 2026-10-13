# MOC 迁移校验记录（`Git 汇总` → `MOC - Git`）

> 对象：把 `笔记/软件笔记/Git 汇总.md` 改造成符合 `AGENTS.md` §十五 的主题地图。
> 用户批准：2026-10-13，原话「是，而且要考虑有人会阅读」。
> 取数时刻：**2026-10-13T13:16:32+08:00**（以 `clear/models/base_filter_check.out.json` 最新一次输出为准）（唯一来源 `clear/models/base_filter_check.out.json`；重跑后凡与本记录不符处，以它为准）。

## 一、判据逐条对照

| # | 判据 | 怎么核 | 结果 |
|---|---|---|---|
| 1 | `MOC - Git.md` 存在且非空；`Git 汇总.md` 不存在 | `ls 笔记/软件笔记/` ＋ 脚本 `artifacts` | ✅ 新文件 3594 B / 64 行（行数口径＝`count('
')`，与 `clear/models/base_filter_check.py` 的 `artifacts` 同源，不再手抄）；旧名 0 个 |
| 2 | `tags` 含 `type/MOC`、不含 `汇总`；`up` 仍指 `[[软件笔记]]` | 读 frontmatter | ✅ 三项都成立 |
| 3 | 知识点各带一句简介，简介逐字取自对应笔记的 `>` 行 | 脚本逐条比对（见 §三） | ✅ **14/14** 逐字一致，且恰好覆盖 `笔记/软件笔记/git*.md` 全部 14 篇，无漏无多 |
| 4 | 「应用场景」与「相关主题」两块都在 | grep 标题 | ✅ 两个 `##` 块都在 |
| 5 | 全库 0 处指向旧名的活链接；复跑脚本 `dangling` = 0 | `grep` ＋ 脚本 | ✅ 旧名 `Git 汇总` 在全库只剩 `AGENTS.md` 里**两处历史说明**（§八 `:147` 与 §十五 `:238`，都写明了已迁移），没有任何活链接；全库也没有任何文件带 `#汇总` 标签；**dangling = 0** |
| 6 | `.base` 过滤改为 `file.hasTag("type/MOC")` 后命中恰 1 条 | 脚本按 `obsidian.asar` 的真实语义求值 | ✅ 命中 `['笔记/软件笔记/MOC - Git.md']`，恰好 1 条，两个施受方向结果一致 |

## 二、本次取数（`generated_at = 2026-10-13T13:14:33+08:00`）

| 量 | 值 |
|---|---|
| wikilink 字面 / 未解析 | 146 / 21 |
| wikilink 渲染 / 未解析 | 126 / 8 |
| 未解析分桶 | code 13, input_content 2, template_placeholder 6（合计 21 = 未解析总数 21） |
| **dangling** | **0** |

字面总数从迁移前的 128 涨到 146，涨的是这份 MOC 里新增的出链（每条知识点与每条应用场景都带链）。分桶合计仍等于未解析总数，这是判据 6 要求的那一格。

## 三、14 条简介与源笔记的逐字比对

| 源笔记 | MOC 里的简介 | 比对 |
|---|---|---|
| `git init 与 clone.md` | 创建新仓库或复制已有仓库，是使用 Git 的第一步。 | 逐字一致 |
| `git config.md` | 配置 Git 的用户身份、别名与行为。 | 逐字一致 |
| `gitignore.md` | 用规则文件忽略无需版本管理的文件（依赖、日志、密钥等）。 | 逐字一致 |
| `git status 与 log.md` | 查看当前工作区状态与提交历史，是最高频的两个查看命令。 | 逐字一致 |
| `git add 与 commit.md` | 把改动加入暂存区（add），再提交进版本历史（commit）。 | 逐字一致 |
| `git diff.md` | 查看文件改动的具体差异，用于提交前检查或对比版本。 | 逐字一致 |
| `git branch.md` | 创建、查看、删除分支，实现并行开发。 | 逐字一致 |
| `git checkout 与 switch.md` | 切换分支或恢复文件；switch 是切换分支的专用新命令。 | 逐字一致 |
| `git merge.md` | 把另一个分支的改动合并到当前分支。 | 逐字一致 |
| `git rebase.md` | 把当前分支的提交「变基」到另一分支顶端，使历史呈线性。 | 逐字一致 |
| `git stash.md` | 把未提交的改动暂存起来，让工作区回到干净状态。 | 逐字一致 |
| `git reset 与 revert.md` | 回退提交：reset 移动指针（改写历史），revert 生成反向提交（保留历史）。 | 逐字一致 |
| `git 链接 GitHub.md` | 把本地 Git 仓库关联到 GitHub 远程仓库并推送。 | 逐字一致 |
| `git remote 与 push.md` | 与远程仓库交互：管理地址、拉取更新、推送本地提交。 | 逐字一致 |

比对方法：抽 MOC「核心知识点」段落里形如 `- [[X]] — Y` 的行，再取 `笔记/软件笔记/X.md` 中第一个以 `> ` 开头的行作 Y'，要求 `Y == Y'` 严格相等（不是「意思相近」）。**全部 14 条严格相等**。

页脚措辞曾笼统写成「上面每条的简介逐字取自对应笔记」，但「相关主题」段那两行不是取自源笔记的说明句，已收紧为「**「核心知识点」里**每一条的简介都逐字取自对应笔记开头的说明句」。

## 四、改了哪些既有文件

| 文件 | 原内容 | 新内容 | 为什么 |
|---|---|---|---|
| `笔记/软件笔记/软件笔记.md` | `>[[Git 汇总|Git]]` | `>[[MOC - Git|Git]]` | 主页 callout 的入链，文件改名后必须同步 |
| `资源/软件工具/Git.md` | `[[笔记/软件笔记/Git 汇总|Git 汇总]]` | `[[笔记/软件笔记/MOC - Git|MOC - Git]]` | 「使用笔记」一行的跨文件夹链接 |
| `数据库/软件笔记数据库.base` | `file.hasTag("汇总")` | `file.hasTag("type/MOC")` | 只换标签不换过滤条件，这个视图会当场空掉 |
| `笔记/软件笔记/Git 汇总.md` | （45 行 / 586 B，sha256 `614480a1825940121bfd1d21aa8ad26a8d78110e6d45dc860d6dde968bb5b423`） | → `笔记/软件笔记/MOC - Git.md`（sha256 `a71ee0a1fdc07892291a5593adf86a603b9669a35410dccbaafd463a6df75525`） | 按 §十五 迁移并补内容 |
| `AGENTS.md` | — | 7 处同步（§三 命名示例、§五 写法样例、§七 跨文件夹示例、§八 汇总标签处置、§九 路径示例、§十五 既有例外段） | 规则里的示例若指着不存在的文件就是坏的 |

## 五、残余风险与没做的事

1. `.base` 的**语义**已按 `obsidian.asar` 里的真实实现复刻求值，但「在 Obsidian 里打开这个视图看到什么」仍需人在界面里看一眼——脚本能证过滤式对，证不了渲染。
2. 应用场景里三处带条件的说法都取自源笔记的「要点」段（`git rebase.md:34-35` 的「只用于自己的本地分支／已 push 的分支不要 rebase」、`git reset 与 revert.md:31-32` 的 `--hard` 会丢改动／已推送用 `revert`、`git merge.md:31-32` 的冲突处理与 `--abort`、`git stash.md:34` 的适用场景），不是我加的判断。
3. **没做**：没有删掉 `汇总` 标签的「定义」——Obsidian 的标签是文件里写出来的，全库已无文件引用它，它自然消失。也没有顺手给其他主题建 MOC（§十五 要求建不建等用户点头）。

## 六、复算命令

```bash
python3 clear/models/base_filter_check.py
python3 -c "import json;d=json.load(open('clear/models/base_filter_check.out.json',encoding='utf-8'));print([v['hits'] for b in d['bases'] if '软件笔记' in b['path'] for v in b['views']])"
grep -rn 'Git 汇总' --include='*.md' --include='*.base' . | grep -v '^./clear/'
sha256sum '笔记/软件笔记/MOC - Git.md'
```
