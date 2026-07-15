# TikTok Shop 内容电商联动看板

三大品类（玩具/潮玩收藏/文具）全链路分析看板：内容曝光→互动→商品点击→下单转化。

## 一键部署

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/YOUR_USERNAME/tiktok-shop-dashboard)

## 本地运行

```bash
python3 -m http.server 8080
# 打开 http://localhost:8080
```

或直接双击 `index.html`。

## 数据结构

- `index.html` — 看板页面
- `data.js` — 产品、内容、联动数据
- `generate_real_data.py` — 数据生成器（修改后重新生成 `data.js`）

## 技术栈

HTML + CSS + Vanilla JS · ECharts · 纯前端无依赖
