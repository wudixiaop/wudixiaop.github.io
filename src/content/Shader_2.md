Title: 瞎聊 Unity3D Shader 系列之二：渲染管线
Date: 2015-04-27 16:50
Modified: 2015-04-27 15:54
Category: Shader
Tags: Shader
Status: draft

为了更好理解和记忆这节内容，先来学下面几个词。

- **渲染管线(Rendering Pipeline)：** 一提到管线，感觉很高大上的样子。说的俗一点就是可以理解为流水线。渲染管线我们可暂时理解为 **从得到模型数据到绘制出图像** 这一过程的称呼。
- **Vertex Shader：** 对顶点数据编程的一段程序。 人类有懒惰的天性，习惯用简化的词汇来表达同一个东西。对 Vertex Shader 也不例外，一般称其为 VS ，但是在本系列文章中会保持全称。
- **Fragment Shader：** 对像素数据编程的一段程序。这里 fragment 可以理解为带有信息（颜色，坐标等）的像素 (Pixel), 一般也简称其为 FS 或者 PS 。 在本系列文章中会保持其全称。
- **Fixed Function：** 由于一些硬件支持等历史原因，早期的图形 API  **只支持对 GPU 做配置**，这部分只可配置的功能就是 fixed fucntion。
这里注意下，fixed function 的功能只能配置，不像 Vertex Shader　和 fragment Shader 可以编程（写自己的算法）。


###渲染管线 (Rendering Pipeline)

这小节主要讲渲染管线的各个阶段。如下图，我事先抽象出来几个小框，不同的框代表不同的阶段。

![]()





###总结
渲染管道是从得模型数据到图像生成过程的一种描述x。Vertex Shader 能对顶点数据写处理算法，而 Fragment Shader 能对像素数据写处理算法。


###参考：
- [Cg Programming in Unity](http://en.wikibooks.org/wiki/Cg_Programming/Programmable_Graphics_Pipeline)


###系列文章目录
- [瞎聊 Unity3D Shader 系列之一：GPU 与 Shader Model]({filename}/Shader_1.md)
- [瞎聊 Unity3D Shader 系列之二：渲染管线]({filename}/Shader_2.md)
