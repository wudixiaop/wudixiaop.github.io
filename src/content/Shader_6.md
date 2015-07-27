Title: 瞎聊 Unity Shader 系列之六：初识 Shaderlab
Date: 2015-05-05 17:55
Modified: 2015-05-05 17:55
Category: Shader
Tags: Shader
Status: published
Keywords: Unity, Shaderlab, Shader, Unity Shader

好吧，其实这不算初识 Shaderlab 了，因为在 [shaderlab 土地上的语言们]({filename}/Shader_3.md) 这节中已经说到在 shaderlab 中有三种方式来写 shader。
这节的内容主要是来认识下 shaderlab 语法写出来的 shader 长得什么样子。

下面有段基于 shaderlab 的 shader 的大概框架的伪代码，在之前要解释下代码中带中括号的部分，如 `[Properties]`, 表示是可以选择的，也就是说可以不写。

	:::cuda
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

上面伪代码中的注释解释了各个部分的作用，如果去除可选部分，最后就留下**精简的骨架**:

	:::cuda
	Shader "shader 的名字" {

		Subshader {

			Pass { }
		}
	}

而大部分 shader 都是在上面代码基础上扩展的。

这节就到这里，会在后面的章节继续聊 shaderlab。

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
- [瞎聊 Unity Shader 系列之十一：深度缓存]({filename}/Shader_11.md)


鄙人才疏学浅，有出入的地方非常感谢能帮忙指正。:)