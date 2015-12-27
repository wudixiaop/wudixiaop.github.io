title: 瞎聊 Unity Shader 系列之六：初识 Shaderlab
date: 2015-05-05 17:55
category: Shader
tags: Shader
---

好吧，其实这不算初识 Shaderlab 了，因为在 {% post_link Shader_3 [shaderlab 土地上的语言们] %} 这节中已经说到在 shaderlab 中有三种方式来写 shader。
这节的内容主要是来认识下 shaderlab 语法写出来的 shader 长得什么样子。

下面有段基于 shaderlab 的 shader 的大概框架的伪代码，在之前要解释下代码中带中括号的部分，如 `[Properties]`, 表示是可以选择的，也就是说可以不写。

<!--more-->

{% codeblock %}
//shader 的名字会显示在 Unity 的 Inspector 中选择 shader 的菜单里面
Shader "shader 的名字" {
    // 属性
    [Properties]

    // 可能存在多个 subshader。Unity 会在所有 subshader 列表中选择当前环境中可用的第一个 subshader
    Subshader {
        // subshader 的标签
        [Tags]

        // 给多个 pass 公用的设置
        [Common State]

        // 可能存在多个 pass, 每个 pass 都会引起一次渲染过程
        Pass {
            // pass 的标签
            [Pass Tags]

            // 渲染设置, 如颜色混合
            [Render Setup]

            // 纹理设置，只有在 fixed function shader 中才可用
            [Texture Setup]
        }

        // 可以有多个 pass
        [其他的 Pass]
    }

    // 可以有多个 subshader
    [其他的 Subshader]

    // 当所有 subshader 失败的时候, 使用 Fallback 指定的 shader
    [Fallback]

    // 当有自定义 shader 的设置 UI 时候用
    [CustomEditor]
}
{% endcodeblock %}

上面伪代码中的注释解释了各个部分的作用，如果去除可选部分，最后就留下**精简的骨架**:

{% codeblock %}
Shader "shader 的名字" {

    Subshader {

        Pass { }
    }
}
{% endcodeblock %}

而大部分 shader 都是在上面代码基础上扩展的。

这节就到这里，会在后面的章节继续聊 shaderlab。

<hr>
鄙人才疏学浅，有出入的地方非常感谢能帮忙指正。:)