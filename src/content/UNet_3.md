Title: UNet 0x03: 引入 NetworkManager
Date: 2015-08-08 16:04
Modified: 2015-08-08 16:05
Category: Unity
Tags: UNet, Unity
Status: draft
Keywords: Unity, Networking, UNet, Unity networking

阅读本章之前, 建议先阅读 [UNet 0x01: 网络连接的建立]({filename}/uNET_1.md) 和 [UNet 0x02: 发送消息]({filename}/UNet_2.md) 这两篇文章。

前两篇文章我们建立 Client / Server 间的连接的时候，手动配置了 Server 的端口和 Client 要连接的目标 Server 及其端口。这些都是在代码里面实现
的。这篇文章我们引入 UNet 提供的一个网络管理组件来达到同样的效果。这个组件的名字叫做 NetworkManager。

NetworkManager 组件提供了很多功能，但是这篇文章只引入 NetworkManager 组件，不打算深入讲
这个组件。下面是 NetworkManager 在 Inspector 里面的长相：

![networkmanager](images/UNet/NetworkManagerInspector.PNG){: width="32%"}
