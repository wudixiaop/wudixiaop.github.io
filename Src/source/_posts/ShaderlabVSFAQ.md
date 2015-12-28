title: ShaderlabVS 的一些常见问题
date: 2015-12-27 21:33:08
tags: Shader
category: Shader
---

谢谢朋友们这一年多来对 ShaderlabVS 插件的支持。这里整理出一些朋友给我的留言或者邮件中提到的常见问题，希望对大家有帮助。

### 常见问题

#### 插件安装碰到错误: `扩展“ShaderlabVS”需要的 .NET Framework 版本没有安装。
尝试安装已移除 .Net Framework 依赖版本的 0.6.1。下载地址：http://pan.baidu.com/s/1qX3CNy0


#### 插件安装上后没有效果 

一般是由于 .shader 或者 .cginc 文件没有和 ShaderlabVS 插件没有关联上。原因可能是：

- 安装了其他跟 .shader 和 .cginc 文件相关的其他插件
- 如果是 VS2015, 在插件安装之后需要执行 [vs2015-register.cmd](https://github.com/wudixiaop/ShaderlabVS/tree/master/Tools) 
来关联插件

#### 其他问题
发邮件到 rockylai@shuiguzi.com，我会尽量解答。