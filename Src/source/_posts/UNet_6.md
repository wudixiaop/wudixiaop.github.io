title: UNet 0x06：Command
date: 2015-08-23 12:01
category: UnityKB
tags: UNet
---

最开始我们来对上篇文章 {% post_link UNet_5 [UNet 0x05: SyncVar] %} 中的程序做点修改。在这里也建议朋友们先阅读上篇，然后继续阅读下面内容。

我们先把只在 Server 端绘制的按钮：

{% codeblock %}
if (isServer)
{
    if (GUI.Button(new Rect(10, 56, 160, 24), "ChangeState"))
    {
        ChangeState();
    }
}
{% endcodeblock %}
	
改成在 Client 端绘制
	
<!--more-->


{% codeblock %}
if (!isServer) // 这里是改变的地方
{
    if (GUI.Button(new Rect(10, 56, 160, 24), "ChangeState"))
    {
        ChangeState();
    }
}
{% endcodeblock %}
	
改完之后我们运行程序会得到一个结果：无论我们怎么点 ChangeState 按钮，Client 端左上角文字有变化，而 Server 端左上角的文字都不会变化。

这为什么呢？我们上篇文章中提到 SyncVar 只能从 Server 到 Client 端的方向起作用，所以我们上面点击 ChangeState 按钮是在 Client 端执行的，只改变了 Client 端的值，不会对 Server 端起作用。

这篇要介绍的就是能从 Client 端做出的改变也能同步的所有终端的功能。它就是 NetworkBevhaiour 提供 __sending commands__ 功能。

### Command

那什么是 Command 呢？如果了解设计模式的朋友应该知道有种设计模式叫做 Command 模式（命令模式），这里的 Command 代表一种行为，UNet 中的 Command 也是代表一种行为，换句话说就是一个函数。但是在 UNet 中这个函数有些特别的规定，它要求：

* 函数的名字 __必须以 Cmd 开头__，这里注意大小写哟。
* 必须带上 __[Command]__ 属性

用代码来示范下就是：

{% codeblock %}
[Command]
private void CmdDoSomething()
{
    // do something
}
{% endcodeblock %}

这里还有几点需要知道的：

* Command 是从 Client 端发起的。当需要从 Client 端发出改变的时候使用它。
* 每个客户端的 spawn 之后的对象，都会在其他各端（包括 Server）有同样的实例。而真实执行 Command 的是在 Server 上的那个实例。所以其实 Command 的执行最终也是在 Server 上的，只不过 Client 会发送请求，要求 Server 上对应的实例来执行这个 Command。这正好符合 UNet 是以 Server 为主导的理念。

接下来我们继续对上篇文章中的代码做些修改。

首先，我们新加入一个 Command 方法：

{% codeblock %}
[Command]
private void CmdChangeState()
{
    ChangeState();
}
{% endcodeblock %}
	
然后我们把 ChangeState 调用的方法从 `ChangeState()` 改成 `CmdChangeState()`：

{% codeblock %}
void OnGUI()
{
    GUI.Label(new Rect(10, 20, 120, 24), State);
    
    if (!isServer)
    {
        if (GUI.Button(new Rect(10, 56, 160, 24), "ChangeState"))
        {
            CmdChangeState();
        }
    }
} 
{% endcodeblock %}
	
这样我们就利用了 Command 方法 `CmdChangeState` 来作出改变了。

### 示例代码

下面是加上 Command 方法之后的最终代码。这样每次在 Client 端点击 ChangeState 按钮的时候，各个终端中 State 字段的值都会发生改变。Demo 程序的地址为: <https://github.com/wudixiaop/UNet/tree/master/Assets/106%20-%20Command> 。

{% codeblock %}
using UnityEngine;
using UnityEngine.Networking;

public class CommandSample : NetworkBehaviour {

[SyncVar]
string State = "Init State";

private void ChangeState()
{
    State = Random.Range(0, int.MaxValue).ToString();
}

[Command]
private void CmdChangeState()
{
    ChangeState();
}

void OnGUI()
{
    GUI.Label(new Rect(10, 20, 120, 24), State);
    
    if (!isServer)
    {
        if (GUI.Button(new Rect(10, 56, 160, 24), "ChangeState"))
        {
            //  ChangeState();
            CmdChangeState();
        }
    }
}
{% endcodeblock %}

### SyncVar Vs Command

下面是一张从 Unity 手册中借来的一种图片，

![UNetDirection](/images/UNet/UNetDirections.jpg)

上面图中的 `State Updates` 是指的 SyncVar。我们从图中可以了解到：

* SyncVar 是从 Server -> Client 方向来改变所有端的同一对象实例的状态
* Command 是从 Client -> Server 方向来改变所有端的同一对象实例的状态