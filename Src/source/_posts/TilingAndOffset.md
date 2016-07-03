title: Tiling 和 Offset 是什么鬼？
date: 2016-07-03 16:47:42
category: UnityKB
tags: Shader
---

相信做过 Unity 开发的同学都在 Inspector 里面见过 Tiling 和 Offset。一般情况下它们两总是形影相随，不分不离，你中有我，我中有你。。。咳咳，我们回归正题。正常情况下它们都是成对出现的，如下图。

![inspector](/images/TilingOffset/Inspector.jpg)

讲 Tiling 和 Offset 之前我们先讲些其他相关的零散的知识。

### 纹理的 UV

UV 是一种标准化了的 2D 坐标系统，等同于 XY 坐标系统，为了不和 XY 混淆，用 U 和 V 分别表示对应的 X 和 Y。UV 系统中， `(0, 0)` 表示左纹理的下角，`(1, 1)` 表示纹理的右上角。

<!-- more -->

### 纹理的 Wrap Mode

Unity 中纹理的 Wrap Mode 可以设置值有：Repeat 和 Clamp。

![warpMode](/images/TilingOffset/textureWrapMode.jpg)

__Clamp__ 模式中 UV 都将被限制在 `0-1` 的范围内，如下图 U 轴（图来自[这里](http://www.manew.com/thread-4363-1-1.html)），左右两侧不相连：

![clamp](/images/TilingOffset/clamp.jpg)

__Repeat__ 中 U 轴是相连的：

![repeast](/images/TilingOffset/repeat.jpg)

同学们现在是否有一种看到 __Repeat__ 模式像是在地板上贴瓷砖的感觉。如果能有这种感觉，我这里给你点个赞。

### 纹理的 _ST

Shaderlab 中纹理都会分配一个对应属性名后加 _ST 的变量来表示纹理的缩放（Scale => S）和偏移（Translation => T)。比如属性 `_MainTex` 其对应的变量为 `_MainTex_ST`。关于 Shaderlab 属性，可以参照 {% post_link Shader_9 [瞎聊 Unity Shader 系列之九：用来包装变量的 Properties] %} 

### Shaderlab 中 TRANSFORM_TEX 

Unity Shaderlab 中的 UnityCG.cginc 有 `TRANSFORM_TEX` 的定义：

> #define TRANSFORM_TEX(tex,name) (tex.xy * name##_ST.xy + name##_ST.zw)

其中 name 为纹理对应属性名，__其中 `name##_ST.xy` 表示缩放，`name##_ST.wz` 表示偏移。__ 

下面我们先贴 [Unity 手册](http://docs.unity3d.com/Manual/SL-VertexFragmentShaderExamples.html) 中一段代码看看 `TRANSFORM_TEX` 是如何在 Shaderlab 编程中使用的。

{% codeblock %}
Shader "Unlit/NewUnlitShader"
{
    Properties
    {
        _MainTex ("Texture", 2D) = "white" {}
    }
    SubShader
    {
        Tags { "RenderType"="Opaque" }
        LOD 100

        Pass
        {
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            // make fog work
            #pragma multi_compile_fog
            
            #include "UnityCG.cginc"

            struct appdata
            {
                float4 vertex : POSITION;
                float2 uv : TEXCOORD0;
            };

            struct v2f
            {
                float2 uv : TEXCOORD0;
                UNITY_FOG_COORDS(1)
                float4 vertex : SV_POSITION;
            };

            sampler2D _MainTex;

            // 这里是 Shaderlab 分配的
            //
            float4 _MainTex_ST; 
            
            v2f vert (appdata v)
            {
                v2f o;
                o.vertex = mul(UNITY_MATRIX_MVP, v.vertex);

                // TRANSFORM_TEX 确保材质球里的缩放和偏移设置是正确的
                //
                o.uv = TRANSFORM_TEX(v.uv, _MainTex);  
                UNITY_TRANSFER_FOG(o,o.vertex);
                return o;
            }
            
            fixed4 frag (v2f i) : SV_Target
            {
                // sample the texture
                fixed4 col = tex2D(_MainTex, i.uv);
                // apply fog
                UNITY_APPLY_FOG(i.fogCoord, col);
                return col;
            }
            ENDCG
        }
    }
}
{% endcodeblock%}

### Tiling 和 Offset

在 Unity 编辑器中创建一个新的 Shader 和材质, 然后将新的 Shader 拖到新建的材质上，在 Inspector 中得到下图：

![inspector](/images/TilingOffset/InInspector.jpg)

我们看到纹理材质的 Inspector UI 中  `_MainTex` 出现了 `Tiling` 和 `Offset`。通过阅读反编译过来的 [MaterialEditor](https://github.com/MattRix/UnityDecompiled/blob/cc432a3de42b53920d5d5dae85968ff993f4ec0e/UnityEditor/UnityEditor/MaterialEditor.cs) 的源码，我们可以得到 ScaleOffset 属性就是 Tilling 和 Offset， __也就是说 _MainText_ST.xy 就是 Tiling, _MainTex_ST_.wz 是 Offset__。

### Tiling 和 Offset 与纹理 Wrap Mode

当 Tiling 的 XY 在 `[-1, -1]` 区间的时候，纹理的 Wrap Mode 无论是 Repeat 还是 Clamp 对现实效果都没有影响，但是在 [-1, 1] 范围之外就有影响了。

例如，假设 Tiling 为 (3, 3) Offset 为 (0, 0), 在 Repeat 模式下显示为：

![33repeat](/images/TilingOffset/33repeat.jpg)

而 Clamp 模式下为：

![33clamp](/images/TilingOffset/33clamp.jpg)

为什么会这样？还记得吗？clamp 模式下 UV 是不连续的，而 repeat 模式下 UV 是连续的。

### Tiling 和 Offset 能用来做什么？

还记得吗，上面提到的贴往地板上贴瓷砖，我们可以把纹理的 Wrap Mode 设置成 Repeat， 然后加大 Tiling 的值就“可以贴好多个瓷砖了”。抽象一下就是可以得到：

* 使用在需要重复很多相同纹理的情景。

除此之外，还可以

* 通过修改 Tiling 和 Offset 对纹理做裁剪。 
* 对 Offset 做动画来改变 UV 实现水流效果等特效
* 实现精灵动画

还有很多其他情况大家可以自己去发掘。好了这篇就啰嗦到这里。Enjoy!




