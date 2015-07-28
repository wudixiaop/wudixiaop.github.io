Title: 好玩：如何把 Github Contributions 填充满
Date: 2015-07-21 12:50
Modified: 2015-07-21 12:54
Category: 一点一滴
Tags: Python
Status: published
Keywords: RockStar, Github, Github Contributions 填充

先看效果：  
![rockstar](images/RockStar/rockstar.PNG){: width="100%"}

我们要使用 RockStar 这个 python 工具来实现这个效果。RockStar 的 Github 地址 [撮这里](https://github.com/avinassh/rockstar)。

RockStar 只支持 Python 3，不能在 Python 2 上面。如果本机没有 Pyhon3 可以从 <http://python.org> 里面下载安装，当前版本的下载地址为 <https://www.python.org/downloads/release/python-343/>。

使用 python 前我们需要在环境变量中加入 python3 的安装路径和脚本文件的路径。假如我们安装在 `C:\Python34` 文件夹下，则加入下面地址到环境变量 `PATH` 中

> C:\Python34;C:\Python34\Scripts


上面设置完成之后我们就可以用 python 来玩耍啦。首先我们打开命令行来安装 RockStar ，输入

> pip install rockstar

输入完成之后, 我们创建一个新文件夹，比如叫做 RSFunny, 并在这个文件夹下面创建一个 python 脚本，比如叫做 rockstar.py。 脚步的内容如下：

	:::python
	from RockStar import RockStar

	csharp_code = """using System;
	
	class HelloWorld
	{
	    static void Main()
	    {
	        Console.WriteLine("I'm Rocky");
	    }
	}"""
	
	# 400 天
	rock_it_bro = RockStar(days=400, file_name='rockstar.cs', code=csharp_code)
	rock_it_bro.make_me_a_rockstar()

更多的例子我们能参考这里 <https://github.com/avinassh/rockstar/tree/master/examples>。
	
接下来，在命令行中跳转到到 RSFunny 目录下, 准备运行 rockstar.py。这里需要注意一下，因为脚本需要用到 git.exe，所以我们需要把 git.exe 的路径加入到当前的环境变量 `PATH` 中，不然会抛出找不到文件的错误。
如果安装了 Github for Windows 客户端，我们可以从客户端的安装目录 `%AppData%\..\Local\GitHub` 下找到 git.exe。添加完后，我们运行脚本：  

> python rockstar.py

运行完后，脚本将 RSFunny 目录变成一个 git 仓库。

好了，万事具备，只欠发布到 Github 了。 建议使用最新版 Github for Windows 客户端，简单快捷，居家旅行必备。。。

不知道怎么在 Github for Windows 客户端添加？ 那就点点左上角的 + 号，然后结合下面这个截图看看，相信应有收获的。 :) 

![gitAddRepo](images/RockStar/gitAddRepo.PNG){: width="100%"}

Enjoy!
