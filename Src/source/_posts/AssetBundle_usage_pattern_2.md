title: AssetBundle 使用模式 (2)
date: 2017-10-27 12:30
category: UnityKB
tags: AssetBundle
---------

<div style='display:none'>
## 4.4. Patching with AssetBundles
</div>

## 给 AssetBundle 打补丁

<div style='display:none'>
Patching AssetBundles is as simple as downloading a new AssetBundle and replacing the existing one. If [WWW.LoadFromCacheOrDownload](http://docs.unity3d.com/ScriptReference/WWW.LoadFromCacheOrDownload.html) or [UnityWebRequest](http://docs.unity3d.com/ScriptReference/WWW.LoadFromCacheOrDownload.html) are used to manage an application's cached AssetBundles, this is as simple as passing a different version parameter to the chosen API. (See the above links to the scripting reference for more details.)
</div>

给 AssetBundle 打补丁就如简单地下载一个新的 AssetBundle 然后替换已存在的。如果 [WWW.LoadFromCacheOrDownload](http://docs.unity3d.com/ScriptReference/WWW.LoadFromCacheOrDownload.html) or [UnityWebRequest](http://docs.unity3d.com/ScriptReference/WWW.LoadFromCacheOrDownload.html) 被用来管理应用已缓存的 AssetBundle，这个过程就是给所选的 API 传递不同的版本号一样简单。（可以参考上面的脚本参考链接来查看更多详情。）

<div style='display:none'>
The more difficult problem to solve in the patching system is detecting which AssetBundles to replace. A patching system requires two lists of information:

* A list of the currently downloaded AssetBundles, and their versioning information
* A list of the AssetBundles on the server, and their versioning information
</div>

更困难的问题是解决补丁系统探测哪个 AssetBundle 需要被替换。一个补丁系统需要两个信息列表：

* 当前已下载的 AssetBundle 和它们的版本信息列表
* 远程服务器上的 AssetBundle 和它们的版本信息列表

<div style='display:none'>
The patcher should download the list of server-side AssetBundles and compare the AssetBundle lists. Missing AssetBundles, or AssetBundles whose versioning information has changed, should be re-downloaded.
</div>
z
修补程序需要下载服务器端的 AssetBundle 列表和然后比较这个列表。AssetBundle 丢失或者 AssetBundle 的版本信息改变了，都需要重新下载。

<div style='display:none'>
Unity 5's AssetBundle system creates one additional AssetBundle when a build is completed. This extra AssetBundle contains an AssetBundleManifest object. This manifest object contains a list of AssetBundles and their hashes, and can be used to deliver the list of available AssetBundles and versioning information to clients. For more information on the AssetBundle manifest bundle, see the [Unity Manual](http://docs.unity3d.com/Manual/BuildingAssetBundles5x.html).
</div>

Unity 5 的 AssetBundle 系统会在编译完成后创建一个额外的 AssetBundle。这个额外的 AssetBundle 包括一个 AssetBundleManifest 对象。这个清单对象包含 AssetBundle 和它们的哈希值，可以用来给客户端传递有效的 AssetBundle 下载列表和版本信息。关于 AssetBundle manifest bundle，请参照 [Unity 手册](http://docs.unity3d.com/Manual/BuildingAssetBundles5x.html)。

<div style='display:none'>
It is also possible to write a custom system for detecting changes to AssetBundles. Most developers who write their own system choose to use an industry-standard data format for their AssetBundle file lists, such as JSON, and a standard C# class for computing checksums, such as MD5.
</div>

我们也可以写一个定制的系统来探测 AssetBundle 的改变。大部分写开发者写的系统都选择使用行业标准的数据结构作为他们的 AssetBundle 文件列表，比如 JSON，还有用来计算 checksum 的标准 C# 类，比如 MD5。

<div style='display:none'>
### 4.4.1. Differential patching

As of Unity 5, Unity can build AssetBundles with data ordered in a deterministic manner. This allows applications with custom downloaders to implement differential patching. To build AssetBundles with a deterministic layout, pass the [BuildAssetBundleOptions.DeterministicAssetBundle](http://docs.unity3d.com/ScriptReference/BuildAssetBundleOptions.DeterministicAssetBundle.html) flag when calling the BuildAssetBundles API. (See the scripting reference link for more details.)
</div>

### 增量更新

在 Unity 5 中，Unity 可以将数据按确定的顺序编译出 AssetBundle。这就允许定制下载器实现增量更新。要让 AssetBunle 按确定的布局编译，需要将 [BuildAssetBundleOptions.DeterministicAssetBundle](http://docs.unity3d.com/ScriptReference/BuildAssetBundleOptions.DeterministicAssetBundle.html) 标签传递给 BuildAssetBundles 函数。（更多详情请参照脚本参考的链接。）

<div style='display:none'>
Unity does not provide any built-in mechanism for differential patching and neither WWW.LoadFromCacheOrDownload nor UnityWebRequest perform differential patching when using the built-in Caching system. If differential patching is a requirement, then a custom downloader must be written.
</div>

Unity 没有提供内置的增量更新的机制，WWW.LoadFromCacheOrDownload 和 UnityWebRequest 使用内置的缓存系统也没有实现增量更新。如果一个系统中，增量更新是必须的，那么必须要写一个定制的下载器。

<div style='display:none'>
### 4.4.2. iOS On-Demand Resources
</div>

### iOS 中的按需加载资源

<div style='display:none'>
__On-Demand Resources__ is an Apple API for providing content to iOS and TVOS devices. It is available on iOS 9 devices. It is not currently a requirement for launching on the App Store, but is a launch requirement for TVOS apps.
</div>

__按需加载资源__ 是 Apple 为 iOS 和 TVOS 设备提供内容的 API。它在 App Store 发布 iOS app 不是必须的需求，但是在 TVOS app 中是必须的。

<div style='display:none'>
A general outline of Apple's On-Demand Resources system can be found on the[ Apple Developer site.](https://developer.apple.com/library/prerelease/ios/documentation/FileManagement/Conceptual/On_Demand_Resources_Guide/)
</div>

关于 Apple 的按需加载资源系统的资料可以从 [ Apple Developer site.](https://developer.apple.com/library/prerelease/ios/documentation/FileManagement/Conceptual/On_Demand_Resources_Guide/) 找到。

<div style='display:none'>
As of Unity 5.2.1, support for App Slicing and On-Demand Resources are both built upon another Apple system, Asset Catalogs. After registering a callback in the Unity Editor, the build pipeline for an iOS applications can report a set of files which will be automatically placed into Asset Catalogs and assigned specified On-Demand Resources tags.
</div>

Unity 5.2.1 中对 Apple 的应用分割和按需资源支持都是 Apple 的另外一个系统上构建，这个系统是 Asset Catalogs。在 Unity 编辑器中注册回调函数之后，iOS 的编译管道会给出被自动放到 Asset Catalogs 中并分配了按需资源标签的文件集合。

<div style='display:none'>
A new UnityEngine.iOS.OnDemandResources API provides runtime support for retrieving and caching On-Demand Resources files. Once resources have been retrieved via ODR, they can then be loaded into Unity via the standard AssetBundle.LoadFromFile API.
</div>

新的 API UnityEngine.iOS.PnDemandResources 提供了运行时获取和缓存按需资源文件的支持。一旦资源通过按需资源系统加载，它就可以通过标准的 API AssetBundle.LoadFromFile 加载进 Unity。

<div style='display:none'>
For more details and an example project, see [this Unity forum post](http://forum.unity3d.com/threads/second-preview-build-for-ios-9-on-demand-resources-and-app-slicing-support.353491/).
</div>

示例和更多的细节可以参照[这篇帖子](http://forum.unity3d.com/threads/second-preview-build-for-ios-9-on-demand-resources-and-app-slicing-support.353491/)。

<div style='display:none'>
## 4.5. Common pitfalls
</div>

## 常见陷阱

<div style='display:none'>
This section describes several problems that commonly appear in projects using AssetBundles.
</div>

这小节讲述了使用 AssetBundle 的项目常出现的几个问题。

<div style='display:none'>
### 4.5.1. Asset duplication
</div>

### 资产重复

<div style='display:none'>
Unity 5's AssetBundle system will discover all dependencies of an Object when the Object is built into an AssetBundle. This is done using the Asset Database. This dependency information is used to determine the set of Objects that will be included in an AssetBundle.
</div>

Unity 5 的 AssetBundle 系统会找出打包进 AssetBundle 的对象的所有依赖。这是 AssetDatabase 来完成的。依赖信息决定了打包进 AssetBundle 的对象集合。

<div style='display:none'>
Objects that are explicitly assigned to an AssetBundle will only be built into that AssetBundle. An Object is "explicitly assigned" when that Object's AssetImporter has its assetBundleName property set to a non-empty string. This can be done in the Unity Editor by selecting an AssetBundle in the Object's Inspector, or from Editor scripts.
</div>

对象被显式的分配到某个 AssetBundle 后它们只会被打包到那个 AssetBundle 中。对象被 “显式分配” 是对象的 AssetImpoter 的 assetBundleName 属性被设置为了非空字符串。这个行为可以在对象 Inspector 中选择 AssetBundle 或者通过编辑器脚本完成。

<div style='display:none'>
__Any Object that is not explicitly assigned in an AssetBundle will be included in all AssetBundles that contain 1 or more Objects that reference the untagged Object.__
</div>

__没有被显式分配到 AssetBundle 的对象会被打包到拥有一个或者多个没有标签的对象的 AssetBundle 中。__

<div style='display:none'>
If two different Objects are assigned to two different AssetBundles, but both have references to a common dependency Object, then that dependency Object will be copied into both AssetBundles. The duplicated dependency will also be instanced, meaning that the two copies of the dependency Object will be considered different Objects with a different identifiers. This will increase the total size of the application's AssetBundles. This will also cause two different copies of the Object to be loaded into memory if the application loads both of its parents.
</div>

如果两个不同的对象被分配到不同的 AssetBundle ，而它们都引用了共同依赖对象，然后这个共同的对象会被拷贝到每个 AssetBundle 中。重复的依赖对象会被实例化，这意味着这些依赖对象的拷贝会被认为是拥有不同标识不同对象。这会增加应用的 AssetBundle 的总大小。这也让加载这两个不同对象所在的 AssetBundle 时，它们会被加载进内存中。

<div style='display:none'>
There are several ways to address this problem:

1. Ensure that Objects built into different AssetBundles do not share dependencies. Any Objects which do share dependencies can be placed into the same AssetBundle without duplicating their dependencies.

    * This method usually is not viable for projects with many shared dependencies. It produces monolithic AssetBundles that must be rebuilt and re-downloaded too frequently to be convenient or efficient.
2. Segment AssetBundles so that no two AssetBundles that share a dependency will be loaded at the same time.

    * This method may work for certain types of projects, such as level-based games. However, it still unnecessarily increases the size of the project's AssetBundles, and increases both build times and loading times.
3. Ensure that all dependency assets are built into their own AssetBundles. This entirely eliminates the risk of duplicated assets, but also introduces complexity. The application must track dependencies between AssetBundles, and ensure that the right AssetBundles are loaded before calling any AssetBundle.LoadAsset APIs.
</div>

有几种方式来应付这种问题：

1. 确保被打包进 AssetBundle 中的不同对象不会有同样的依赖。任何跟其他对象没有共同依赖的对象都会打包到 AssetBundle  中，而不同重复拷贝依赖。
    * 这种方法对有很多共享依赖的项目不太合适。它会产生的巨大的 AssetBunle，而且这个 AssetBunle 必须频繁地重建和下载，不方便而又低效。
2. AssetBundle 分片，这样就不会同时有两个有共同依赖的 AssetBundle 会被加载
    * 这个方法可能只对某些项目管用，比如基于关卡的游戏。但是它会给项目增加不必要的 AssetBundle 大小和增加编译与加载时间。
3. 把所有的依赖都打包到依赖他们的 AssetBundle 中。这完全地排除了冗余资产的风险，但是它也引入了复杂性。应用程序必须 AssetBundle 间的依赖，来确保在调用 AssetBundle.LoadAsset API 前加载了正确的 AssetBundle。

<div style='display:none'>
In Unity 5, Object dependencies are tracked via the AssetDatabase API, located in the UnityEditor namespace. As the namespace implies, this API is only available in the Unity Editor and not at runtime.
</div>

Unity 5 中，对象的依赖是通过 AssetDatabase API 来跟踪的，这些 API 位于 UnityEditor 命名空间。就行命名空间名字所表明意思一样，这些 API 只有在 Unity 编辑器中可用，在运行时不可用

<div style='display:none'>
AssetDatabase.GetDependencies can be used to locate all of the immediate dependencies of a specific Object or Asset. Note that these dependencies may have their own dependencies. Additionally, the AssetImporter API can be used to query the AssetBundle to which any specific Object is assigned.
</div>

AssetDatabase.GetDependencies 可用来得到特定对象或者资产当前的依赖。注意得到的依赖可能还有它们自己的依赖。另外的，AssetImporter API 可用来查询 AssetBundle 被指派到了那些指定的对象上。

<div style='display:none'>
By combining the AssetDatabase and AssetImporter APIs, it is possible to write an Editor script that ensures that all of an AssetBundle's direct or indirect dependencies are assigned to AssetBundles, or that no two AssetBundles share dependencies that have not been assigned to an AssetBundle. Due to the memory cost of duplicating assets, it is recommended that all projects have such a script.
</div>

通过 AssetDatabase 和  AssetImporter API 的组合使用，让编程用来确保一个 AssetBundle 的所有直接或者间接的依赖都指派到了同一个 AssetBundle 上，或者不存在没有指派到 AssetBundle 的依赖被两个  AssetBundle 共享着。出于对重复资源内存消耗考虑，建议所有的项目都有这种的编辑器脚本。

<div style='display:none'>
### 4.5.2. Sprite atlas duplication
</div>

### 图集的冗余

<div style='display:none'>
The following sections describe a quirk of Unity 5's asset dependency calculation code when used in conjunction with automatically-generated sprite atlases. Unity 5.2.2p4 and Unity 5.3 have been patched to address this behavior.
</div>

下面小结介绍了 Unity 5 的资产依赖计算代码中，用于自动生成的图集结合的一种缺陷。Unity 5.2.4p4 和 Unity 5.3 已经对这个行为打了补丁。

<div style='display:none'>
#### Unity 5.2.2p4, 5.3 and newer
</div>

#### Unity 5.2.2p4，5.3 和更新版本

<div style='display:none'>
Any automatically-generated sprite atlas will be assigned to the AssetBundle containing the Sprite Objects from which the sprite atlas was generated. If the sprite Objects are assigned to multiple AssetBundles, then the sprite atlas will not be assigned to an AssetBundle and will be duplicated. If the Sprite Objects are not assigned to an AssetBundle, then the sprite atlas will also not be assigned to an AssetBundle.
</div>

所有自动生成的精灵图集所有对象都会指派到包含它们的 AssetBundle 中。如果这些对象被指派到多个 AssetBunle, 精灵对象会被复制多份，而不是只指派到一个 AssetBundle 中，并且精灵图集也不会只指派到一个 AssetBundle 中。

<div style='display:none'>
To ensure that sprite atlases are not duplicated, check that all sprites tagged into the same sprite atlas are assigned to the same AssetBundle.
</div>

为了确保精灵图集不会冗余，确保所有标在同一个图集中的精灵都指派到了同一个 AssetBundle 中。

<div style='display:none'>
#### Unity 5.2.2p3 and older
</div>

### Unity5.2.2p3 以及更老的版本

<div style='display:none'>
Automatically-generated sprite atlases will never be assigned to an AssetBundle. Because of this, they will be included in any AssetBundles containing their constituent sprites and also any AssetBundles referencing their constituent sprites.
</div>

在这些版本中，自动生成的精灵图集永远不会指派到 AssetBundle 中。因为这样，包含有组成这个图集的精灵对象的 AssetBundle 和引用了组成这个图集的精灵对象的 AssetBundle 都会包含这个图集。

<div style='display:none'>
Because of this problem, it is strongly recommended that all Unity 5 projects using Unity's sprite packer upgrade to Unity 5.2.2p4, 5.3 or any newer version of Unity.
</div>

因为这个问题，建议所有使用 Unity 的 Sprite Packer 的版本都生升级到 Uinty 5.2.2p4，5.4 或者更新的 Unity 版本。

<div style='display:none'>
For projects that cannot upgrade, there are two workarounds for this problem:
</div>

对于不能升级的项目，有两种临时解决方案：

<div style='display:none'>
1. Easy: Avoid using Unity's built-in sprite packer. Sprite atlases generated by external tools will be normal Assets, and can be properly assigned to an AssetBundle.
2. Hard: Assign all Objects that use automatically atlased sprites to the same AssetBundle as the sprites.
* This will ensure that the generated sprite atlas is not seen as the indirect dependency of any other AssetBundles and will not be duplicated.
* This solution preserves the simple workflow of using Unity's sprite packer, but it degrades developers' ability to separate Assets into different AssetBundles, and forces the re-download of an entire sprite atlas when any data changes on any component referencing the atlas, even if the atlas itself is unchanged.
</div>

1. 简单的方案：避免使用 Unity 的内置 Sprite Packer. 外部的打包工具生成的精灵图集是常的资产，可以正确的指派到 AssetBundle 中。
2. 难的方案：将所有使用了自动打图集的精灵的对象都指派到和精灵同一个 AssetBundle 中
    * 这可以确保生成的精灵图集对于非直接的依赖的 AssetBundle 不可见，也不会有冗余
    * 这个方案解决了使用 Unity Sprite Packer 的简单流程，但是它让开发者不能讲分配资产到不同的 AssetBundle 中，并且引用了这个图集的组件上的任何数据变动都要强制重新下载整个精灵图集，即使图集自己没有任何变动。

<div style='display:none'>
### 4.5.3. Android textures
</div>

### 安卓的纹理

<div style='display:none'>
Due to heavy device fragmentation in the Android ecosystem, it is often necessary to compress textures into several different formats. While all Android devices support ETC1, ETC1 does not support textures with alpha channels. Should an application not require OpenGL ES 2 support, the cleanest way to solve the problem is to use ETC2, which is supported by all Android OpenGL ES 3 devices.
</div>

由于安卓生态中设备的碎片化特别严重，常常我们需要将纹理压缩成好几种格式。所有的安卓设备都支持 ETC1, 而 ETC1 不支持 alpha 通道。在不是必须要求使用 OpenGL ES 2 支持的设备上，最彻底简便的解决这个问题方法就是使用 ETC2 格式，这个格式被所有使用 OpenGL ES 3 的安卓设备支持。

<div style='display:none'>
Most applications need to ship on older devices where ETC2 support is unavailable. One way to solve this problem is with Unity 5's AssetBundle Variants. (Please see Unity's Android optimization guide for details on other options.)
</div>

如果很多应用程序需要在不支持 ETC2 的老设备支持。一个解决这个问题的方法就是使用 Unity 5 的 AssetBundle 变体。（更多设置详情请查看 Unity 的安卓优化指导。）

<div style='display:none'>
To use AssetBundle Variants, all textures that cannot be cleanly compressed using ETC1 must be isolated into texture-only AssetBundles. Next, create sufficient variants of these AssetBundles to support the non-ETC2-capable slices of the Android ecosystem, using vendor-specific texture compression formats such as DXT5, PVRTC and ATITC. For each AssetBundle Variant, change the included textures' TextureImporter settings to the compression format appropriate to the Variant.
</div>

为了使用 AssetBundle 变体，所有不能使用 ETC1 的纹理多要被隔离到只包含纹理的 AssetBunld 中。然后为非 ETC2 设备创建主变种，并使用第三方纹理压缩格式，比如 DXT5, PVRTC 和 ATITC。对于每个 AssetBundle 变种，改变包含的纹理的 TextureImporter 设置来改变为变种对应的格式。

<div style='display:none'>
At runtime, support for the different texture compression formats can be detected using the [SystemInfo.SupportsTextureFormat](http://docs.unity3d.com/ScriptReference/SystemInfo.SupportsTextureFormat.html) API. This information should be used to select and load the AssetBundle Variant containing textures compressed in a supported format.
</div>

在运行时，不同纹理压缩格式可以用 [SystemInfo.SupportsTextureFormat](http://docs.unity3d.com/ScriptReference/SystemInfo.SupportsTextureFormat.html) API 来探测到。这个信息应该用来选择和加载其所支持纹理格式的AssetBundle 变种。

<div style='display:none'>
### 4.5.4. iOS file handle overuse
</div>

### iSO 文件句柄过度使用

<div style='display:none'>
The issue described in the following section was fixed in Unity 5.3.2p2. Current versions of Unity are not affected by this issue.
</div>

下面描述的问题已经在 Unity 5.3.2p2 中修复，当前版本的 Unity 并不受其影响

<div style='display:none'>
In versions prior to Unity 5.3.2p2, Unity would hold an open file handle to an AssetBundle the entire time that the AssetBundle is loaded. This is not a problem on most platforms. However, iOS limits the number of file handles a process may simultaneously have open to 255. If loading an AssetBundle causes this limit to be exceeded, the loading call will fail with a "Too Many Open File Handles" error.
</div>

在 Unity 5.3.2p2 之前，Unity 会在整个周期内保持对已加载过的 AssetBundle 的文件句柄的占用。这个对大多数平台不算大问题。但是 iOS 限制了并行的文件句柄数量最大为 255。 如果超过这个数量时加载 AssetBundle, 加载的调用会失败，并抛出 "打开文件句柄太多" 错误。

<div style='display:none'>
This was a common problem for projects trying to divide their content across many hundreds or thousands of AssetBundles.
</div>

这对那些把内容拆分到上百甚至上千个 AssetBundle 的项目算是比较常见的问题。

<div style='display:none'>
For projects unable to upgrade to a patched version of Unity, temporary solutions are:
</div>

对于没法升级 Unty 补丁版本的 Unity, 有两个临时解决方案可以用：

<div style='display:none'>
* Reducing the number of AssetBundles in use by merging related AssetBundles
* Using AssetBundle.Unload(false) to close an AssetBundle's file handle, and managing the loaded Objects' lifecycles manually
</div>

* 合并相关的 AssetBundle 来减少 AssetBundle 的数量
* 使用 AssetBundle.Unload(false) 关闭文件句柄，并手动的管理加载的对象的生命周期

<div style='display:none'>
## 4.6. AssetBundle Variants
</div>

## AssetBunle 变体

<div style='display:none'>
A key feature of Unity 5's AssetBundle system is the introduction of AssetBundle Variants. The purpose of Variants is to allow an application to adjust its content to better suit its runtime environment. Variants permit different UnityEngine.Objects in different AssetBundle files to appear as being the "same" Object when loading Objects and resolving Instance ID references. Conceptually, it permits two UnityEngine.Objects to appear to share the same File GUID & Local ID, and identifies the actual UnityEngine.Object to load by a string Variant ID.
</div>

Unity 5 AssetBundle 系统关键的一个功能就是引入了 AssetBundle 变体。变体的目的是允许应用可以调整他们的内容来更适用于运行环境。它可以让不同 AssetBundle 中的不同 UnityEngine.Objects 对象在加载和引用处理的时候表现的像 “同一个” 对象一样。从概念上来讲，它允许两个不同的 UnityEngine.Objects 对象表现为共享了相同的文件 GUID 和 本地 ID，然后通过变体 ID 来断定实际要加载的 UnityEngine.Object 对象。

<div style='display:none'>
There are two primary use cases for this system:
</div>

这个系统有两个主要的用途：

<div style='display:none'>
1. Variants simplify the loading of AssetBundles appropriate for a given platform.

    * Example: A build system might create an AssetBundle containing high-resolution textures and complex shaders suitable for a standalone DirectX11 Windows build, and a second AssetBundle with lower-fidelity content intended for Android. At runtime, the project's resource loading code can then load the appropriate AssetBundle Variant for its platform, and the Object names passed into the AssetBundle.Load API do not need to change.

2. Variants allow an application to load different content on the same platform, but with different hardware.
* This is key for supporting a wide range of mobile devices. An iPhone 4 is incapable of displaying the same fidelity of content as an iPhone 6 in any real-world application.
* On Android, AssetBundle Variants can be used to tackle the immense fragmentation of screen aspect ratios and DPIs between devices.
</div>

1. 变体简化了平台对应 AssetBundle 的加载。
    * 例子：编译系统可能创建了一个适用于 DirectX11 Windows Standalone 程序 的AssetBundle， 它包含高分辨率纹理和复杂的 Shader，然后另外一个给 Android 平台的低质量的 AssetBundle。在运行期，项目资源加载代码可以根据运行的平台加载对应的 AssetBundle 变体，而不用改变传递给 AssetBundle.Load API 的名字。
2. 变体可以让应用在相同平台上为不同的硬件加载不同的内容。
    * 这是支持大范围移动设备的关机。在真实世界中应用 iPhone4 显示 iPhone6 质量的内容会比较吃力
    * 在 Android 上，AssetBundle 变体可以用来处理不同设备间屏幕分辨率和 DPI 碎片化严重的问题

<div style='display:none'>
### 4.6.1. Limitations
</div>

### AssetBundle 变体限制

<div style='display:none'>
A key limitation of the AssetBundle Variant system is that it requires Variants to be built from distinct Assets. This limitation applies even if the only variations between those Assets is their import settings. If the only distinction between a texture built into Variant A and Variant B is the specific texture compression algorithm selected in the Unity texture importer, Variant A and Variant B must still be entirely different Assets. This means that Variant A and Variant B must be separate files on disk.
</div>

AssetBunble 变体系统的主要限制是要求变体需要从不同的资产中编译出来。即使只有导入设置的改变也受这个限制影响。如果一个纹理需要打包进变体 A 和变体 B 中，两个变体中这个纹理的唯一差别是导入设置中的压缩算法不同，这种情况下，变体 A 和变体 B 必须要求是完全不同的资产，意味着必须是磁盘上独立分开的文件。

<div style='display:none'>
This limitation complicates the management of large projects as multiple copies of a specific Asset must be kept in source control. All copies of an Asset must be updated when developers wish to change the content of the Asset.
</div>

这个限制会导致在版本管理中同一个资产可能会有多份拷贝，增加了大项目的管理复杂度。而且如果开发者要更新资产的内容时，所有这些拷贝也要更新。

<div style='display:none'>
There are no built-in workarounds for this problem.
</div>

针对这个问题，现在还没有内置的临时解决方案。

<div style='display:none'>
Most teams implement their own form of AssetBundle Variants. This is done by building AssetBundles with well-defined suffixes appended to their filenames, in order to identify the specific variant a given AssetBundle represents. Custom code programmatically alters the importer settings of the included Assets when building these AssetBundles. Some developers have extended their custom systems to also be able to alter parameters on components attached to prefabs.
</div>

大部分团队会有他们自己的 AssetBundle 变种方式。通常靠将定义好的后缀加入到编译的 AssetBundle 文件名中，用来区分不同的变体。然后用代码在打包这些 AssetBundle 时修改资产的导入设置。也有些开发会扩展他们定制的系统，让其能修改预设上的组件的参数。

<div style='display:none'>
## 4.7. Compressed or uncompressed?
</div>

## 压缩还是不压缩

<div style='display:none'>
Whether to compress AssetBundles or not requires careful consideration. The important questions are:
</div>

是否要压缩 AssetBundle 需要仔细的考虑，重点问题有几个：

<div style='display:none'>
* Is an AssetBundle's __loading time__ a critical factor? Uncompressed AssetBundles are much faster to load than compressed AssetBundles when loading from local storage or a local cache. Downloading compressed AssetBundles from a remote server is usually faster than downloading an uncompressed AssetBundle.
* Is an AssetBundle's __build time__ a critical factor? LZMA and LZ4 are very slow when compressing files, and the Unity Editor processes AssetBundles in serial. Projects with a large number of AssetBundles will spend a lot of time compressing them.
* Is __the application's size__ a critical factor? If the AssetBundles are shipped in the application, compressing them will reduce the application's total size. Alternatively, the AssetBundles can be downloaded post-install.
* Is __memory usage__ a critical factor? Prior to Unity 5.3, all of Unity's decompression mechanisms required the entire compressed AssetBundle to be loaded into memory prior to decompression. If memory usage is important, use either uncompressed or LZ4 compressed AssetBundles.
* Is __download time__ a critical factor? Compression may only be necessary if the AssetBundles are large, or if users are in a bandwidth-constrained environment, such as downloading via 3G on mobile, or on low-speed or metered connections. If only a few tens of megabytes of data are being delivered to PCs on high-speed connections, it may be possible to omit compression.
</div>

* __加载时间__ 是不是这个 AssetBundle 的主要因数？从磁盘或缓存中加载没有压缩的 AssetBundle 会比压缩的 AssetBundle 快很多。但是通常从服务器上下载一个压缩的文件会比一个未压缩的 AssetBundle 快。
* __编译时间__ 是不是这个 AssetBundle 的主要因数？LZMA 和 LZ4 在压缩式很慢，并且 Unity 编辑器会序列化 AssetBundle。有很多 AssetBundle 的项目会在压缩上花费很长的时间。
* __程序大小__ 是不是主要因数？如果 AssetBundle 是跟程序一起发布，压缩他们会减少包体的大小。另外 AssetBundle 可以在程序安装后安装。
* __内存使用__ 是不是主要因数？在 Unity 5.3 之前，所有 Unity 的解压机制都要求解压前将整个 AssetBundle 都加载到内存中。如果内存使用率比较重要，请使用 LZ4 压缩 AssetBundles 或者不压缩 AssetBundle。
* __下载时间__ 是不是主要因数？压缩仅在 AssetBundle 比较大或者用户在带宽有限的环境中才需要，比如移动端通过 3G 下载或者在低速连接中。如果只有几十 M 的数据需要传输到 PC 或者在高速连接中，可以把压缩去掉。

<div style='display:none'>
## 4.8. AssetBundles and WebGL
</div>

## AssetBundle 和 WebGL

<div style='display:none'>
Unity strongly recommends that developers not use compressed AssetBundles on WebGL projects.
</div>

Unity 强烈推荐开发者在 WebGL 项目上不压缩 AssetBundle。

<div style='display:none'>
As of Unity 5.3, all AssetBundle decompression and loading in a WebGL project must occur on the main thread. This is because Unity 5.3's WebGL export option does not currently support worker threads. (The downloading of AssetBundles is delegated to the browser via the XMLHttpRequest Javascript API, and will occur off of Unity's main thread.) This means that compressed AssetBundles are extremely expensive to load on WebGL.
</div>

Unity 5.3 中所有的 AssetBundle 解压和加载在 WebGL 项目中都发生在主线程之上。这是因为 Unity 5.3 的 WebGL 导出选项不支持工作线程。（AssetBundle 的下载通过 Javascript 的 XMLHttpRequest API 代理给了浏览器，不是在主线程中。）这意味着在 WebGL 中加载压缩的 AssetBundle 开销比较昂贵。

<div style='display:none'>
With this in mind, you may want to avoid using the default LZMA Format for your AssetBundles and compress using LZ4 instead, which is decompressed very efficiently on-demand. If you need smaller compression sizes then LZ4 delivers, you can configure your web server to gzip-compress the files on the http protocol level (on top of LZ4 compression).
</div>

知道了这些，你能会想到使用解压很高效的 LZ4 压缩来避免 LZMA 压缩格式。如果你需要传输比 LZ4 更小的压缩大小，你可以通过配置 Web 服务器在 Http 协议层中使用 gzip 压缩文件（在 LZ4 压缩之上使用）。