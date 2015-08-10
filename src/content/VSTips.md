Title: 如何在Visual Studio中愉快的玩耍
Category: 一点一滴
Date: 2014-12-24 14:50
Tags: Visual Studio
keywords: VS, VS tip

好吧，其实我想要说一些我觉得可以在Visual Studio中提高效率的经验。下面直接进入正题：


###熟记并使用各种快捷键
快捷键之所以叫快捷键就是因为它会让事情变得更快捷。好吧，其实我知道前面一句废话。下面就列举一些碰上常用的(基于Visual C# 2005快捷键映射)


> * 注释: **Ctrl + E, C** (也就是，先**Ctrl**和**E**一起摁，然后摁**C**. 下面碰到有带组合键的情况类似)
> * 取消注释: **Ctrl + E, U**
> * 整行剪切: **Ctrl + X**
> * 收起/展开光标所在行的概述(Outlining): **Ctrl + M, M**
> * 收起概述(Outlining)到定义: **Ctrl + M, O**
> * 收起/展开所有概述(Outlining): **Ctrl + M, L**
> * 呼出自动补全窗口: **Ctrl + J**
> * 回跳到光标上一次所在位置: **Ctrl + -** (这是减号)
> * MSDN帮助: **F1** (光标移到类名或者方法名上，然后摁**F1**)
> * 运行: **F5**
> * 编译: **F6**
> * 调试时Step Over/In: **F10**/**F11**
> * 跳转到定义: **F12**
> * 搜索和替换窗口: **Ctrl + Shift + F** 或者 **Ctrl + Shift + H**
> * 当然还有超级好用的自能感应: **Ctrl + .** (或者**Ctrl + Shift + F10**)


当然还有很多其他快捷，但是平时自己用的少，就不列举了。


###偷懒技巧一：使用代码片段管理器(Code Snippets Manager)


如果还不知道有这个东西的童鞋可以在Vistual Studio的工具菜单中找到。具体怎么用大家可以参照别的童鞋们的文章


* [Visual Studio 小技巧：自定义代码片断](http://www.cnblogs.com/cyq1162/archive/2013/06/14/3135373.html)
* [使用Visual Studio Snippet(片断)提交开发效率](http://kb.cnblogs.com/page/42164/)


简单一句话描述Code Snippets使用就是：如果用C#举例，编写代码的时候，输入代码片段的快捷键(比如for), 然后摁两下Tab键，接下来就知道怎么做了。


按惯例，列举一些C#常用的:
> * 循环: **for**, **foreach**
> * 生成类: **class**
> * 生成构造函数: **ctor**
> * 生成属性: **prop**, **propfull**, **propdp**(Wpf系列中的依赖属性)


###偷懒技巧二: Toolbox


文字看多了，咱们来看视频吧

<iframe src="//channel9.msdn.com/Series/vstips/lazycodesnippets/player?format=html5" allowFullScreen frameBorder="0"></iframe>

视频源地址：<http://channel9.msdn.com/Series/vstips/lazycodesnippets>


###成为高手~~


不想成为标题党的程序员不是一个好写手。好吧，其实我是来推荐**VsVim**这个插件的。。。


首先，我们需要安装**VsVim**。童鞋们可以在VS工具菜单下的扩展及更新(Extension and Updates)里查找并安装。具体可以参照这篇文章: <http://www.tuicool.com/articles/YF7RNv>


然后开始练技能打怪练级:


* <http://coolshell.cn/articles/5426.html>
* <https://github.com/jaredpar/VsVim/wiki/faq>


再然后会慢慢发现平时编码时摸鼠标的次数越来少。。。

再然后。。。没有再然后了。。
