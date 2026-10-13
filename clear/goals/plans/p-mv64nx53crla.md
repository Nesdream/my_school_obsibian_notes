# 阶段归档 · p-mv64nx53crla

- 收束时间:2026-10-13T04:18:51.571Z
- 所属目标:g-mv62a6fjugxy
- 收束之辞:这一阶段（t3）把判据 6 的新口径落到了实物上，并按 L3 做了一次独立核验。产出与结果：① 重跑 `clear/models/base_filter_check.py`，当次读数 字面 122 条 / 未解析 19（`code` 11、`template_placeholder` 6、`input_content` 2，三类合计＝19）、渲染口径 104 / 8、`dangling` = 0，原始数据在 `clear/models/base_filter_check.out.json`；② 报告新增 §八 写明新口径与逐条登记，并顺带补上末尾的外链作者名核实附录；③ 「零摩擦入箱」经独立核验判为**支持**（那份剪藏搬进 `收集箱/` 后 frontmatter 一字未改，仍恰好命中「待消化」1 篇）。评估者留下 4 条记账类异常，已逐条解释并据此改正报告与脚本：u1 把 §五 与 §八 两套数字的差额算清（未解析 18→19 完全对上；字面 123→122 中有 3 条已解析链接因交付时刻的 AGENTS.md 副本未保留而无法指认，已如实写明并改为「快照要连脚本版本与被扫文件清单一起存档」）；u2 把 §一/§二 的过期大小与计数改成当次实测（1856 B / 12566 B / 209 行 / 49 个）；u3 按 asar 字节偏移 2938182 的**调用点**把 `file.hasTag` 的方向改回「文件标签以查询标签为前缀」，并记下这次读反的教训；u4 改正了 `[[九章智算云]]` 的例外理由（它是剪藏 frontmatter 的 author 字段、属输入内容，且文件已移入 `收集箱/`）。

## 步骤
- [advanced] 1. 重跑 clear/models/base_filter_check.py，把当次数字（generated_at、字面/渲染两口径的链接总数与未解析数、by_bucket 三桶计数、dangling）与逐条明细写进报告里判据 6 那一节，改成新口径的表述；同时记录当次扫描里「收集箱数据库.base」的「待消化」视图命中项（应当是那份未改 frontmatter 的剪藏） → clear/reports/知识库重构-校验记录.md, clear/models/base_filter_check.out.json
