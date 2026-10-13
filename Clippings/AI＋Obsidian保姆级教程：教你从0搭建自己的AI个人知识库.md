---
title: "AI＋Obsidian保姆级教程：教你从0搭建自己的AI个人知识库"
source: "https://zhuanlan.zhihu.com/p/2060861787680012127"
author:
  - "[[直男山禾]]"
published:
created: 2026-10-13
description: "但每次打开AI，真正能被它利用的仍然只有当前聊天框里的几句话。 所以你会反复遇到几个问题： 让AI写东西，每次都要重新介绍自己的行业、读者和表达习惯；想找以前看过的资料，却记不起存在哪个文件里； 这篇文章…"
tags:
  - "clippings"
---
1 人赞同了该文章

![](https://pic3.zhimg.com/v2-8261ece7bd8c14a81a4da20542503602_1440w.jpg)

但每次打开AI，真正能被它利用的仍然只有当前聊天框里的几句话。

所以你会反复遇到几个问题：

让AI写东西，每次都要重新介绍自己的行业、读者和表达习惯；想找以前看过的资料，却记不起存在哪个文件里；

这篇文章要解决的，就是如 **何让你过去积累的资料真正被AI用起来。**

看完以后，你会知道怎样让AI在开始工作之前，就知道了你的参考资料和使用要求。

让AI不再只是回答你眼前的问题，而是能够接着你过去的积累继续工作。

---

这篇用到的软件是 [obsidian](https://zhida.zhihu.com/search?content_id=279116877&content_type=Article&match_order=1&q=obsidian&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3OTIwMzI1MjgsInEiOiJvYnNpZGlhbiIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3OTExNjg3NywiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.NnubLpQQp7McIKm0zDe-tKIvoiSKpqd_SkgVps8Fw58&zhida_source=entity) ，它能把你的所有笔记存成电脑上的纯文本文件，而纯文本恰好是 AI 最擅长的东西。

并且任何模型都能直接读、直接改 **你的笔记库，这就是 AI 的记忆库。**

Notion、印象笔记这些封闭格式的软件，AI 是钻不进去的，它只能帮你存个东西；

而 [Obsidian](https://zhida.zhihu.com/search?content_id=279116877&content_type=Article&match_order=1&q=Obsidian&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3OTIwMzI1MjgsInEiOiJPYnNpZGlhbiIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3OTExNjg3NywiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.4hxwRsrd9rjr2wANV2dY7OXyozC70ONgEw9Knf4A9Gs&zhida_source=entity) 的文件夹就存在本地，天生就是为 AI 而适配的。

等到接好以后，你说“帮我写篇文章”，它自动知道你的行业、你的读者、你讨厌的腔调；

你问“我上个月对那个项目是怎么判断的”，它会翻出你自己的原话；你走在路上说的每句碎碎念，晚上都被它整理成能用的素材。

**笔记越多，这个系统越聪明，而且所有数据都在你自己的电脑上，谁也拿不走。**

接下来，我们不学理论，用10分钟，来让AI搭建你的第一个文件夹。

## 第一步：创建一个仓库

现在，请你在电脑里随便找三份资料。

可以是一篇以前写过的文章、一份会议纪要和一份项目方案；也可以是三篇课程笔记、几份行业报告，或者最近收集的产品资料。

内容不重要，只要它们是你以后可能还会用到的东西，你就可以把它们收集起来。

接下来，我们完成四件事：下载Obsidian、把仓库放进 [iCloud](https://zhida.zhihu.com/search?content_id=279116877&content_type=Article&match_order=1&q=iCloud&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3OTIwMzI1MjgsInEiOiJpQ2xvdWQiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzkxMTY4NzcsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.rpaDBsalahtWoEJ25bL5NHKXwSF0hq2QTsk9KXVxV_E&zhida_source=entity) 、认识一下页面，再让AI读取这个文件夹。

整个过程不需要安装Obsidian里的AI插件，可以直接用 [Claude](https://zhida.zhihu.com/search?content_id=279116877&content_type=Article&match_order=1&q=Claude&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3OTIwMzI1MjgsInEiOiJDbGF1ZGUiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzkxMTY4NzcsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.RwDT6T_tFTJJ_TVvgA5QjubC0fYO5ATxpOy_jlRzeCQ&zhida_source=entity) code或者 [codex](https://zhida.zhihu.com/search?content_id=279116877&content_type=Article&match_order=1&q=codex&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3OTIwMzI1MjgsInEiOiJjb2RleCIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3OTExNjg3NywiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.pf9jylOacrxEF3vL_CfgUZ3NXyaIvDPydwHUf7R-Fwc&zhida_source=entity) ，因为AI要读取的并不是Obsidian这个软件，而是它背后的本地文件夹。

在刚开始学习时，尽量减少前期的安装动作，才能更快适应新方式。

## 下载Obsidian

如果你同时使用iPhone和Mac，我更建议 **先在iPhone上创建仓库。 这样仓库会直接进到icloud里面，后面在电脑上打开时更省事。**

第一次进入软件，会让我们进行设置，可以先创建一个新的仓库，取名后，将仓库放在icloud中。

Obsidian个人使用免费，官方同步服务需要单独订阅，我个人习惯把obsidian放icloud，能在所有设备中同步，也不需要额外订阅。

Obsidian把资料库叫作Vault，听起来很复杂，其实它就是电脑上的一个普通文件夹。

里面的笔记主要以 [Markdown](https://zhida.zhihu.com/search?content_id=279116877&content_type=Article&match_order=1&q=Markdown&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3OTIwMzI1MjgsInEiOiJNYXJrZG93biIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3OTExNjg3NywiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.yvzmmQkFifvFe8Qje6X3TucQSInUExf_jw5NkT1PnpM&zhida_source=entity) 文本保存，所以不仅Obsidian能打开，Claude Code、 [Codex](https://zhida.zhihu.com/search?content_id=279116877&content_type=Article&match_order=1&q=Codex&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3OTIwMzI1MjgsInEiOiJDb2RleCIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3OTExNjg3NywiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.Sq-WZbGj9XS66ZovI9_tQ4xJFY5uAV0gPtNpoFPd33g&zhida_source=entity) 、VS Code和其他支持本地文件的工具都能读取。

创建后，打开icloud，就看到了刚才取名的文件夹，现在里面只有欢迎.md，稍后我们慢慢填充内容。

仓库放进iCloud以后，还有一个非常关键的设置。

右键点击刚才创建的仓库选择“保留下载”，开启后，文件夹旁边会出现对应的保留下载状态图标。

![](https://pic2.zhimg.com/v2-4dd719692505e5c0544aff687dad3acb_1440w.jpg)

打开这个设置后，即使Mac需要节省空间，也不要自动移除这批文件的本地副本。

如果省掉这一步，那iCloud可能把一段时间没有使用的文件只保存在云端，需要时才重新下载。

我们用Obsidian打开笔记时，等几秒也许问题不大；但AI直接扫描文件夹时，云端占位文件可能还没来得及下载，可能会出现读取不到、内容不全或反复等待的情况。

另外还要提醒一句：同步不等于备份。误删和错误修改也可能同步到所有设备，特别重要的资料还是要多备份一下。

## 认识Obsidian

创建仓库后，我们再进入Obsidian，初看页面有些简陋，左边右边都是图标，不知道该点哪里。

第一次使用，只需要只需要认识三个区域。

左边是文件区。这里显示仓库中的文件夹和笔记，和电脑里的文件资源管理器很像，这里是「 **根目录** 」。

以后新建文件夹、移动资料、打开笔记，都可以在这里操作。

![](https://pic4.zhimg.com/v2-a5dfb1a3a3312ef1724e2e8701da26b1_1440w.jpg)

最左侧那条更窄的竖栏是工具栏，里面有搜索、关系图谱等入口，现在暂时不用研究。

中间是编辑区。点击左侧任何一篇笔记，内容都会在这里打开，可以自由编辑，上方可以像浏览器一样开多个标签页，类似WPS的页面。

新手可以使用默认的实时预览模式，直接正常打字，不需要先学习Markdown语法。

右边是辅助区，默认打开文件的关系图谱，以后会显示当前笔记的大纲、属性和 [反向链接](https://zhida.zhihu.com/search?content_id=279116877&content_type=Article&match_order=1&q=%E5%8F%8D%E5%90%91%E9%93%BE%E6%8E%A5&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3OTIwMzI1MjgsInEiOiLlj43lkJHpk77mjqUiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzkxMTY4NzcsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.LJOoImub09Fc_JZd8TeiUA-BOm7ikGNRwo9a-JdzlDo&zhida_source=entity) ，现在它挡视线的话可以先关闭标签页。

![](https://pic2.zhimg.com/v2-544f93a240937f98da5502ead18fceef_1440w.jpg)

在obsidian中，还有一个非常重要的设置，进入“设置→文件与链接”，打开“自动更新内部链接”。

以后移动或重命名笔记时，Obsidian会尽量同步更新其他笔记中的链接。

![](https://pic3.zhimg.com/v2-4b94f004cbc397fed6de86af9a5ae83c_1440w.jpg)

到这里先不要换主题，也不要慌着去社区市场安装十几个插件，现在只需要左侧文件区和中间编辑区。

## 接入AI

OK，obsidian准备好了，现在把AI和obsidian联动起来。

如果你习惯终端，可以直接进入仓库文件夹，打开终端，输入cd，空格后跟文件路径，再打开Claude code，就能用AI来操控仓库文件。

![](https://pica.zhimg.com/v2-bd167d0a392cfde12edb38aceacbf9da_1440w.jpg)

用codex的同学，选择该文件夹作为项目即可。

使用 [Codex CLI](https://zhida.zhihu.com/search?content_id=279116877&content_type=Article&match_order=1&q=Codex+CLI&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3OTIwMzI1MjgsInEiOiJDb2RleCBDTEkiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzkxMTY4NzcsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.H-3kPpkYJJFt8ePQOotbxi4IxeL_OpY_pdeUF6AAdvA&zhida_source=entity) 时，也是在终端先进入这个目录，再启动Codex。

![](https://pic4.zhimg.com/v2-94491e4ac59ab55a97069ca4c1975c75_1440w.jpg)

这两种方式，核心不是用哪个工具，随便选自己已经在用的一个AI工具就行，这套工作流不依赖具体模型，真正关键的是它能否访问这个本地文件夹。

为了确认AI没有打开错位置，可以先问：

> 请只查看当前文件夹，不要修改内容。告诉我这个文件夹的名称、里面目前有哪些文件，以及你是否能够正常读取它们。

![](https://pic1.zhimg.com/v2-cfc183593ea00b5e78fd0d28ab3bb848_1440w.jpg)

当AI能列出仓库中的文件，接入就完成了。

这里没有安装任何Obsidian AI插件，本质上，我们是在AI中来操控文件，obsidian只是充当了一个资料库的作用。

但如果你对obsidian界面更熟悉，还是需要下载插件来使用AI，在「设置」-「第三方插件」中，关闭安全模式，就可以下载相应插件。

![](https://pic1.zhimg.com/v2-72f554937e0bb58018f8aabba581190a_1440w.jpg)

有 `Terminal` ，能在obsidian中使用终端，有 `Claudian` ，登录后直接在侧边栏中与 Claude Code 对话。

obsidian官方也推出了自己的 `Obsidian CLI` 。

不管用哪种方法，能让AI看到、修改仓库文件，就都可以用。

现在把刚才准备好的三份资料放进仓库。

最简单的方法是直接拖到Obsidian左侧文件区，但它不能识别word和pdf，只能识别md文件。

所以你之前的文件，要么就让AI统一改成MD文件，要么就新建笔记，把文字内容粘贴进去。

![](https://pic1.zhimg.com/v2-11ee954ae06d3ec3b9ef9d86fc085ab2_1440w.jpg)

这时我们再进入obsidian，就能看到仓库里面的文档了。

第一次不要让它修改文件，只让它读取：

> 请查看当前文件夹中的三份资料，分别告诉我每份资料讲了什么、它们之间有什么联系，以及这些内容以后可以帮助我完成哪些任务。暂时不要修改或新建任何文件。

如果你放进去的是会议纪要、项目方案和 [行业报告](https://zhida.zhihu.com/search?content_id=279116877&content_type=Article&match_order=2&q=%E8%A1%8C%E4%B8%9A%E6%8A%A5%E5%91%8A&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3OTIwMzI1MjgsInEiOiLooYzkuJrmiqXlkYoiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzkxMTY4NzcsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MiwiemRfdG9rZW4iOm51bGx9._Hjyi-uatwvLoMa0Hljb6W3-qPdO0BRod8JqLDDRpwA&zhida_source=entity) ，AI可能会发现：行业报告中的数据可以支持项目方案，而 [会议纪要](https://zhida.zhihu.com/search?content_id=279116877&content_type=Article&match_order=3&q=%E4%BC%9A%E8%AE%AE%E7%BA%AA%E8%A6%81&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3OTIwMzI1MjgsInEiOiLkvJrorq7nuqropoEiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzkxMTY4NzcsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MywiemRfdG9rZW4iOm51bGx9.8TTi0B4HrNsof2CYIdHRvt1TrV0LL31mO42t5iMGAl4&zhida_source=entity) 里已经出现了相关执行安排。

我放进去的是三份脚本，AI会分析脚本内容、还可以用来做什么，以及三份文件可以如何联系起来。

到这里，你已经完成AI＋Obsidian最核心的一步： **AI不再只看当前聊天框，而是开始读取你自己的资料。**

现在再看原理就很简单了。

Obsidian负责把资料保存在一个长期可控的文件夹中，AI Agent负责阅读、查找、整理和执行。你的资料不必被锁在某个聊天记录里，换一个支持本地文件的AI，原来的仓库依然能用。

不过，三份资料很好管理。等你每天都往里面放东西，它很快又会变乱。所以下一步不是继续塞资料，而是先给所有新内容留一个固定入口。

## 第二步：给资料分类

刚才我们只放了三份资料，AI当然很容易读懂。

但真正使用几天以后，你的仓库里会同时出现很多不同状态的内容。

假设我们准备写一篇短篇小说，现在手里已经有这些东西：

刷到的一则社会新闻，觉得可以改成故事背景、以前写过但没有完成的小说、收藏的几篇爆款短篇小说、AI根据素材生成的故事大纲，以及最后准备发布的版本。

它们看起来都是“和小说有关的文件”，但实际上完全不是一回事。

新闻、聊天记录和突然冒出的灵感，只是原始素材；

以前写过的小说，可以帮助AI了解你的写法；收藏的爆款内容，是供AI分析结构和节奏的参考样本；

AI生成的大纲和正文，是当前项目里的工作文件；最后确认过的版本，才是真正的成品。

如果这些文件全部堆在左边的仓库根目录里，你自己会越来越难找，AI也很容易混淆。

比如你让AI：

> 根据我以前的写作风格，结合当前素材，写一篇10000字的短篇小说。

如果没有清楚的文件结构，它可能把你收藏的爆款小说当成你的作品，模仿了别人的风格；也可能把AI昨天生成的第一稿当成你已经确认过的成品。

所以，给资料建立文件夹，把不同的文件进行分类，不仅仅只是为了页面整齐好看点，只是想告诉AI：哪些文件只是参考，哪些代表我的风格，哪些可以修改，哪些不能覆盖，哪一份才是最终版本。

### 先从收件箱开始

在文件列表上面的按钮中，能直接创建单个文件或者创建文件夹。

现在先在仓库里创建一个文件夹，取名为「收件箱」。

在Obsidian里，每次点击“新建笔记”，软件都需要决定：这篇新笔记保存到哪个文件夹。

如果你没有设置默认位置，新笔记默认直接出现在仓库根目录，全部堆在左边文件列表中，看起来非常乱。

所谓“默认位置”，就是提前告诉Obsidian：以后我随手新建的笔记，如果没有专门指定位置，就统一先放进「收件箱」里。

设置路径是：设置 → 文件与链接 → 指定的附件文件夹→ 收件箱

![](https://pica.zhimg.com/v2-68326d6e6cd3df809109a4fcf1033c28_1440w.jpg)

设置完成后，无论你当时正在查看哪篇小说、哪个项目，只要点击新建笔记，它都会先进入「收件箱」这个文件夹里。

它相当于整个资料库的临时入口。

比如你走在路上，突然想到一句对话：

> “皇宫里 [倒夜香](https://zhida.zhihu.com/search?content_id=279116877&content_type=Article&match_order=1&q=%E5%80%92%E5%A4%9C%E9%A6%99&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3OTIwMzI1MjgsInEiOiLlgJLlpJzpppkiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzkxMTY4NzcsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.3CYwyRAXo2AZJ2iWeR77gM4j9HvOJsIYkTMtXrBn9zw&zhida_source=entity) 的小太监，发现自家陛下正在变成 [僵尸](https://zhida.zhihu.com/search?content_id=279116877&content_type=Article&match_order=1&q=%E5%83%B5%E5%B0%B8&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3OTIwMzI1MjgsInEiOiLlg7XlsLgiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzkxMTY4NzcsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.RBQ-V1osVuLWu7DOJCK95iqpempVRZDFdHS0bQchZfs&zhida_source=entity) 。”

你暂时不知道它会被写进哪篇小说，也没有必要立刻给它设计标签、人物和剧情。就先新建一篇笔记，写下这句话，放到收件箱就可以了。

又比如你半夜想到一个设定：

> 末世降临，我的异能是每天召唤一个AI。

也先扔进收件箱。

你不用在灵感出现时停下来思考“应该放哪里”，AI以后也只需要检查一个入口，就能知道最近新增了什么，再来分类处理。

但这里要注意，obsidian里的文字笔记通常是`.md` 文件，但你要想在md文件中粘贴图片，那图片并不会存放在当前文件中，这和WPS不一样。

WPS中，图片和文字都会被保存在word中，但obsidian中，你把一张新闻截图粘进笔记，它实际上做了两件事：

1. 把图片作为一个独立文件保存到仓库；
2. 在笔记中插入一条指向这张图片的链接。

如果不设置附件位置，这些图片都会全部堆在仓库的根目录里面，会非常混乱，比如：

```
我的资料库
├── image 1.png
├── image 2.png
├── 截图20260711.png
├── 未命名附件.pdf
├── 项目说明.md
├── 第一稿.md
└── 第二稿.md
```

你很难分辨哪些是正文、哪些只是正文引用的图片，AI扫描仓库时也会看到大量意义不明的附件名称。

所以我们要建一个「附件」文件夹，让所有的图片都直接放里面，那根目录会清楚很多：

设置路径是：设置 → 文件与链接 → 指定的附件文件夹 → 附件

![](https://pic1.zhimg.com/v2-de40f0a5f38bb4972c4ed2e7a1d3a9ce_1440w.jpg)

这里的“附件默认位置”和前面的“新建笔记默认位置”是两回事：

- 新建笔记默认位置：决定新的.md文字笔记先放在哪里；
- 新附件默认位置：决定图片、PDF、音频等文件保存在哪里。

附件单独存放只是为了保持目录清楚，并不影响笔记里的显示。你打开原来的笔记，图片依然会正常出现，因为Obsidian会自动保留它们之间的链接。

### 素材及知识库

接下来，我们再继续创建文件夹，可以是「原始资料」和「知识库」，这两个文件夹很容易混淆。

「原始资料」保存的是你找到的东西，重点是保留原貌和出处，让每一个素材都有据可查。

比如：

```
原始资料
├── 新闻-独居老人连续收到陌生快递.md
├── 访谈-殡葬师讲述特殊订单.md
```

这里可以放新闻、采访、网页文章、视频字幕，也可以放你收藏的爆款作品。

这些资料可以供AI分析，但不能让AI默认把它们当成你的原创内容。

知识库保存的则不是整篇原文，而是你和AI从原始资料中提取出来，并且以后还能继续使用的东西。

例如AI分析了十篇爆款短篇小说后，总结出：

```
知识库
├── 短篇小说的5种高效开头.md
├── 三千字故事如何埋下反转.md
├── 第一人称悬疑的视角限制.md
└── 我的常用人物关系.md
```

这样以后AI需要写反转故事时，不必重新阅读所有爆款小说，可以先调用这篇已经整理过的知识。

总得来说，原始资料保存“我看过什么”，知识库保存“我从中学到了什么”。

如果你还想让AI了解自己的表达风格，还需要把“自己以前写过的内容”和“别人写的爆款样本”分开。

可以建立新的文件夹「我的作品」，只放你自己写过、并且认可的内容。

例如：

```
我的作品
├── 番茄-凌晨三点的末班车.md
├── 七猫-失踪的第七位住户.md
└── 九洲-每天收到明天的快递.md
```

以后你让AI模仿自己的风格时，它就知道应该优先读取哪些文件了。

### AI正在写的内容，必须单独放进项目

现在，我们真的要开始写这篇小说了。

这时再创建个写小说的文件夹「 [AI小说](https://zhida.zhihu.com/search?content_id=279116877&content_type=Article&match_order=1&q=AI%E5%B0%8F%E8%AF%B4&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3OTIwMzI1MjgsInEiOiJBSeWwj-ivtCIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3OTExNjg3NywiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.egKf5gSv4QABCAfvYPRfvPIStf-ZP4w1H4ZIcg8UL7E&zhida_source=entity) 」，这里放的是AI正在处理但还没有最终确认的AI小说。里面同样要划分出来不同的层级，比如：

```
03-项目
└── 明天寄来的快递
  ├── 项目说明.md
  ├── 故事大纲.md
  ├── 第一稿.md
  ├── 第二稿.md
  └── 修改记录.md
```

`项目说明.md` 告诉AI这次到底要写什么，故事大纲`.md` 是让AI按照大纲来书写，看到这篇内容，你就能判断AI能不能写正文。

第一稿、第二稿也都留在项目文件夹里，因为它们只是过程中的草稿，不代表最终成品，最后也可以把过程文件和成文进行比较，让AI不断优化。

### 现在，这套目录才真正有意义

最后得到的结构是：

```
收件箱
临时想法和还没决定用途的内容

原始资料
新闻、网页、访谈、爆款样本等外部材料

知识库
从资料中提炼的方法，以及自己以前确认过的作品

我的作品
方便Ai学习我们的语言风格

AI小说
AI正在生成和修改的内容

附件
图片、PDF、音频等非文字文件
```

它不是一套为了“看起来专业”而设计的分类，而是让AI名字，什么刚刚进入、什么只能参考、什么正在修改、什么已经确认、什么只是附件。

有了这些边界以后，AI才不会把别人的爆款小说当成你的作品，把自己生成的第一稿当成最终版本，或者为了找一张截图扫描整个仓库。

## 第三步：让AI懂你

整理几次以后，你会遇到一个新问题：AI能找到资料，输出却仍然不像你。

比如第一次让AI生成项目汇报，它可能写出一篇结构完整但没有用的“正确废话”：项目总体推进顺利、团队协同良好、后续持续优化。

可你真正需要的是先写结论，再列出已经完成的事项、卡点负责人、截止日期和需要领导决定的问题；所有数据还必须能回到会议或原始材料核对。

对于这种你有明确要求的工作，就要给AI写好工作规则。

这时，在仓库根目录创建规则文件。

别被规则这两个字给迷惑到，所谓规则文件，就是创建一个单独的md文件，这个md文件中，告诉AI你是谁，你需要AI帮你做什么，做事情的要求是怎么样的。

把AI刚才你手底下的实习生去用。

Claude Code主要读取CLAUDE.md，Codex主要读取AGENTS.md，我们创建好md文件后，把文件名改成对应的即可。

到这一步，你说我不会写规则不会介绍啊，没关系，不用对着空白文档硬写，让AI采访你：

> 我正在搭建个人Obsidian资料库。请连续问我10个问题，了解我最常完成的任务、服务对象、表达偏好、判断标准、常见交付格式、不能接受的输出、 [隐私边界](https://zhida.zhihu.com/search?content_id=279116877&content_type=Article&match_order=1&q=%E9%9A%90%E7%A7%81%E8%BE%B9%E7%95%8C&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3OTIwMzI1MjgsInEiOiLpmpDnp4HovrnnlYwiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzkxMTY4NzcsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.UQc_4QtKLkr924BOE3bA4iYqScrHswVI8M9KrE_F_KE&zhida_source=entity) 和文件使用习惯。一次只问一个，并根据上一题继续追问。结束后，把答案整理成一份简洁、具体、可以执行的资料库规则。不要写“保持专业”之类的空话，每条规则都要能用于实际判断。

初次使用，不需要每个文件都做到最好，采访完之后，AI给你写什么内容，你就先用着。

规则文件不是一次写完的。

AI第二次犯同一个错误，就补一条；你发现自己又在重复解释相同偏好，也补进去。它更像一份会持续更新的新员工手册。

但这里注意，不要把个人经历、所有项目背景和几十页写作方法全部塞进根规则。

规则文件越长，每次启动消耗的上下文越多，真正重要的指令反而越容易被忽略。根目录只负责告诉AI“你是谁、这里有什么、应该去哪里找”，具体项目再放具体要求。

## 第四步：让AI按需寻找

刚开始搭建知识库时，只有十几份资料，全读一遍也很快，但等到仓库中有几百篇笔记，再让AI每次“阅读所有内容”，不仅浪费Token，还会非常占上下文。

最好是在规则里，直接告诉AI该去哪里找东西，处理会议时，先读当前项目说明和相关会议记录。需要核实观点时，回到01-原始资料查找来源。

这样，做项目周报时AI会先读取当前项目和本周会议，不会顺便扫描整个仓库；只有需要核对行业数据时，它才回到原始资料。读取范围更小，重点反而更清楚。

每个文件中，同样可以塞进去一份简短的说明.md。

比如原始素材中，说明当前文件夹是做什么用的，有哪些内容。

根规则负责指路，文件夹说明负责局部标准，项目文件负责当前任务，把文件分清楚了，AI了解得会更快。

## 第五步：实时输入

目录搭好以后，真正决定这套系统能不能长期使用的，不是文件夹设计得多漂亮，而是“把东西存进去”够不够轻松。

如果看到一篇好文章，要先复制标题、再复制链接、再打开Obsidian、选择文件夹、粘贴正文；路上想到一句话，还要等回到电脑以后再补记，那这套流程用不了几天就会停下来。

所以我给Obsidian接了两条最常用的输入方式：

电脑上看到的内容，用官方 [Web Clipper](https://zhida.zhihu.com/search?content_id=279116877&content_type=Article&match_order=1&q=Web+Clipper&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3OTIwMzI1MjgsInEiOiJXZWIgQ2xpcHBlciIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3OTExNjg3NywiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.Ny35SeDeioj_fYucpoKDFgSiMo0tYocwkmIdDqmHJOI&zhida_source=entity) 一键保存；外出突然出现的想法，用 [iPhone快捷指令](https://zhida.zhihu.com/search?content_id=279116877&content_type=Article&match_order=1&q=iPhone%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3OTIwMzI1MjgsInEiOiJpUGhvbmXlv6vmjbfmjIfku6QiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzkxMTY4NzcsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.ab7hHA8GAJE0gN4c3adod9s8oJ0PAfFMqABfRuFxXKM&zhida_source=entity) 直接写进当天的日记。

两边最后都会通过iCloud进入同一个仓库，电脑上的AI不需要再次导入，就能直接读取。

## 网页、推文和长视频，用Web Clipper一键进入资料库

第一条路径是Obsidian官方推出的浏览器扩展Web Clipper。

![](https://pic4.zhimg.com/v2-a0c229a29198d494c5bca8ca19db7e91_1440w.jpg)

第一次使用时，在Web Clipper里选择自己的Obsidian仓库，再把默认保存目录设为收件箱。

![](https://pic2.zhimg.com/v2-b951fb7d6ae4fc00aa23e57bb57fc175_1440w.jpg)

以后看到一篇值得保留的网页或推文，点击Web Clipper，它会自动识别页面标题、作者、原始链接和正文内容。

确认后点击“Add to Obsidian”，几秒钟后，内容就会以Markdown笔记出现在对应文件夹中。

它对内容型长视频也很有用。打开视频页面后，在Web Clipper里切换到适合视频或阅读的模板，可以把视频字幕保存进Obsidian。

整理好的笔记中会保留字幕和 [时间戳](https://zhida.zhihu.com/search?content_id=279116877&content_type=Article&match_order=1&q=%E6%97%B6%E9%97%B4%E6%88%B3&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3OTIwMzI1MjgsInEiOiLml7bpl7TmiLMiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzkxMTY4NzcsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.xmUDTaqi3_6-7OZPWx0cJK-3wB75xyxU6IPkk5kDXfg&zhida_source=entity) ，信息非常全。

当然，这种方式是很方便，但这不代表看到什么都要全文收藏。

真正值得剪藏的是以后可能被研究、引用或继续创作的内容。

只觉得“有点意思”的网页，留一个链接就够了。

## 路上冒出的碎碎念，用iPhone直接写进当天的Daily Note

网页解决的是外部信息，但很多真正有价值的内容并不在网上，而是在某个瞬间突然从脑子里冒出来。

比如走在路上时，你突然想到：可以让国内的AI们都打一场比赛，看看谁能猜出世界杯冠军。

我的做法是使用iPhone自带的“快捷指令”，把语音直接追加到Obsidian的书签或者当天的Daily Note中。

这里大家再注意，如果你是先用的mac，后用的iphone，还想让两者用同一个仓库的话，那整个文件夹必须放在icloud云盘的obsidian文件夹中。

**最好大家还是先在iphone上下载obsidian。**

回到电脑，Claude Code或Codex看到的也是这条新记录。

中间不需要给Obsidian安装AI插件，也不需要把内容再发到微信或文件传输助手。

一天可能会出现十几个零散想法，把它们按时间连续写进文档里，晚上再统一整理，比生成十几个“未命名笔记”更容易处理。

快捷指令做好后，打开iPhone的“设置→操作按钮”，把操作按钮指定为刚刚创建的快捷指令。

以后走路、坐车或者临睡前突然想到什么，只要按一下操作按钮，直接说话，松开后内容就会自动进入文档中。

## 第六步：AI自动化

如果你连续好几天，都在对AI说：“帮我整理今天的灵感内容，生成我明天的代办事项”，这段重复流程才值得自动化。

比如我之前，每天都需要AI读取文档中的灵感，先按主题归类，找出哪些是写作灵感，哪些是代办事项，总结出一份清单，但不要覆盖我的原始灵感。

这里最好在规则.md中再写一条规则：

```
碎碎念.md使用规则
带时间戳的内容是我当时未经整理的碎碎念。
可以提取、分类和复制到项目，但不能修改或删除原始记录。
整理时保留日期和时间，方便回到当天的上下文。
```

这样AI就知道：日记里的碎碎念是原始输入，不是已经确认的观点。它可以拿去做二次创作，但不能擅自把原话润色后覆盖掉。

同时，每天维护我们的仓库，也需要AI做一些动作，比如整理收件箱。

需要AI识别新文件、建议处理方式、补充来源信息，然后生成一份等待确认的清单。

一周后，可以让AI读取过去七天新增的记录和项目变化，告诉你：哪些问题反复出现，哪些任务一直没有推进。

接着还有知识库检查，看哪些结论缺少来源，哪些笔记有明显重复的内容。

用codex的同学，直接用自动化功能来进行操作，Claude Code也可以配合系统定时任务或其他自动化工具触发。

## 到这里，你已经真正用上了AI＋Obsidian

OK到这里再回头看，你没有学完Obsidian所有菜单，也没有安装几十个插件，更没有一直调整反向链接。

你只是先把三份资料交给AI，看到它能够跨文件理解；资料变多以后，建立一个统一入口；

输出不像你，就加入个人规则；记录不方便，就接入网页和语音；内容开始混乱，再让AI保留来源、提取知识。

如果只有Obsidian，没有AI，你可能只是拥有一个越来越大的仓库；

如果只有AI，没有自己的资料，它给你的往往是正确但平均的答案；如果把判断也完全交给AI，知识库只会更快地产生看起来整齐的错误。

所以，你今天不用搭建“终极第二大脑”。

只需要完成一个最小闭环：

**放入三份资料，让AI读懂它们，再用其中的内容完成一个真实任务。**

第一份真正能交付的结果做出来之后，你自然会知道下一条规则该写什么、哪个环节值得自动化。

发布于 2026-07-15 23:02・北京[知识库](https://www.zhihu.com/topic/19553061)

赞同 1