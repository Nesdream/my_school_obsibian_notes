# mermaid 渲染检查（可重跑）

`index.html` 会把 `知识库工作流.md` 里的两段 ```mermaid 图源抽出来，交给 mermaid 渲染；
成功时页面高度 = 640 + 两张图实际渲染高度之和，所以**看截图高度就知道渲染成没成**（不必用眼睛判断）。

重跑三步：

```bash
# 1. 取一份本地 mermaid 构建（本机 omniroute 自带，无需联网）
cp /home/linuxbrew/.linuxbrew/lib/node_modules/omniroute/node_modules/mermaid/dist/mermaid.min.js clear/models/mmcheck/
# 2. 用无头 Chrome 截图（DSH 的 vision_html_screenshot，source 指上面这个 index.html，fullPage=true）
# 3. 比对返回的 pageHeight：明显大于 600 即为渲染成功
```

`mermaid.min.js` 有 3.5 MB，是第三方构建、且本库会开源，**用完就删，不进版本**。
