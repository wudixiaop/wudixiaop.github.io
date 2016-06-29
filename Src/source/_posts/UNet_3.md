title: UNet 0x03：NetworkManager 初见
date: 2015-08-10 14:04
category: UnityKB
tags: UNet
---

阅读本章之前, 建议先阅读 {% post_link uNET_1 [UNet 0x01: 网络连接的建立] %} 和 {% post_link UNet_2 [UNet 0x02: 发送消息] %} 这两篇文章。

前两篇文章我们建立 Client / Server 间的连接的时候，手动配置了 Server 的端口和 Client 要连接的目标 Server 及其端口。这些都是在代码里面实现
的。这篇文章我们引入 UNet 提供的一个网络管理组件来达到同样的效果。这个组件的名字叫做 NetworkManager。

NetworkManager 组件提供了很多功能，但是这篇文章只引入 NetworkManager 组件，不打算深入讲这个组件。下面是 NetworkManager 在 Inspector 里面的长相：

![networkmanager](/images/UNet/NetworkManagerInspector.PNG)

上图中 Network Info 部分就是就是配置 Server 地址及其端口的地方。

接下来看看 NetworkManager 如何启动一个 Server / Client / Host。

<!--more-->

### 利用 NetowrkManager 的方法替换之前代码

利用 NetworkManager 的方法替换之前的代码，大体为：

* 之前我们用 `NetworkServer.listen(port)` 来启动一个 Server 并监听某个端口。NetworkManager 提供 `StartServer()` 方法替代
* 之前我们单独创建了 NetowrkClint 类的实例开创建 Client。 NetworkManager 提供 `StartClient()` 方法替代
* 如果想启动 Host (Server + Local Client)，NetworkManager 提供 `StartHost()` 方法

### 得到 NetworkManager 实例

NetworkManager 组件挂上 GameObject 之后我们可以像其他组件一同通过 `GetComponent<T>()` 这个方法来得到其实例，但是这推荐使用  `NetworkManager.singleton` 来得到其实例。

### 为什么要使用 NetworkManager

我觉得大概有如下几点：

* NetworkManager 包装了很多信息的设置，提供统一的入口
* 利用现成 NetworkManager 提供的功能，简化代码

但总体上的目的还是简化，复用代码。

### 代码示例

下面代码和 {% post_link UNet_2 [UNet 0x02: 发送消息] %} 一样，也是发送消息。功能上的区别就是下面代码中 Client 会每隔 5 秒自动发送消息给 Server。

{% codeblock %}
using UnityEngine;
using UnityEngine.Networking;

public class ComBaseOnNetworkManager : MonoBehaviour {

    private NetworkClient client;

    private float interval = 5f;
    private float time = 0f;
    
    void Start () {
        SetupServer();
        SetupClient();
    }
    
    void Update()
    {
        time += Time.deltaTime;
        if(time >= interval)
        {
            time = time - interval;
            SendMessageToServer();
        }
    }
    
    private void SetupServer()
    {
        if(NetworkServer.active)
        {
            return;
        }
        
        NetworkServer.RegisterHandler(MessageX.MsgType, OnMessageReceived);
        
        NetworkManager.singleton.StartServer();
    }
    
    private void SetupClient()
    {
        client = NetworkManager.singleton.StartClient();
    }
    
    private void OnMessageReceived(NetworkMessage msg)
    {
        Debug.Log(string.Format("SERVER: {0}", msg.ReadMessage<MessageX>()));
    }
    
    private void SendMessageToServer()
    {
        MessageX mx = new MessageX();
        mx.From = "NetworkMangerBase Sample";
        mx.Message = "Hello Rocky!";
        
        client.Send(MessageX.MsgType, mx);
    }
}
{% endcodeblock %}

代码可以在这里找到：[Github 地址](https://github.com/wudixiaop/UNet/tree/master/Assets/103%20-%20introduce%20NetworkManager)。
	
新建一个 GameObject， 在它挂上上面的脚本，然后添加 NetworkManager 组件，然后运行项目。控制台会得到类似下面的输出结果：

![output](/images/UNet/103Output.PNG)

Enjoy!