Title: 瞎聊 Unity Shader 系列之三：Shader 土地上的语言们
Date: 2015-04-29 14:33
Modified: 2015-05-04 14:33
Category: Shader
Tags: Shader
Status: published
Keywords: Unity, Shaderlab, Shader, Unity Shader

这节是关于 Unity 平台上 shader 语言的选择。

计算机行业的各公司（或者组织）似乎都遵循着某种规则。当他们在某个领域划出了一亩三分地，当上了地主后, 就要用方法圈住干活的农民。让他们觉得在我这里不会饿死，有饭吃，你要到别家
干活的话，需要重头再来，这是一个很亏本的买卖。这个方法就是制定自己体系（软硬件中的各种协议，接口，语言，框架），脱离这套体系，在别的地方玩不起来。开个玩笑来取名这个规矩叫做**圈地规则**吧。

### Shader 语言们

根据上面提到的圈地规则，下面来隆重的介绍下 shader 这块地上地主们建立起来的体系：CG, HLSL 和 GLSL 语言

- **CG：** C for Graphics 的简称，是 NVIDIA 公司开发的语言。从名字上来看的出它是 C 语言的亲戚，现实是它保留了 C 语言的大部分语义。
- **HLSL：** High Level Shader Language 的简称，由微软开发的语言。语法跟 CG 非常的相似。
- **GLSL：** OpenGL Shading Language 的简称，OPENGL 组件开发的，语法也是基于 C 语言的。

那么问题来了，Shader 语言到底哪家强？这个也发生过强烈的讨论。

其实这个问题好回答，既然跟着 Unity 地主干，听 Unity 地主的话就好了。那么另外一个问题又来了，Unity 地主的观点又是什么？

###Unity 体系规则 Shaderlab

根据圈地规则，Unity 地主也有自己的体系，那就是 Shaderlab。那 shaderlab 又是什么呢？ 这是一个能包容 CG, HLSL 和 GLSL，并且有自己语法体系的东西。

- 能包容 CG, HLSL, 和 GLSL 意思是说在它里面能使用这三种语言。Shaderlab 中用特定的语法块来指定他们：
    - GG 和 HLSL 包括在 `CGPROGRAM ... ENDCG` 语法块内
    - GLSL 包括在 `GLSLPROGRAM ... ENDGLSL` 语法块内
- 有自己的语法系统是指它有自己独特的语法，并且独立于上面三种语言（这句似乎是废话。。。）

Unity 官方比较提倡 CG 或 HLSL 语言。所以我们首选这两个中的其中一个了。之前提到，其实这两语法非常相似，所以其实学好了其中一门就差不多等于学了两门语言。（好像很划算的样子！）

###在 Shaderlab 中写 Shader 的三种方式

Unity 手册 Shader 参考章节[开篇](http://docs.unity3d.com/Manual/SL-Reference.html)就写道 :

> Shaders in Unity can be written in one of three different ways:
>
> as [**surface shaders**](http://docs.unity3d.com/Manual/SL-SurfaceShaders.html),  
> as [**vertex and fragment shaders**](http://docs.unity3d.com/Manual/SL-ShaderPrograms.html) or  
> as fixed function shaders.
>

也就是说有三种 shader 的变体。

####Fixed function shaders

这种 shader 一般用于不支持可编程 shader 模型的老设备上面， 比如 iPhone3。Unity 用 shaderlab 的语法来配置。

####vertex and fragment shaders

参考名字，这个主要是玩转 vertex 和 fragment shader 的。参考[渲染管线]({filename}/Shader_2.md)章节可以知道这两个 shader 处于什么位置。

####surface shaders

Unity 提倡如果想写跟光线交互的 shader 使用这种方式写。那 surface shader 又是什么。 [Unity 手册里面有段话道出了真相：](http://docs.unity3d.com/Manual/SL-SurfaceShaders.html)

> Surface Shader compiler then figures out what inputs are needed, what outputs are filled and so on, ** and generates actual vertex&pixel shaders,**
> as well as rendering passes to handle forward and deferred rendering.

原来 surface shader 最终会被编译成 vertex&fragment shader，这只是换了个汤。当然汤里家里点佐料就是 Unity 帮你处理光线而不用自己写算法。

###总结
Unity Shaderlab 是基于shader语言上建立了自己的一套语法规则，我们不仅要学习 shaderlab 语法，也要学习 shader 语言。Unity 官方提倡使用 CG 或 HLSL 语言。

###参考
- [Unity Manual](http://docs.unity3d.com/Manual/ShadersOverview.html)
- [GPU 编程与CG 语言之阳春白雪下里巴人](http://pan.baidu.com/s/1rsaho)（点击链接即可下载），推荐此书。

###系列文章目录
- [瞎聊 Unity Shader 系列之一：GPU 与 Shader Model]({filename}/Shader_1.md)
- [瞎聊 Unity Shader 系列之二：渲染管线]({filename}/Shader_2.md)
- [瞎聊 Unity Shader 系列之三：Shader 土地上的语言们]({filename}/Shader_3.md)
- [瞎聊 Unity Shader 系列之四：坐标系]({filename}/Shader_4.md)
- [瞎聊 Unity Shader 系列之五：RGBA 101]({filename}/Shader_5.md)
- [瞎聊 Unity Shader 系列之六：初识 Shaderlab]({filename}/Shader_6.md)
- [瞎聊 Unity Shader 系列之七：究竟谁先被渲染？]({filename}/Shader_7.md)
- [瞎聊 Unity Shader 系列之八：#pragma 指令]({filename}/Shader_8.md)
- [瞎聊 Unity Shader 系列之九：用来包装变量的 Properties]({filename}/Shader_9.md)
- [瞎聊 Unity Shader 系列之十：数据的标签：语义绑定]({filename}/Shader_10.md)
