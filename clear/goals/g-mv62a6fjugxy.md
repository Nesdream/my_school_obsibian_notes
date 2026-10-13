# Goal g-mv62a6fjugxy (rev2 · open)
- **Headline**: 给 school 库建「收集箱」入口与「项目」状态层，把消化流程写进 AGENTS.md，导航层保持人可读
- **Claim**: 怎样在不动既有笔记的前提下，为 school 知识库加上统一入口（收集箱）与三态项目层，并把「从入口到归位」的流程固定成可重复执行的规则？
- **Promotion threshold**: L3
- **Criteria (full text)** (not itemized):
  1) 新增文件全部存在且非空：收集箱/收集箱.md、项目/项目.md、数据库/收集箱数据库.base、数据库/项目数据库.base、模板/项目模板.md；2) 两个 .base 的 YAML 可被解析，且与库内已有 5 个 .base 同构（顶层 views 列表 + file.inFolder/file.hasTag 过滤），项目数据库含待处理/进行中/已完成 三个视图；3) 两个新主页的 up 链能回到 home，并在 home.md 各有 callout 挂载；4) home.md 原有 20 行一条未删；5) AGENTS.md 已同步：权限表含两个新目录、模板对照表含项目模板、标签规范含 status/ 与 type/ 命名空间、工作流含「消化收集箱」步骤与触发口令；6) 报告列出全部新增/修改文件，且全库 wikilink 无悬空（0 个指向不存在文件）。
> The system writes this file from the ledger (a projection); the authority is `goal/set` and `criteria/revised` in the ledger.
## Judgments (2)
- `h-dlq9i8` [alive] 用 #status/* 层级标签 + .base 的 file.hasTag 过滤，能在不移动任何文件的前提下把项目分成 待处理/进行中/已完成 三态视图
  - Refuted if: Obsidian 的 file.hasTag 不能对层级标签做精确匹配，或一个 .base 文件不能同时容纳多个视图（各自带过滤条件）
  - scope: {"conditions":{"既有笔记":"不动","库":"school","导航层":"保持不变","触发方式":"会话触发","插件":"核心 Bases 1.9+"},"ranges":{},"note":"只覆盖 Obsidian 核心 Bases；社区插件视图不在范围内"}
  - uses (framing declarations): []
  - Assertions: 1
- `h-92w9e1` [alive] 收集箱视图用「在收集箱文件夹内 且 非主页 且 无已归档标签」过滤，就能做到往里丢东西时不必写任何 frontmatter；归档只加一个标签、不移动文件，碎片随即自动退出视图
  - Refuted if: not 组多条件的实际语义不是「以下任一成立即不显示」，导致主页自身或已归档碎片仍出现在待消化列表里
  - scope: {"conditions":{"既有笔记":"不动","库":"school","导航层":"保持不变","触发方式":"会话触发","插件":"核心 Bases"},"ranges":{}}
  - uses (framing declarations): []
  - Assertions: 1
