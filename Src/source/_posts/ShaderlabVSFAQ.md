title: ShaderlabVS 的一些常见问题
date: 2015-12-27 21:33:08
tags: Shader
category: Shader
---

谢谢朋友们这一年多来对 ShaderlabVS 插件的支持。这里整理出一些朋友给我的留言或者邮件中提到的常见问题，希望对大家有帮助。

### 常见问题

#### 黑色背景下文字看不清楚，如何改变字体颜色

1. 打开 VS -> 工具 -> 选项 -> 环境 -> 字体和颜色,
2. 显示其设置 下拉列表中选择 文本编辑器 （如果没改过，这就是默认的）。
3. 在 显示项(D) 文字下面的列表框中选择以 “Shaderlab-” 开头的项，然后改变前景色
4. 改完后确定就可以了

#### 插件安装碰到错误: `扩展“ShaderlabVS”需要的 .NET Framework 版本没有安装。
尝试安装已移除 .Net Framework 依赖版本的 0.6.1。  

下载地址：
- VS2015: http://pan.baidu.com/s/1pK5GIU3
- VS2012 / VS2013: http://pan.baidu.com/s/1pK5GIU3 

<!--more-->

#### 插件安装上后没有效果 

一般是由于 .shader 或者 .cginc 文件没有和 ShaderlabVS 插件没有关联上。原因可能是：

- 安装了其他跟 .shader 和 .cginc 文件相关的其他插件
- 关闭 VS, 安装插件，然后执行 [vs2015_2013_2012-register.cmd](https://github.com/wudixiaop/ShaderlabVS/tree/master/Tools) 
来关联插件, 执行之后重启 VS

#### 其他问题
发邮件到 rockylai@shuiguzi.com，我会尽量解答。