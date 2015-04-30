Title: 瞎聊 Unity3D Shader 系列之三：Shader 土地上的语言们
Date: 2015-04-29 14:33
Modified: 2015-04-29 14:33
Category: Shader
Tags: Shader
Status: published

这节是关于 Unity3D 平台上 shader 语言的选择。

计算机行业的各公司（或者组织）似乎都遵循着某种规则。当他们在某个领域划出了一亩三分地，当上了地主后, 就要用方法圈住干活的农民。让他们觉得在我这里不会饿死，有饭吃，你要到别家
干活的话，需要重头再来，这是一个很亏本的买卖。这个方法就是制定自己体系（软硬件中的各种协议，接口，语言，框架），脱离这套体系，在别的地方玩不起来。开个玩笑来取名这个规矩叫做**圈地规则**吧。

### Shader 语言们

根据上面提到的圈地规则，下面来隆重的介绍下 shader 这块地上地主们建立起来的体系：CG, HLSL 和 GLSL 语言

- **CG：** C for Graphics 的简称，是 NVIDIA 公司开发的语言。从名字上来看的出它是 C 语言的亲戚，现实是它保留了 C 语言的大部分语义。
- **HLSL：** High Level Shader Language 的简称，由微软开发的语言。语法跟 CG 非常的相似。
- **GLSL：** OpenGL Shading Language 的简称，OPENGL 组件开发的，语法也是基于 C 语言的。

那么问题来了，Shader 语言到底哪家强？这个也发生过强烈的讨论。

其实这个问题好回答，既然跟着 Unity3D 地主干，听 Unity3D 地主的话就好了。那么另外一个问题又来了，Unity3D 地主的观点又是什么？

###Unity3D 体系规则 Shaderlab

根据圈地规则，Unity3D 地主也有自己的体系，那就是 Shaderlab。那 shaderlab 又是什么呢？ 这是一个能包容 CG, HLSL 和 GLSL，并且有自己语法体系的东西。

- 能包容 CG, HLSL, 和 GLSL 意思是说在它里面能使用这三种语言。Shaderlab 中用特定的语法块来指定他们：
    - GG 和 HLSL 包括在 `CGPROGRAM ... ENDCG` 语法块内
    - GLSL 包括在 `GLSLPROGRAM ... ENDGLSL` 语法块内
- 有自己的语法系统是指它有自己独特的语法，并且独立于上面三种语言（这句似乎是废话。。。）

Unity3D 官方比较提倡 CG 或 HLSL 语言。所以我们首选这两个中的其中一个了。之前提到，其实这两语法非常相似，所以其实学好了其中一门就差不多等于学了两门语言。（好像很划算的样子！）

###总结
Unity3D Shaderlab 是基于shader语言上建立了自己的一套语法规则，我们不仅要学习 shaderlab 语法，也要学习 shader 语言。Unity3D 官方提倡使用 CG 或 HLSL 语言。

###参考
- [Unity3d Manual](http://docs.unity3d.com/Manual/ShadersOverview.html)
- [GPU 编程与CG 语言之阳春白雪下里巴人](http://pan.baidu.com/s/1rsaho)（点击链接即可下载），推荐此书。

###系列文章目录
- [瞎聊 Unity3D Shader 系列之一：GPU 与 Shader Model]({filename}/Shader_1.md)
- [瞎聊 Unity3D Shader 系列之二：渲染管线]({filename}/Shader_2.md)
- [瞎聊 Unity3D Shader 系列之三：Shader 土地上的语言们]({filename}/Shader_3.md)
- [瞎聊 Unity3D Shader 系列之四：坐标系]({filename}/Shader_4.md)
