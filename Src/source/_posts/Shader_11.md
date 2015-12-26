title: 瞎聊 Unity Shader 系列之十一：深度缓存
date: 2015-06-09 15:17
category: Shader
tags: Shader
---

第二节 {% post_link Shader_2 [渲染管线] %} 中提到了 Frame Buffer, 这个是用来存储帧位图的数据存储区域。 这里在介绍另外一个缓存, 叫深度缓存 (Depth Buffer), 也叫作 Z-Buffer。从名字上来看这是一个
存储深度（数据）的存储区。下面我们带着两个问题来解释这个深度缓存。

> 1. 存储的深度数据是什么
> 2. 有什么用处


### 深度是什么

第四节 {% post_link shader_4 [坐标系] %} 中提到，要描述一个物体的位置，需要借助参照物。我们这里扩展一下， 要 **用数值来表述一个物体的某种属性，要有这个数值参照的原点**。 既然深度值是数值，那它的
参照原点是什么呢？ 答案是观察者的视角，换句话说就是 Camera。

在 {% post_link Shader_2 [渲染管线] %} 这节中提到， Vertex Shader 之后有一个插值过程，生成像素。这个像素的 X 和 Y 坐标为屏幕坐标， Z 坐标轴数值就是深度，存储在深度缓存里面。  

### 有什么用处

首先让我们来思考一个问题

> 假设有两个物体都经过渲染后的像素在屏幕坐标系中是同一个点，那哪个像素应该渲染？

我想现在你应该会想到，当然是渲染里观察者更近的一个像素啦。这个一般来说是对的，但是也不全对。 因为远近是用深度数值来表示，但是渲染的逻辑在 Shaderlab 里面可以用 ZTest 设置，它的语法是

{% codeblock %}
ZTest Less | Greater | LEqual | GEqual | Equal | NotEqual | Always
{% endcodeblock %}	

ZTest 默认的值是 LEqual, 也就是渲染在物体在这个深度值同位置或者之前的物体，不渲染之后的物体。

你也许会想，那如果连个像素的深度值一样怎么办？ 深度值一样的情况也叫做 **深度冲突** (Z-fighting)。解决方法是给其中某一个物体设置偏移量。 Shaderlab 中语法是:

{% codeblock %}
Offset Factor, Units
{% endcodeblock%}

Offset 根据一个插值公式来计算出新的深度值。有兴趣的可以 [参考这里](https://msdn.microsoft.com/en-us/library/windows/desktop/dd373973%28v=vs.85%29.aspx)

我们也可以打开和关闭深度写入功能，在 Shaderlab 中用 ZWrite 来控制，它的语法是:

{% codeblock %}
ZWrite On | Off
{% endcodeblock %}

### 在 Unity 图像渲染中顺序中的位置

![PipelineCullDepth](/images/Shader/11/PipelineCullDepth.png)

图片来自 Unity 官方手册 <http://docs.unity3d.com/Manual/SL-CullAndDepth.html>

<hr>
鄙人才疏学浅，有出入的地方非常感谢能帮忙指正。:)