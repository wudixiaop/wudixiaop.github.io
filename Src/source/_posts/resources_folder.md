title: Resources 文件夹
date: 2016-12-28 12:40:00
category: UnityKB
tags: AssetBundle
---

<div style='display:none'>
The Resources folder
----
</div>

<div style='display:none'>
This is the third chapter in a [series of articles covering Assets, Resources and resource management](https://unity3d.com/de/learn/tutorials/topics/best-practices/guide-asset-bundles-and-resources) in Unity 5.
</div>

这是 Unity 5 {% post_link GuideToABAndRes [资产, 资源和资源管理系列文章] %}的第三篇。

<div style='display:none'>
This chapter discusses the Resources system. This is the system that allows developers to store Assets within one or more folders named Resources and to load or unload Objects 
from those Assets at runtime using the Resources API.
</div>

这个章节将讨论 Resources 系统。这个系统可以让开发者通过 Resources API 加载或卸载存储在在一个或多个以 Resources 命名的文件夹中的资产。

<div style='display:none'>
### 2.1. Best Practices for the Resources System
</div>

### Resources 系统的最佳实践

<div style='display:none'>
__Don't use it.__
</div>

__下面情况不要使用它__

<!-- more -->
<div style='display:none'>
This strong recommendation is made for several reasons:

* Use of the Resources folder makes fine-grained memory management more difficult.
* Improper use of Resources folders will increase application startup time and the length of builds.
    * As the number of Resources folders increases, management of the Assets within those folders becomes very difficult.

* The Resources system degrades a project's ability to deliver custom content to specific platforms and eliminates the possibility of incremental content upgrades.

    * AssetBundle Variants are Unity's primary tool for adjusting content on a per-device basis.
</div>

这个强烈建议有下面几点原因：

* 使用 Resources 文件夹会让内存颗粒度管理变得更困难
* 不正确的使用 Resources 文件夹会增加应用启动时间和包的大小
    * 随着在 Resources 文件中的文件增加，管理这些文件会变得很困难
* Resources 系统自定义的平台特殊文件推送变得恶化并且不能增量更新
    * AssetBundle 变体是 Unity 用来不同平台内容调整的主要工具
    
<div style='display:none'>
### 2.2. Proper uses of the Resources system
</div>

### Resources 系统正确使用：

<div style='display:none'>
There are two specific use cases where the Resources system can be helpful without impeding good development practices:
</div>

下面两种情况 Resources 系统很有用处：

<div style='display:none'>
1. Resources is an excellent system for during rapid prototyping and experimentation because it is simple and easy to use. However, when a project moves into full production, it is strongly recommended to eliminate uses of the Resources folder.

2. The Resources folder is also useful in trivial cases, when all of the following conditions are met:

* The content stored in the Resources folder is not memory-intense
* The content is generally required throughout a project's lifetime
* The content rarely requires patching
* The content does not vary across platforms or devices.
</div>

1. 因为 Resources 系统很容易使用，它很适合是在快速原型制作和试验。但是当项目要转成产品时，强烈建议不要使用 Resources 文件夹
2. Resources 文件夹对一些满足如下条件的案例很有用：
    * 存储在 Resources 文件夹下的内容不要很大的内存
    * 存储在 Resources 文件夹下的内容在整个项目周期都有用
    * 内容基本不用升级
    * 内容在各平台都一样的

<div style='display:none'>
Examples of this second case include a globally-used prefab hosting singleton MonoBehaviours or an Asset hosting third-party configuration data, such as a Facebook App ID.
</div>

上面第二种情况（存储在 Resources 文件夹下的内容在整个项目周期都有用）例子包括在全局使用的 MonoBehaviour 单例的预设或者第三方配置数据中的资产，比如 Facebook 应用的 ID。

<div style='display:none'>
### 2.3. Serialization of Resources

The Assets and Objects in all folders named "Resources" are combined into a single serialized file when a project is built. This file also contains metadata and indexing information, similar to an AssetBundle. As described in the [Sidebar: What's in an AssetBundle?](https://unity3d.com/de/learn/tutorials/topics/best-practices/asset-bundle-fundamentals#Whats_in_an_Asset_Bundle) section of the [AssetBundle fundamentals](http://note.youdao.com/https://unity3d.com/de/learn/tutorials/topics/best-practices/asset-bundle-fundamentals) chapter, this indexing information includes a serialized lookup tree that is used to resolve a given Object's name into its appropriate File GUID and Local ID. It is also used to locate the Object at a specific byte offset in the serialized file's body.
</div>

当项目构建完成之后，所有名为 `Resources` 的文件夹内的资产和对象都会被合并到然后序列化到同一个文件中。这个文件跟 AssetBundle 类似，包括包含了源数据和索引信息。就像在 AssetBundle 基本原理章节中的 __什么是 AssetBundle__ 小节中提到的，索引信息里面包括了处理对象名字到对应的文件 GUID 和本地ID 的查找树。它也用来定位对象在序列化文件中的偏移位置。

<div style='display:none'>
As the lookup data structure is (on most platforms) a balanced search tree(1), its construction time grows at an O(N log(N)) rate, where N is the number of Objects indexed within the tree. This growth also causes the index's loading time to grow more-than-linearly as the number of Objects in Resources folders increases.
</div>

用于查找的数据结构是平衡搜索树<a href='#f1'>[1]</a>（在大多数平台上），它的构建时间增长到了 O(nLog(N)), 其中 N 是在查找树内的对象的个数。这个增长也使 Resources 文件夹内的对象增加时，索引的加载时间会比线性增长时间长。

<div style='display:none'>
This operation is unskippable and occurs at application startup time while the initial non-interactive splash screen is displayed. Initializing a Resources system containing 10,000 assets has been observed to consume multiple seconds on low-end mobile devices, even though most of the Objects contained in Resources folders are rarely actually needed to load into an application's first scene.
</div>

这个操作是在程序启动，不可交互的闪屏页显示时发生，是不能去除的。一个包含 10000 个资产的 Resouces 系统，即使其中大部分资产都不需要在第一个场景中加载，在低端移动设备上初始化也需要好几秒的时间。

<div style='display:none'>
### Footnotes
</div>

### 脚注

<div style='display:none'>
On most platforms, it is a std::multimap from the C++ Standard Template Library.  
</div>

<div id='f1'>
[1] 在大部分平台上是 C++ STL（Standard Template Library）中的 std:multimap

</div>

原文链接: <https://unity3d.com/learn/tutorials/topics/best-practices/asset-bundle-fundamentals>