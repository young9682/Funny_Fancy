# Pelican Riding a Bicycle 🚲🐦

一只悠哉骑行的鹈鹕 —— 纯 SVG + CSS 动画实现，**零 JavaScript**。

## 运行

直接用浏览器打开 `Pelican Riding a Bicycle.html` 即可，无需安装依赖、无需构建。

```bash
# 也可以起一个本地静态服务
python -m http.server 8000
# 然后访问 http://localhost:8000/Pelican%20Riding%20a%20Bicycle.html
```

## 动画细节

- 双轮与曲柄匀速旋转，脚踏动作与车轮联动
- 鹈鹕身体随节奏上下起伏，翅膀扇动、头部轻摆
- 云朵缓慢漂移，地面线条滚动，营造向前骑行的错觉
- 地面阴影随颠簸呼吸式缩放

所有动效均由 CSS `@keyframes` 驱动，场景本身是一份可缩放、无位图的矢量 SVG。

## 文件结构

```
Pelican Riding a Bicycle/
├── Pelican Riding a Bicycle.html   # 全部内容:HTML + CSS + SVG
└── README.md
```

## 致谢

本片由 **SSPU AILAB | 超级棒棒糖（bbt）** 独家赞助播出。

独家自部署 **int8 deepseek-v4-flash**。
