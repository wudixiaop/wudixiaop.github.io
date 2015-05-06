Title: 瞎聊 Unity3D Shader 系列之五：RGBA 101
Date: 2015-05-04 13:55
Modified: 2015-05-04 13:55
Category: Shader
Tags: Shader
Status: published

这节说说 fragment shader 最后输出的像素的颜色表示方法 RGBA。

玩过 Photoshop 的同学可能知道，存在好几种颜色模式来表示颜色，[比如 RGB 和 CMYK](http://baike.baidu.com/view/1139658.htm). 由于显示器的发光物体，所以使用的 RGB 模式。
Unity3D 中也采用这种表示方法。

###RGB模式
RGB是用红绿蓝混合来表示的颜色。R 是红色， G 表示绿色， B 是蓝色。一般用8为来表示一个颜色通道，每个通道有 256 个等级（0~255）。它有如下特性：

- `(0, 0, 0)` 表示黑色
- `(255, 255, 255)` 表示白色
- 三个通道数值相同的时候是灰色，比如 `(128, 128, 128)`
- 数值越大颜色越亮，反之数值越小越暗

![RGB](images/Shader/5/rgb.png){: width="61%"}

但是 Unity Shader 中并不用 256 个等级来表示颜色数值，而是用标准化（取值0~1）的数值来表示。换句话说就是所有通道都除以 255 得到标准化的结果。

###RGBA 中的 A 是什么

A 叫做 alpha，其数值表示不透明度。 据说提出者用 alpha 来命名源于经典的线性插值方程 αA + (1-α)B 所用的希腊字母 α。Unity3D 中的 aplha blending 基于这个线性方程。

###混合模式

抽象一下就是对两个颜色做运算后得到结果颜色的过程。这个过程其实就是个运算公式。下面列举两个 Photoshop 中常见的正片叠底和滤色两个混合模式的计算公式。C为结果色，A 和 B 是需要混合的颜色。

- **正片叠底(Multiply):** C=A*B
- **滤色(Screen):** C=1-(1-A)*(1-B)


我们要叠加模型多个贴图（比如法线贴图和模型贴图）的时候就可以利用到混合模式。更多混合模式公式参考[这个文档](http://wenku.baidu.com/view/da9d22d9ad51f01dc281f1f9.html)。

###系列文章目录
- [瞎聊 Unity3D Shader 系列之一：GPU 与 Shader Model]({filename}/Shader_1.md)
- [瞎聊 Unity3D Shader 系列之二：渲染管线]({filename}/Shader_2.md)
- [瞎聊 Unity3D Shader 系列之三：Shader 土地上的语言们]({filename}/Shader_3.md)
- [瞎聊 Unity3D Shader 系列之四：坐标系]({filename}/Shader_4.md)
- [瞎聊 Unity3D Shader 系列之五：RGBA 101]({filename}/Shader_5.md)
- [瞎聊 Unity3D Shader 系列之六：初识 Shaderlab]({filename}/Shader_6.md)
- [瞎聊 Unity3D Shader 系列之七：究竟谁先被渲染？]({filename}/Shader_7.md)
