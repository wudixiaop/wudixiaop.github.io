title: 瞎聊 Unity Shader 系列之八：#pragma 指令
date: 2015-05-07 16:13
category: Shader
tags: Shader
---

第三节 {% post_link Shader_3 [Shader 土地上的语言们] %} 里面说到过 CG 和 HLSL 等语言被 `GGPROGRAM ... ENDCG` 语句块里面。这节的主角 #pragma 出现的位置就是在这个语句块里面，用来做编译指示的。就好比告诉
 Shaderlab 的编译器，你应该这么干应该那么干。这里把 #pragma 叫做编译指令吧。

`CGPROGRAM ... ENDCG` 语句块根据 Shaderlab 写作方式不同，它的位置也不同。

- 如果是 **surface shader**, 它在 Subshader 语句块里面，不是在 Pass 语句块里面
- 如果是 **vertex&&framgment shader**，它是 Pass 语句块里面

其实 surface shader 最终会编译成 vertex&&framgment shader, 最终结果是一样的的。surface shader 会被编译成含多个 Pass 的 vertex&&fragment shader, 而这些都用相同的编译指令。我们可以从 Inspector 的 shader
属性信息里面去打开被编译为 vertex&&fragment shader 后的代码。

![surface shader](/images/Shader/8/surfaceshader.png)

如果本身不是 surface shader 的话，上面那个 show generated code 按钮是不会出现的。上面提到 #pragma 是在 `CGPROGRAM ... ENDCG` 语句块里面的，所以它出现的位置也符合上面提到的特征。

### Surface Shader 的编译指令

这类 shader 必须指明

- surfaceFuction 是什么
- 关照模型是什么

语法是

>   #pragma surface surfaceFunction lightModel [optionalparams]


从上面语法能知道，它有一些可以选的参数。具体参考 [这个页面](http://docs.unity3d.com/Manual/SL-SurfaceShaders.html)

伪代码大概是这样：

{% codeblock %}
Shader "shader 的名字" {

    Subshader {
        // CGPROGRAM ... ENDCG 在 Subshader 里面
        CGPROGRAM

        // surfaceFunction 是 surf,
        // 光照模型是 Standard
        // [...] 表示可选参数
        #pragma surface surf Standard [...]


        // surfaceFunction
        void surf () {

        }

        ENCG
    }
}
{% endcodeblock %}

### Vertex&&Fragment Shader 的编译指令

这里的指令集分三类:

- CG/HLSL 程序相关
- 面向的 {% post_link Shader_1 [Shader Model]%}
- 渲染的平台

具体参考 [这个页面](http://docs.unity3d.com/Manual/SL-ShaderPrograms.html)

伪代码大概是这样：

{% codeblock %}
Shader "shader 的名字" {

    Subshader {

        pass {
            // CGPROGRAM ... ENDCG 在 Pass 里面
            CGPROGRAM

            // vertex shader 的函数是 vert
            #pragma vertex vert

            // fragment shader 的函数是 fragment
            #pragma fragment frag

            vert() {

            }

            frag () {

            }

            ENDCG
        }
    }
}
{% endcodeblock %}

代码中的 vertex shader 和 fragment shader 在渲染管道中的位置请参考这系列文章第二节 {% post_link Shader_2 [渲染管道] %}。

<hr>
鄙人才疏学浅，有出入的地方非常感谢能帮忙指正。:)