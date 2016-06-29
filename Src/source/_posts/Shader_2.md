title: 瞎聊 Unity Shader 系列之二：渲染管线
date: 2015-04-28 11:07
category: Shader
tags: Shader
---

这节描述的是图形渲染的大致过程。

为了更好理解和记忆这节内容，先来学下面几个词。

- **渲染管线(Rendering Pipeline)：** 一提到管线，感觉很高大上的样子。说的俗一点就是可以理解为流水线。渲染管线我们可暂时理解为 **从得到模型数据到绘制出图像** 这一过程的称呼。
- **Vertex Shader：** 对顶点数据编程的一段程序。 人类有懒惰的天性，习惯用简化的词汇来表达同一个东西。对 Vertex Shader 也不例外，一般称其为 VS ，但是在本系列文章中会保持全称。
- **Fragment Shader：** 对像素数据编程的一段程序。这里 fragment 可以理解为带有信息（颜色，坐标等）的像素 (Pixel), 一般也简称其为 FS 或者 PS 。 在本系列文章中会保持其全称。
- **FrameBuffer：** 缓存帧数据的存储区，它一般包含的是要显示到显示设备上的位图数据（也就是图片数据）。
- **Fixed Function：** 由于一些硬件支持等历史原因，早期的图形 API  **只支持对 GPU 做配置**，这部分只可配置的功能就是 fixed fucntion。这里注意下，fixed function 的功能只能配置，不像 Vertex Shader　和 fragment Shader 可以编程（写自己的算法）。


### 渲染管线 (Rendering Pipeline)

看图说话

![2.renderingpipeline.jpg](/images/Shader/2/rendering-pipeline.jpg)

上面是可编程的渲染管线模型的示意。下面多说几点：

 - 输入阶段。Unity 使用 Mesh Renderer 等组件读取模型顶点数据，然后调用图形 API，将数据传递给 GPU。
 - 现实中同时会进行多条渲染管线，他们是**并行的**。 这点概念比较重要，以后还会提到它。我们记住 GPU 并行能力很强。
 - 最后输出的 FrameBuffer (可以理解为渲染出来的图片) 有几率被抛弃掉，也就是说不显示在显示设备上。这个以后单独说明原因。好比残酷的现实世界，努力了（整个渲染过程）也不一定会成功（被显示出来）。

<!--more-->

### 总结
渲染管道是从得模型数据到图像生成过程的一种描述。Vertex Shader 能对顶点数据写处理算法，而 Fragment Shader 能对像素数据写处理算法。


### 参考：
- [Cg Programming in Unity](http://en.wikibooks.org/wiki/Cg_Programming/Programmable_Graphics_Pipeline)
- [Fixed-function](http://en.wikipedia.org/wiki/Fixed-function)

<hr>
鄙人才疏学浅，有出入的地方非常感谢能帮忙指正。:)