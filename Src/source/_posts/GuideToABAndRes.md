title: 资源和 AssetBundle 指导
date: 2016-12-15 17:40:00
category: UnityKB
tags: AssetBundle
---
<div style='display:none'> This is a series of articles that provides an in-depth discussion of Assets and resource management in the Unity engine. It seeks to provide expert developers with deep, source-level knowledge of Unity's Asset and serialization systems. It examines both the technical underpinnings of Unity's AssetBundle system and the current best practices for employing them.
</div>

这是深度探讨 Unity 引擎中资源（Resource）和资产（Asset） 管理的系列文章。文章试图给高级开发者提供 Unity 资产和序列化系统的底层、代码级的知识，并且审视 Unity 的 AssetBundle 系统技术基础和当前使用它们的最佳实践。

<div style='display:none'>
The guide is broken down into four chapteros:

1. [Assets, Objects and serialization](https://unity3d.com/learn/tutorials/topics/best-practices/assets-objects-and-serialization) discusses the low-level details of how Unity serializes Assets and handles references between Assets. It is strongly recommended that readers begin with this chapter as it defines terminology used throughout the guide.
2. [The Resources folder](https://unity3d.com/learn/tutorials/topics/best-practices/resources-folder) discusses the built-in Resources API.
3. [AssetBundle fundamentals](https://unity3d.com/learn/tutorials/topics/best-practices/asset-bundle-fundamentals) builds on the information in chapter 1 to describe how AssetBundles operate, and discusses both the loading of AssetBundles and the loading of Assets from AssetBundles.
4. [AssetBundle usage patterns](https://unity3d.com/learn/tutorials/topics/best-practices/asset-bundle-usage-patterns) is a long article discussing many of the topics surrounding the practical uses of AssetBundles. It includes sections on assigning Assets to AssetBundles and on managing loaded Assets, and describes many common pitfalls encountered by developers using AssetBundles.
</div>

系列文章将会拆分为四个章节：
1. {% post_link Assets_Objects_serialization [资产，对象和序列化] %} 章节探讨 Unity 如何序列化资产和处理它们之间的引用的底层细节。__强烈推荐从读者从这章开始阅读，因为它定义了贯穿这系列文章的术语__。
2. {% post_link resources_folder [Resources 文件夹] %} 探讨内置的 Resources API.
3. [AssetBundle 基本原理](https://unity3d.com/learn/tutorials/topics/best-practices/asset-bundle-fundamentals) 在第一章的基础上描述 AssetBundles 怎么运转和加载 AssetBundles 及从 AssetBundles 加载资产。
4. [AssetBundle 使用模式](https://unity3d.com/learn/tutorials/topics/best-practices/asset-bundle-usage-patterns) 是一篇探讨很多 AssetBundle 的实际用途。它包括了给 AssetBundles 添加资产 和管理加载后的资产并描述了开发者使用 AssetBundles 时经常碰到的陷阱。

<div style='display:none'>
Note: This guide's terms for Objects and Assets differ from Unity's public API naming conventions.
</div>

注意：这系列文章中的对象和资产有别与 Unity API 命名约定中的对象和资产。

<!-- more -->

<div style='display:none'>
The data this guide calls Objects are called Assets in many public Unity APIs, such as [AssetBundle.LoadAsset](http://docs.unity3d.com/ScriptReference/AssetBundle.LoadAsset.html) and [Resources.UnloadUnusedAssets](http://docs.unity3d.com/ScriptReference/Resources.UnloadUnusedAssets.html). The files this guide calls Assets are rarely exposed to any public APIs. When they are exposed, it is generally only in build-related code, such as [AssetDatabase](http://docs.unity3d.com/ScriptReference/AssetDatabase.html) and [BuildPipeline](http://docs.unity3d.com/ScriptReference/BuildPipeline.html). In these cases, they are called files in public APIs.
</div>

本指导中所指的对象是数据，在很多 Unity API 中叫做资产，比如 [AssetBundle.LoadAsset](http://docs.unity3d.com/ScriptReference/AssetBundle.LoadAsset.html) and [Resources.UnloadUnusedAssets](http://docs.unity3d.com/ScriptReference/Resources.UnloadUnusedAssets.html)。 本指导中的资产很少在公开的 API 中出现。当他们出现时，一般仅在和构建相关的代码中，比如 [AssetDatabase](http://docs.unity3d.com/ScriptReference/AssetDatabase.html) and [BuildPipeline](http://docs.unity3d.com/ScriptReference/BuildPipeline.html)。这种情况下，公开的 API 中都叫它们为文件。

原文链接: <https://unity3d.com/cn/learn/tutorials/topics/best-practices/guide-assetbundles-and-resources>