title: UNet 0x04： 做一个简单的 Network Manager 界面
date: 2015-08-12 14:01
category: Unity
tags: UNet
---

上一篇中我们引入了 NetworkManager 组件，然后在代码里面通过它来建立了网络连接。这篇让我们来把连接部分的代码独立出来，并提供 GUI 来达到管理 Server / Client 的开启和停止的目的。
这样我们以后就可以重复利用代码了。

下面是我们这个简单的 NetworkManger 界面提供的功能：

* 可以启动 / 停止 Server，并且多个程序端只能启动一个 Server
* 可以启动 / 停止 Client 并连接 Server
* 当 Server 停止时，所有 Client 端界面都会重置

这个简单的界面如下：

![ui](/images/UNet/SimpleUI.PNG)

本篇中的 demo 可以 [戳这里](https://github.com/wudixiaop/UNet/tree/master/Assets/104%20-%20simple%20network%20GUI) 得到，下面就 Demo 细说一下。

### 代码

我们通过 NetworkManager 的 `StartServer()` / `StopServer()` 方法来开启 / 停止 Server, `StartClient()` / `StopClient()` 方法来启动 / 停止 Client。我们可以新建一个 GameObject，
然后把下面脚本挂在它上面。脚本代码如下:

{% codeblock %}
using UnityEngine;
using UnityEngine.Networking;

public class SimpleNetworkGUI : MonoBehaviour
{
    bool isHaveNetworkRole = false;
    
    void Start()
    {
        isHaveNetworkRole = false;
    }
    
    private void OnDisconnected(NetworkMessage msg)
    {
        isHaveNetworkRole = false;
        Application.LoadLevel(Application.loadedLevel);
    }
    
    void OnGUI()
    {
        if(isHaveNetworkRole)
        {
            if(GUI.Button(new Rect(Screen.width / 2 - 80, Screen.height / 2 - 12, 160, 24), "Stop"))
            {
                NetworkManager.singleton.StopServer();
                NetworkManager.singleton.StopClient();
                OnDisconnected(null);
            }
            return;
        }
        
        if(GUI.Button(new Rect(Screen.width / 2f - 80, Screen.height / 2 - 12, 160, 24), "Start Server"))
        {
            isHaveNetworkRole = NetworkManager.singleton.StartServer();
        }
        
        if(GUI.Button(new Rect(Screen.width / 2f - 80, Screen.height / 2 + 24, 160, 24), "Start Client"))
        {
            var client = NetworkManager.singleton.StartClient();
            client.RegisterHandler(MsgType.Disconnect, OnDisconnected);
            isHaveNetworkRole = true;
        }
    }
}
{% endcodeblock %}

### 关于 Demo 其他一些需要知道的

* 首先，代码中利用了 NetworkManager 组件。我们可以把这个组件挂到挂有上面 UI 脚本的 GameObject 之上。
* 为了演示效果，Demo 里面创建了一个Prefab， 这个 Prefab 会传递给上面的 NetworkManager 组件（Spawn Info 下的 Player Prefab）。当 Client 连接已经启动的 Server 的时候，Server 端会创建这个 Perfab 的实例。
这个 Prefab 比较特殊，它上面需要添加 __NetworkIndentity__ 组件，这样才能传递过去给 NetworkManager。

到这里，可能有的朋友有疑问。什么 Spawn？ NetworkIndentity 又是什么鬼？

### UNet 中的 Spawn

换句话说，Spawn 就是网络对象实例的初始化这个行为，再换句话说就是创建网络对象。在 UNet 中用 Spawn 来描述，而不是用 Instantiate。

UNet 是个以 Server 为主导的系统，所有的 Spawn 行为都要在 Server 端发生，通过调用 `NetworkServer.Spawn( GameObject go )` 方法，产生的对象会在各个 Client 出现对应的实例。

### 网络对象与 NetworkIndentity

每个网络对象（Networked Object）都需要在根上带上 NetworkIndentity 组件。那 NetworkIndentity 组件是什么？ 大概是这个样子：

* 它是标志对象网络身份的一个组件
* 拥有系统用来跟踪对象的信息，比如 SenceId, NetworkID, AssetID 等
* 所有需要 Spawn 的 Prefab 都必须在对象根上带有这个组件

对了，需要注意一点。带有 NetworkIndentity 组件的对象，在未 Spawn 之前是不可用的，Disabled 状态，即使在 Hierarchy 里面有它的实例也会自动被 Disabled.

### NetworkManagerHUD 组件

为什么要提到这个组件呢。因为它也是一个 NetworkManager 管理的界面。它是 Unity 提供给我们的，提供比我们这篇文章所给的更加丰富的功能。平时开发调试的时候，建议使用这个控件。
引出 NetworkManagerHUD 组件也是这篇文章的目的。

好了，这篇就到这里。Enjoy!
