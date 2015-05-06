Title: 瞎聊 Unity3D Shader 系列之一：GPU 与 Shader Model
Date: 2015-04-26 16:50
Modified: 2015-04-27 15:54
Category: Shader
Tags: Shader
Status: published

我想首先唠叨下我为什么打算写这一系列的文章及文章的定位。

我写的动力主要来源于如下原因：

- 对之前学习的一些总结、复习和提炼
- 尽可能的填充一些概念上的空白。 有不少关于 Unity3D shader 的文章只讲 Shaderlab 语法，讲各种光照模型等, 这对于缺乏概念的新手来说是不太好理解的。
- 之前信誓旦旦的跟朋友说以后学了 shader 会写点文章出来，算是允诺。。。

文章定位：

- 这是学习笔记，不是教程。如果内容会有出入，非常感谢和希望您能指正。
- 主要基础概念为主，可能很零散。

之前有前辈说过，学习一门知识前，了解其由来对入门很有好处。我比较赞同这个观点，所以开篇我们来说写历史。

###CPU 之外的另外一个 PU - GPU

随着计算机处理图形的计算量越来越来大，CPU难以满足计算速度上的需求, 为了将图形的计算单独拿出来执行，上世纪70年代开始出现了为加速图形绘制的硬件。
这些硬件跟大部分刚出来的新事物一样，功能有限，而且不太完善，当然那个时候也不叫 GPU。

1999 年，NVIDIA 公司发布了 GeForce256, 并且提出一个 Graphics Process Unit (GPU) 概念。很多文章都提到这款显卡有划时代的意义，因为它使第一款
带有可编程顶点处理能力的显卡，这意味着显卡从**之前的只可配置**上升到了**可编程**的高度，开发者从此可以实现自己顶点处理算法。NVIDIA 也是提出 GPU 这个词
来对 GeForece256 与之前显卡做区分。

2000 年以后， GPU 技术一直在不断的发展，处理和运算能力不断打变强变大。为了利用 GPU 强大的并行计算能力，出现了 CUDA 并行计算平台。有兴趣的同学可以关注下
[CUDA官网](https://developer.nvidia.com/cuda-zone).


###Shader Model

首先我们要提下当今跟 GPU 打交道的形API：[Microsoft DirectX](http://en.wikipedia.org/wiki/DirectX)、 [OPENGL](https://www.opengl.org) 和
 转为嵌入式设备设计的[OPENGL GS](https://www.khronos.org/opengles/)。Directx 是微软提供的图形 API, OPENGL 和 OPENGL ES 现在是由 [Khronos Group](http://baike.baidu.com/link?url=vW0PfmVKQC00WWRibyVSrnjRYVdVj1lk9HG6B4w9uc9lnlnWnYoDJd1puZu1CNf2_vacBBTFFbdMzZWCNkliSK) 团队维护开发的图形API。

这些图形 API 都提供对 GPU 编程的能力，这能力就是我们说的 Shader。图形 API 的更新会提供不同的 shader 的能力 (当然是越来越强大)。
微软提出了一个词叫 Shader Model, 并用不同的版本号来区分 Shader 的能力。通常我们也会称 Shader Model 为 SM。

下面列出到现在为止 Shader Model 的各个版本与 DirectX 版本的对应关系：

- Shader Model 1.0（DirectX8.0）
- Shader Model 2.0（DirectX9.0b）
- Shader Model 3.0（DirectX9.0c）
- Shader Model 4.0（DirectX10）
- Shader Model 4.1（DirectX10.1）
- Shader Model 5.0（DirectX11）

我们先不关注各个版本区别，只要知道版本号越高，提供的功能越来越强大。


###总结  
GPU 为大量图形计算而生，而 Shader 是对 GPU 编程的技术。微软用 Shader Model 的不同版本号来区分不同 Shader 的能力。


###参考  

- [Wikipidia: Graphics processing unit ](http://en.wikipedia.org/wiki/Graphics_processing_unit)
- [_Real-Time Rendering, Third Edition_](http://www.amazon.com/gp/product/1568814240?tag=realtimerenderin&pldnSite=1)
- [Shader Model](http://baike.baidu.com/link?url=DDy0sTi56RE9TiVdj5MOCqwmV7ATJEkBHQp7V8eRzA_lyq1HPOLgmBULeSo-Khw2-mb7Wst75LJF3_I3SjZAZa)


###系列文章目录
- [瞎聊 Unity3D Shader 系列之一：GPU 与 Shader Model]({filename}/Shader_1.md)
- [瞎聊 Unity3D Shader 系列之二：渲染管线]({filename}/Shader_2.md)
- [瞎聊 Unity3D Shader 系列之三：Shader 土地上的语言们]({filename}/Shader_3.md)
- [瞎聊 Unity3D Shader 系列之四：坐标系]({filename}/Shader_4.md)
- [瞎聊 Unity3D Shader 系列之五：RGBA 101]({filename}/Shader_5.md)
- [瞎聊 Unity3D Shader 系列之六：初识 Shaderlab]({filename}/Shader_6.md)
- [瞎聊 Unity3D Shader 系列之七：究竟谁先被渲染？]({filename}/Shader_7.md)
