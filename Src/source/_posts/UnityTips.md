title: Unity Tips - 关于 Untiy 一些需要知道的技巧
date: 2016-02-16 22:03
category: Unity
tags: Tips
---

Unity Tips
----------------
* `List<T>` 或者数组序列化的时候默认生成的名字为 Element n，如果要改变这个，只需要把 T
的第一个序列化的字段的数据类型设置为 `string`
* 保存 Play 模式下调试出的数据：在组件的右上角点击右键，选择 `Copy Component`，然后关闭 Play
模式之在对应的组件右上角点击右键，选择 `Copy Component as Values`。 跟多小技巧请看 [这个链接](https://mp.weixin.qq.com/s?__biz=MjM5NjM3NDA1Mg==&mid=401777518&idx=1&sn=aa995d6c44866fb0f5bcc096e75969bb&scene=0&key=710a5d99946419d912a29c647796b42ba9c71553d849b38d45c2b41608a344d5befb72dd9cb578c745cd931a0e330ad7&ascene=0&uin=MTQ0NjU3MzQyNw)。



性能 Tips
----------------
* 用 `for` 循环代替 `foreach` 循环
* 禁止不动的物体可以用 lightmap 来烘焙阴影贴图
* 移动端，清晰度可以接受的情况选尽量用低质量的贴图
* 用原生的数组代替 `List<T>`能提高性能