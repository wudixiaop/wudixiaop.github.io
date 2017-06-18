title: AssetBundle 使用模式 (1)
date: 2017-04-18 12:30
category: UnityKB
tags: AssetBundle
---------

<div style='display:none'>
This is the fifth chapter in a [series of articles covering Assets, Resources and resource management](https://unity3d.com/cn/learn/tutorials/topics/best-practices/guide-asset-bundles-and-resources) in Unity 5.
</div>

这是 Unity 5 {% post_link GuideToABAndRes [资产, 资源和资源管理系列文章] %} 的第五篇。（译者注：原文太长，我拆分成了两部分，这是第一部分。）

<div style='display:none'>
The previous chapter in this series covered the [fundamentals of AssetBundles](https://unity3d.com/cn/learn/tutorials/topics/best-practices/asset-bundle-fundamentals), in particular the low-level behavior of various loading APIs. This chapter discusses problems and potential solutions to various aspects of using AssetBundles in practice.
</div>

上一篇文章涵盖了 {% post_link AssetBundle_Fundamentals [AssetBundle 基本知识] %}，特别是多种加载用的 API 的底层行为。这篇会讨论真实使用 AssetBundle 碰到的问题和可能的解决方案。

<div style='display:none'>
### 4.1. Managing loaded Assets
</div>

### 管理加载后的资产

<div style='display:none'>
It is particularly critical to carefully control the size and number of loaded Objects in memory-sensitive environments. Unity does not automatically unload Objects when they are removed from the active scene. Asset cleanup is triggered at specific times, and it can also be triggered manually.
</div>

在性能要求高的环境中，要特别严格地，小心翼翼地控制加载的对象的数量和大小。当对象从当前场景中移除时，Unity 不会自动的卸载他们。资产的清理是在特殊的时间触发，当然它也可以手动来触发。

<div style='display:none'>
AssetBundles themselves must be carefully managed. An AssetBundle backed by a file on local storage (either in the Unity cache or one loaded via [AssetBundle.LoadFromFile](http://docs.unity3d.com/ScriptReference/AssetBundle.LoadFromFile.html)) has minimal memory overhead, rarely more than 10-40 kilobytes. This overhead can still become problematic when a large number of AssetBundles are present.
</div>

AssetBundle 必须要仔细的管理。来自本地存储文件的 AssetBundle（不管是从缓存或者是通过 [AssetBundle.LoadFromFile](http://docs.unity3d.com/ScriptReference/AssetBundle.LoadFromFile.html)加载的) 会有最小内存开销，一般不超过 10-40 kb。当存在大量 AssetBundle 时，这种开销仍然可能成为问题。

<div style='display:none'>
As most projects allow users to re-experience content (such as replaying a level), it's important to know when to load or unload an AssetBundle. __If an AssetBundle is unloaded improperly, it can cause Object duplication in memory__. Improperly unloading AssetBundles can also result in undesirable behavior in certain circumstances, such as causing textures to go missing. To understand why this can happen, refer to the [Inter-Object references](https://unity3d.com/cn/learn/tutorials/topics/best-practices/assets-objects-and-serialization#InterObject_References) section of the [Assets, Objects, and serialization](https://unity3d.com/cn/learn/tutorials/topics/best-practices/assets-objects-and-serialization) chapter.
</div>

大多数项目都允许用户对内容再次体验（比如重新玩一个关卡），知道什么时候加载和卸载 AssetBundle 是很重要的。__如果一个 AssetBundle 被错误卸载，可能会引起内存中对象重复__。错误卸载也可以在某些情况下引起不希望的结果，比如引起纹理丢失。要理解为什么这个会发生，请参照 {% post_link Assets_Objects_serialization [资产，对象和序列化] %} 章节的 __内部对象引用__ 小结。

<div style='display:none'>
The most important thing to understand when managing assets and AssetBundles is the difference in behavior when calling [AssetBundle.Unload](http://docs.unity3d.com/ScriptReference/AssetBundle.Unload.html) with either a true or false argument.
</div>

要理解何时去管理资产和 AssetBunle，最重要的是理解调用 [AssetBundle.Unload](http://docs.unity3d.com/ScriptReference/AssetBundle.Unload.html) 的不同行为，不管其参数是 true 还是 false.

<div style='display:none'>
This API unloads the header information of the AssetBundle being called. The argument indicates whether to also unload all Objects instantiated from this AssetBundle. If it is true, then all Objects originating from the AssetBundle will also be immediately unloaded - even if they are currently being used in the active scene.
</div>

<!-- more -->

这个 API 会卸载正在调用的 AssetBundle 头信息。参数意思是是否也卸载从这个 AssetBundle 加载的对象实例。如果是 true, 所有从这个 AssetBundle 实例化的对象会立即被卸载，即使它们被当前场景使用着。

<div style='display:none'>
For example, assume a material M was loaded from an AssetBundle AB, and assume M is currently in the active scene.
</div>

例如，假设材质 M 是从 AssetBundle AB 中加载的，并且当前场景正使用着材质 M。

![description](https://unity3d.com/sites/default/files/ab2a.jpg)

<div style='display:none'>
If AB.Unload(true) is called, then M will be removed from the scene, destroyed and unloaded. However, if AB.Unload(false) is called, then AB's header information will be unloaded but M will remain in the scene and will still be functional. Calling AssetBundle.Unload(false) breaks the link between M and AB. If AB is loaded again later, then fresh copies of the Objects contained in AB will be loaded into memory.
</div>

如果 AB.Unload(true) 被调用了，M 也会从当前场景中删除，销毁和卸载。如果 AB.Unload(false) 被调用了，AB 的头信息会被卸载，但是材质 M 依然在当前场景中并且可用。调用 AssetBundle.Unload(false) 会打破 M 和 AB 直接的关联。如果稍后再次加载 AB，则 AB 中包含的对象的新副本将被加载到内存中。

![description](https://unity3d.com/sites/default/files/ab2b.jpg)

<div style='display:none'>
If AB is loaded again later, then a new copy of the AssetBundle's header information will be reloaded. However, M was not loaded from this new copy of AB. Unity does not establish any link between the new copy of AB and M.
</div>

如果稍后再次加载 AB, 将会加载一个新的 AB Header 信息的副本。但是 M 不是从 AB 新副本中加载的。Unity 不会为 M 和新的 AB 拷贝间建立新的关系链接。

![description](https://unity3d.com/sites/default/files/ab2c.jpg)

<div style='display:none'>
If AB.LoadAsset() were called to reload M, Unity would not interpret the old copy of M as being an instance of the data in AB. Therefore, Unity will load a new copy of M and there will be __two__ identical copies of M in the scene.
</div>

如果调用 AB.LoadAsset() 来重新加载 M, Unity 不会把 M 的旧副本解析为 AB 的数据的实例。所以，Unity 会重新加载一个 M 的副本，这时场景中就会有两个完全相同的 M 的副本。

![description](https://unity3d.com/sites/default/files/ab2d.jpg)

<div style='display:none'>
For most projects, this behavior is undesirable. Most projects should use AssetBundle.Unload(true) and adopt a method to ensure that Objects are not duplicated. Two common methods are:

1. Having well-defined points during the application's lifetime at which transient AssetBundles are unloaded, such as between levels or during a loading screen. This is the simpler and most common option.
2. Maintaining reference-counts for individual Objects and unload AssetBundles only when all of their constituent Objects are unused. This permits an application to unload & reload individual Objects without duplicating memory.
</div>

大多数项目中，这种行为是不可取的。大多数项目应该使用 AssetBundle.Unload(true) 并且使用方法确保对象不会有重复副本。有两种通用的方法：

1. 在应用生命周期中，临时 AssetBundle 卸载有明确定义的点，比如两个关卡之间或者加载场景的时候。这个比较简单，也是使用最多的情况
2. 维护单个物体的引用计数，并当组成 AssetBundle 的对象都未被使用时卸载 AssetBundle。这允许应用卸载和重新加载对象而不会复制多余的内存。

<div style='display:none'>
If an application must use AssetBundle.Unload(false), then individual Objects can only be unloaded in two ways:

* Eliminate all references to an unwanted Object, both in the scene and in code. After this is done, call [Resources.UnloadUnusedAssets](http://docs.unity3d.com/ScriptReference/Resources.UnloadUnusedAssets.html).
* Load a scene non-additively. This will destroy all Objects in the current scene and invoke Resources.UnloadUnusedAssets automatically.
</div>

如果应用必须使用 AssetBundle.Unload(false), 则单个对象能通过下面两种方式卸载：

* 在场景和代码中删除不需要对象的所有引用。完成之后调用 [Resources.UnloadUnusedAssets](http://docs.unity3d.com/ScriptReference/Resources.UnloadUnusedAssets.html)
* 非增量方式加载场景。这个行为会卸载当前场景中的所有对象，然后自动的调用 Resources.UnloadUnusedAssets()

<div style='display:none'>
If a project has well-defined points where the user can be made to wait for Objects to load and unload, such as in between game modes or levels, these points should be used to unload as many Objects as necessary and to load new Objects.
</div>

如果一个项目中有明确定义的点，那它可以用来等待对象的加载和卸载，比如游戏模式和关卡之间，那么在这些点应该尽可能多的卸载对象和加载新的对象。

<div style='display:none'>
The simplest way to do this is to package discrete chunks of a project into scenes, and then build those scenes into AssetBundles, along with all of their dependencies. The application can then enter a "loading" scene, fully unload the AssetBundle containing the old scene, and then load the AssetBundle containing the new scene.
</div>

最简单的方法是将项目中离散快打包到场景中，然后把场景和所有依赖打包到 AssetBundle 中。这个应用可以进入一个 "加载" 场景，在这个场景中完全卸载包含旧场景的 AssetBundle ， 然后加载包含新场景的 AssetBundle。

<div style='display:none'>
While this is the simplest flow, some projects require more complex AssetBundle management. There is no universal AssetBundle design pattern. Each project's data is different. When deciding how to group Objects into AssetBundles, it is generally best to start by bundling Objects into AssetBundles if they must be loaded or updated at the same time.
</div>

这只是一个简单的流程，有些项目需要更复杂的 AssetBundle 管理。现在还没有通过的 AssetBundle 设计模式。每个项目的数据都是有区别的。当决定如何把对象分组进 AssetBundle 时候，通常最好的做法是打包需要同时加载或者卸载的对象进同一个 AssetBundle。

<div style='display:none'>
For example, consider a role-playing game. Individual maps and cutscenes can be grouped into AssetBundles by scene, but some Objects will be needed in most scenes. AssetBundles could be built to provide portraits, the in-game UI, and different character models and textures. These latter Objects and Assets could then be grouped into a second set of AssetBundles that are loaded at startup and remain loaded for the lifetime of the app.
</div>

例如，对于一个角色扮演游戏。单个地图和过场动画可以按场景分组到 AssetBundle 中，但是有一些对象在大多数场景中使用。AssetBundle 可以用于提供肖像，游戏中 UI, 不同的角色模型和纹理。这些后面的对象和资产可以被分组成在启动时加载的第二组 AssetBundle 并且在应用程序的生命周期保持加载状态。

<div style='display:none'>
Another problem can arise if Unity must reload an Object from its AssetBundle after the AssetBundle has been unloaded. In this case, the reload will fail and the Object will appear in the Unity Editor's hierarchy as a (Missing) Object.
</div>

如果 Unity 必须重新从已经卸载的 AssetBundle 中加载对象，还有一种问题会出现。这种情况是, 对象加载失败，对象在 Unity 编辑器的 Hierarchy 中显示为（Missing）。

<div style='display:none'>
This primarily occurs when Unity loses and regains control over its graphics context, such as when a mobile app is suspended or the user locks their PC. In this case, Unity must re-upload textures and shaders to the GPU. If the source AssetBundle for these assets is unavailable, the application will render Objects in the scene with "missing shader" magenta.
</div>

这主要发生在 Unity 丢失和拿回它的图形上下文控制权时，比如一个移动应用被挂起或者用户 PC 端锁屏。在这种情况下，Unity 必须给 GPU 重新上传纹理和 shader。如果上传的资产的源 AssetBundle 不可用，应用就会将场景中的对象显示成丢失 Shader 的洋红色的对象。

<div style='display:none'>
### 4.2. Distribution
</div>

### 部署

<div style='display:none'>
There are two basic ways to distribute a project's AssetBundles to clients: installing them simultaneously with the project or downloading them after installation. The decision whether to ship AssetBundles within or after installation is driven by the capabilities and restrictions of the platform(s) on which the project will run. Mobile projects usually opt for post-install downloads to reduce initial install size and remain below over-the-air download size limits. Console and PC projects generally ship AssetBundles with their initial install.
</div>

有两种基本的方式可以将项目的 AssetBundle 部署到终端：跟项目一起安装或者项目安装之后下载。是一起安装还是之后安装的决策依赖于项目目标平台的能力和限制。移动端项目通常采用安装后下载来达到减少初始安装大小, 并且保持低于无线下载大小限制。控制台和 PC 项目一部是采用 AssetBundle 跟初始安装一起。

<div style='display:none'>
Proper architecture permits patching new or revised content into your project post-install regardless of how the AssetBundles are delivered initially. For more information on this, see the [Patching with AssetBundles](https://unity3d.com/cn/learn/tutorials/topics/best-practices/assetbundle-usage-patterns#Patching_with_Asset_Bundles) section of this article.
</div>

好的架构可以在跟初始安装无关的情况下，安装之后在项目中新加或者修改内容。更多的信息请参照这章中的 __为 Assetbunlde 打补丁__ 小节。

<div style='display:none'>
### 4.2.1. Shipped with project
</div>

### 随项目一起打包

<div style='display:none'>
Shipping AssetBundles with the project is the simplest way to distribute them as it does not require additional download-management code. There are two major reasons why a project might include AssetBundles with the install:
</div>

AssetBundle 跟随项目一起打包是部署他们的最简单的方式，因为不需要额外的下载管理代码。为什么一个项目需要将 AssetBunle 打包在一起，下面有两个主要的原因：

<div style='display:none'>
* To reduce project build times and permit simpler iterative development. If these AssetBundles do not need to be updated separately from the application itself, then the AssetBundles can be included with the application by storing the AssetBundles in Streaming Assets. See the [Streaming Assets](https://unity3d.com/cn/learn/tutorials/topics/best-practices/assetbundle-usage-patterns#Distribution_Streaming_Assets) section, below.
* To ship an initial revision of updatable content. This is commonly done to save end-users time after their initial install or to serve as the basis for later patching. Streaming Assets is not ideal for this case. However, if writing a custom downloading and caching system is not an option, then an initial revision of updatable content can be loaded into the [Unity cache from Streaming Assets](https://unity3d.com/cn/learn/tutorials/topics/best-practices/assetbundle-usage-patterns#Cache_Priming).
</div>

* 减少项目构建时间和允许更简单的迭代开发。如果 AssetBundle 不需要独立于程序本身独立更新，程序可以将 AssetBundle 放置于 StreamingAssets 中。参考下面的 [Streaming Assets](https://unity3d.com/cn/learn/tutorials/topics/best-practices/assetbundle-usage-patterns#Distribution_Streaming_Assets) 小结。
* 为可以更新的内容提供一个初始版本。这通常是为最终用户初始安装之后节省时间或者作为一个后期更新的基础版本。Streaming Assets 在这种情况下不是好的选择。如果写一个定制的下载和缓存系统是必须的话，那么可以更新内容的基础版本可以从 [Streaming Assets 的 Unity 缓存](https://unity3d.com/cn/learn/tutorials/topics/best-practices/assetbundle-usage-patterns#Cache_Priming) 中加载。

<div style='display:none'>
#### 4.2.1.1. Streaming Assets
</div>

#### Streaming Assets

<div style='display:none'>
The easiest way to include any type of content within a Unity application at install time is to build the content into the __/Assets/StreamingAssets/__ folder, prior to building the project. Anything contained in the StreamingAssets folder at build time will be copied into the final application. This folder can be used to store any type of content within the final application, not just AssetBundles.
</div>

在 Unity 程序安装时包括各种类型内容的最简单的方法，是在构建项目之前将内容构建入 __/Assets/StreamingAssets/__ 文件夹内。所有在 StreamingAssets 文件夹内的文件都会在项目构建的时候被拷贝到最终程序包里。StreamingAssets 文件夹可以用来存储最终程序包内的各种内容，而不仅仅是 AssetBundle。

<div style='display:none'>
The full path to the StreamingAssets folder on local storage is accessible via the property [Application.streamingAssetsPath](http://docs.unity3d.com/ScriptReference/Application-streamingAssetsPath.html) at runtime. The AssetBundles can then be loaded with via AssetBundle.LoadFromFile on most platforms.
</div>

StreamingAssets 文件夹在本地存储中的全路径，可以在运行期时通过属性 [Application.streamingAssetsPath](http://docs.unity3d.com/ScriptReference/Application-streamingAssetsPath.html) 得到。AssetBundle 之后在大多数平台上都可以通过 AssetBundle.LoadFromFile 来加载。

<div style='display:none'>
Android Developers: On Android, Application.streamingAssetsPath will point to a compressed .jar file, even if the AssetBundles are compressed. In this case, WWW.LoadFromCacheOrDownload must be used to load each AssetBundle. It is also possible to write custom code to decompress the .jar file and extract the AssetBundle to a readable location on local storage.
</div>

__给安卓开发者：__ 在安卓平台上， Application.streamingAssetsPath 指向的是一个压缩的 .jar 文件，即使 AssetBundle 已经被压缩过了。在这种情况下，必须使用 WWW.LoadFromCacheOrDownload 加载每个 AssetBundle。当然可以写代码去解压 .jar file，然后将 AssetBundle 提取到一个可以读的本地存储上。

<div style='display:none'>
Note: Streaming Assets is not a writable location on some platforms. If a project's AssetBundles need to be updated after installation, either use __WWW.LoadFromCacheOrDownload__ or write a custom downloader. See the [Custom downloaders - storage ](https://unity3d.com/cn/learn/tutorials/topics/best-practices/assetbundle-usage-patterns#Custom_Downloaders_Storage)section for more details.
</div>

__注意：__ StreamingAssets 在一些平台上是不可写的。如果一个项目的 AssetBundle 需要在安装之后更新，可以使用 __WWW.LoadFromCacheOrDownload__ 或者写一个定制的下载器。更多详情请参照 [Custom downloaders - storage ](https://unity3d.com/cn/learn/tutorials/topics/best-practices/assetbundle-usage-patterns#Custom_Downloaders_Storage) 小结里面。

<div style='display:none'>
### 4.2.2. Downloaded post-install
</div>

### 安装之后下载

<div style='display:none'>
The favored method of delivering AssetBundles to mobile devices is to download the Bundles after app installation. This also allows the content to be updated with new or refined content after installation without forcing users to re-download the entire application. On mobile platforms, application binaries must undergo an expensive and lengthy re-certification process. Therefore, developing a good system for post-install downloads is vital.
</div>

将 AssetBundle 交付到移动设备上的首选方式是在应用安装完之后下载。内容可以再在应用安装后，用户不需要重新下载整个应用的情况下新加或者修改。在移动平台上，应用文件需要进过昂贵并且长时间的认证过程。所以一个安装后下载的系统是必不可少的。

<div style='display:none'>
The simplest way to deliver AssetBundles is to place them on a web server and deliver them via WWW.LoadFromCacheOrDownload or UnityWebRequest. Unity will automatically cache downloaded AssetBundles on local storage. If the downloaded AssetBundle is LZMA compressed, the AssetBundle will be stored in the cache uncompressed for faster loading in the future. If the downloaded bundle is LZ4 compressed, the AssetBundle will be stored compressed.
</div>

最简单地交付 AssetBundle 是将它们放到一个网络服务器上，然后通过 WWW.LoadFromCacheOrDownload 或者 UnityWebRequest 来下载它们。Unity 会在本地存储上自动的缓存已下载的 AssetBundle。如果下载的 AssetBundle 是 LZMA 压缩格式，为了之后更快的加载，它会以未压缩格式存储在缓存中。如果下载的 AssetBundle 是 LZ4 压缩格式，则会保持压缩格式存储在缓存中。

<div style='display:none'>
If the cache fills up, Unity will remove the least recently used AssetBundle from the cache. See the Built-in caching section for more details.
</div>

如果缓存满了，Unity 会将最近最少使用的 AssetBundle 从缓存中移除。更多详情请参照 __内建缓存__ 小节。

<div style='display:none'>
Please note that __WWW.LoadFromCacheOrDownload__ is flawed. As described in the Loading AssetBundles section, the WWW object consumes an amount of memory equal in size to an AssetBundle's data while downloading it. This can lead to unacceptable memory spikes. There are three ways to avoid this:
</div>

注意 __WWW.LoadFromCacheOrDownload__ 是有瑕疵的。就如在加载 AssetBundle 小节中所说，WWW 对象下载的时候会消耗跟 AssetBundle 数据的大小一样的内存。这会导致意想不到的内存尖峰。有三种方法可以避免这种情况：

<div style='display:none'>
* Keep AssetBundles small. The maximum size of an AssetBundle will be determined be a project's memory budget when the Bundle is being downloaded. Applications with "downloading" screens can usually allocate more memory to downloading AssetBundles than applications streaming the AssetBundles in the background.
* If using Unity 5.3 or newer, switch to using the new UnityWebRequest API's DownloadHandlerAssetBundle, which does not cause memory spikes during downloads.
* Write a custom downloader. For more information, see the Custom downloaders section.
</div>

* 使用小尺寸 AssetBundle。AssetBundle 下载过程中，项目内存预算值决定了下载的 AssetBundle 的最大值。有 “加载中” 界面的应用可分配用来下载 AssetBundle 的内存通常会比在后台读写 AssetBundle 的多。
* 如果是 Unity 5.3 或者更新版本，使用新的 UnityWebRequest API 的 DownloadHandlerAssetBundle，这个不会引起内存尖峰
* 定制一个下载器。更多的信息，可以参照定制下载器小节

<div style='display:none'>
It is generally recommended to start by using UnityWebRequest when possible, or __WWW.LoadFromCacheOrDownload__ if using Unity 5.2 or older. Only invest in a custom download system if the built-in APIs' memory consumption, caching behavior or performance are unacceptable for a specific project, or if a project must run platform-specific code to achieve its requirements.
</div>

通常推荐尽可能使用 UnityWebRequest 或者在 Unity 5.2及之前版本中使用 __WWW.LoadFromCacheOrDownload__。只有当内置的 API 在内存消耗，缓存行为或者性能上不满足项目，或者项目必须跑平台相关代码来满足其需求时才需要定制下载器。

<div style='display:none'>
Examples of situations which may prevent the use of __UnityWebRequest__ or __WWW.LoadFromCacheOrDownload__:

* When fine-grained control over the AssetBundle cache is required
* When a project needs to implement a custom compression strategy
* When a project wishes to use platform-specific APIs to satisfy certain requirements, such as the need to stream data while inactive.
    * Example: Using iOS' Background Tasks API to download data while in the background.
* When AssetBundles must be delivered over SSL on platforms where Unity does not have proper SSL support (such as PC).
</div>

不适用 __UnityWebRequest__ 或者 __WWW.LoadFromCacheOrDownload__ 的情况实例：

* 需要对 AssetBundle 缓存做细微地控制
* 项目需要实现定制的压缩策略
* 项目希望使用平台相关的 API 去满足特定需求，比如需要在程序非激活状态下读写数据
    * 比如：使用 iOS 的 Background Tasks API 去后台下载数据
* AssetBundle 需要通过在 Unity 不完全支持平台上使用 SSL，比如 PC

<div style='display:none'>
### 4.2.3. Built-in caching
</div>

### 内置缓存

<div style='display:none'>
Unity has a built-in AssetBundle caching system that can be used to cache AssetBundles downloaded via the __WWW.LoadFromCacheOrDownload__ or __UnityWebRequest__ APIs.
</div>

Unity 中有一个可以用来缓存通过 __WWW.LoadFormCacheOrDownload__ 或者 __UnityWebRequest__ API下载的软件 AssetBundle 的缓存系统。

<div style='display:none'>
Both APIs have an overloads which accept an an AssetBundle version number as an argument. This number is not stored inside the AssetBundle, and is not generated by the AssetBundle system.
</div>

这两个 API 都有接收 AssetBundle 版本号为参数的函数重载。这个版本号不是保存在 AssetBundle 里面，也不是由 AssetBundle 系统生成。

<div style='display:none'>
The caching system keeps track of the last version number passed to __WWW.LoadFromCacheOrDownload__ or __UnityWebRequest__. When either API is called with a version number, the caching system checks to see if there is a cached AssetBundle. If so, it compares the version number passed in when the AssetBundle was first cached, and the version number passed into the current call. If these numbers match, the system will load the cached AssetBundle. If the numbers do not match, or there is no cached AssetBundle, then Unity will download a new copy. This new copy will be associated with the new version number.
</div>

缓存系统会一直跟踪传递给 __WWW.LoadFromCacheOrDownload__ 和 __UnityWebRequest__ 的版本号。当带着版本号调用两者其中之一时，缓存系统会检查是否有缓存过的 AssetBundle。缓存系统会比较首次缓存时被传递的版本号和当前传递的版本号。如果两个版本号不匹配，或者没有缓存过的 AssetBundle，Unity 会下载一个新的副本，然后将其与新的版本号关联。

<div style='display:none'>
__AssetBundles in the caching system are identified only by their file names__, and not by the full URL from which they are downloaded. This means that an AssetBundle with the same file name can be stored in multiple different locations. For example, an AssetBundle can be placed on multiple servers on a Content Delivery Network. As long as the file names are identical, the caching system will recognize them as the same AssetBundle.
</div>

缓存系统中的 AssetBundle 只靠他们的文件名来鉴别的，并不是靠下载他们的地址。这就意味着拥有相同名字的 AssetBundle 可以存储在不同路径中。比如，一个 AssetBundle 可以放到内容分发网络中的多台服务器上。只要他们的文件名一样，缓存系统会认为它们是同一个 AssetBundle。

<div style='display:none'>
It is up to each individual application to determine an appropriate strategy for assigning version numbers to AssetBundles, and to pass these numbers to __WWW.LoadFromCacheOrDownload__. Most applications can use Unity 5's __AssetBundleManifest__ API. This API generates a version number for each AssetBundle by calculating an MD5 hash of the AssetBundle's contents. Whenever an AssetBundle changes, its hash also changes, and this indicates that the AssetBundle should be downloaded.
</div>

分配版本号给 AssetBundls 和传递这些版本号给 __WWW.LoadFromCacheOrDownload__ 的策略完全由各个应用自己决定。大部分应用可以用 Unity 5 的 __AssetBundleManifest__ API。这个 API 会根据 AssetBundle 的内容为其生成一个 MD5 哈希值。当 AssetBundle 改变时，这个哈希值会跟着改变，这表明这个 AssetBundle 需要被下载。

<div style='display:none'>
Note: Due to a quirk in the implementation of Unity's built-in cache, old AssetBundles will not be deleted until the cache fills up. Unity intends to address this quirk in a future release.
</div>

注意：Unity 内置缓存系统的实现方式的特殊，老的 AssetBundle 直到缓存被填满之后才会被删除。Unity 有意向在未来的 Release 中处理这个特殊。

<div style='display:none'>
See the [Patching with AssetBundles](https://unity3d.com/cn/learn/tutorials/topics/best-practices/assetbundle-usage-patterns#Patching_with_Asset_Bundles) section for more details.
</div>

更多详情参照 [给 AssetBundle 打补丁](https://unity3d.com/cn/learn/tutorials/topics/best-practices/assetbundle-usage-patterns#Patching_with_Asset_Bundles) 小节。

<div style='display:none'>
Unity's built-in caching can be controlled by calling APIs on the Caching object. The Unity cache's behavior can be controlled by changing Caching.expirationDelay and __Caching.maximumAvailableDiskSpace__.
</div>

我们可以调用缓存对象上的 API 来控制 Unity 内置的缓存。Unity 缓存的行为可以通过 __Caching.expirationDeplay__ 和 __Caching.maximumAvailableDiskSpace__ 来控制。

<div style='display:none'>
[Caching.expirationDelay](http://docs.unity3d.com/ScriptReference/Caching-expirationDelay.html) is the minimum number of seconds that must elapse before an AssetBundle is automatically deleted. If an AssetBundle is not accessed during this time, it will be deleted automatically.
</div>

[Caching.expirationDelay](http://docs.unity3d.com/ScriptReference/Caching-expirationDelay.html) 是 AssetBundle 被自动删除前最小需要达到的秒数。如果 AssetBundle 没有在设置的时间内访问，它将被自动删除。

<div style='display:none'>
[Caching.maximumAvailableDiskSpace](http://docs.unity3d.com/ScriptReference/Caching-maximumAvailableDiskSpace.html) determines the amount of space on local storage that the cache may use before it begins deleting AssetBundles that have been used less recently than the expirationDelay. It is counted in bytes. When the limit is reached, Unity will delete the AssetBundle in the cache which was least recently opened (or marked as used via Caching.MarkAsUsed). Unity will delete cached AssetBundles until there is sufficient space to complete the new download.
</div>

[Caching.maximumAvailableDiskSpace](http://docs.unity3d.com/ScriptReference/Caching-maximumAvailableDiskSpace.html) 决定了缓存在删除最少使用的 AssetBundle  前可以使用本地存储的最大空间。它通过字节来计数。当达到最大限制时，Unity 会删除最近最少打开的或者通过 Caching.MarkAsUsed 标识已使用的 AssetBundle。直到空间满足新下载的 AssetBundle 时 Unity 才会停止删除已缓存的 AssetBundle。

<div style='display:none'>
Note: As of Unity 5.3, control over the built-in Unity cache is very rough. It is not possible to remove specific AssetBundles from the cache. They will only be removed due to expiration, excess disk space usage, or a call to Caching.CleanCache. (Caching.CleanCache will delete all AssetBundles currently in the cache.) This can be problematic during development or live operations, as Unity does not automatically remove AssetBundles that are no longer used by an application.
</div>

注意：Unity 5.3 版本中控制内置缓存的功能很不完善。不支持主动地从缓存中移除指定的 AssetBundle, 而只能当 AssetBundle 超过了时限，或者超过了磁盘空间限制，或者调用 Caching.CleanCache API。Cache.CleanCache 将会清除缓存中的所有 AssetBundle。这会给开发过程或者线上操作带来问题，比如 Unity 不会移除不再被应用使用的 AssetBundle。

<div style='display:none'>
#### 4.2.3.1. Cache Priming
</div>

#### 填充缓存

<div style='display:none'>
Because AssetBundles are identified by their file names, it is possible to "prime" the cache with AssetBundles shipped with the application. To do this, store the initial or base version of each AssetBundle in /Assets/StreamingAssets/. The process is identical to the one detailed in the [Shipped with project](https://unity3d.com/cn/learn/tutorials/topics/best-practices/assetbundle-usage-patterns#Shipped_with_Project) section.
</div>

因为 AssetBundle 是通过他们的名字还鉴别的，所以将应用附带的 AssetBundle 填充到缓存是可行的。将初始或者基础版本的 AssetBundle 放置到 /Assets/StreamingAssets/ 文件夹下可以达到这种目的。这个过程跟 [随项目一起打包] (https://unity3d.com/cn/learn/tutorials/topics/best-practices/assetbundle-usage-patterns#Shipped_with_Project) 提到的一种方式是一样的。

<div style='display:none'>
The cache can be populated by loading AssetBundles from Application.streamingAssetsPath the first time the application is run. From then on, the application can call WWW.LoadFromCacheOrDownload or UnityWebRequest normally.
</div>

应用第一次运行的时候，将从 Application.streamingAssetsPath 加载的 AssetBundle 放置到缓存中。然后以后可以调用 WWW.LoadFromCacheOrDownload 或者 UnityWebRequest 加载。

<div style='display:none'>
### 4.2.3. Custom downloaders

Writing a custom downloader gives an application full control over how AssetBundles are downloaded, decompressed and stored. Writing a custom downloader is only recommended for larger teams writing ambitious applications. There are four major problems to think through when writing a custom downloader:

* How to download the AssetBundles
* Where to store the AssetBundles
* If/how to compress the AssetBundles
* How to patch the AssetBundles
For information on patching AssetBundles, see the [Patching with AssetBundles](https://unity3d.com/cn/learn/tutorials/topics/best-practices/assetbundle-usage-patterns#Patching_with_Asset_Bundles) section.
</div>

### 定制下载器

定制一个下载器可以让应用完全控制 AssetBundle 如何下载，压缩和存储。只有当大团队需要些一些精益的应用时才推荐写下载器。写一个下载器时有四个主要的问题需要考虑：

* 怎么样下载 AssetBundle
* 将 AssetBundle 存储到哪里
* 是否需要和如何压缩 AssetBundle
* 如果给 AssetBundle 打补丁

关于如何打补丁，可以参照 [给 AssetBundle 打补丁](https://unity3d.com/cn/learn/tutorials/topics/best-practices/assetbundle-usage-patterns#Patching_with_Asset_Bundles) 小节。

<div style='display:none'>
#### 4.2.3.1. Downloading
</div>

#### 下载

<div style='display:none'>
For most applications, HTTP is the simplest method to download AssetBundles. However, implementing an HTTP-based downloader is not the simplest task. Custom downloaders must avoid excessive memory allocations, excessive thread usage and excessive thread wakeups. Unity's WWW class is unsuitable for reasons exhaustively described here. Because of WWW's high memory cost, Unity's WWW class should be avoided if an application is not using WWW.LoadFromCacheOrDownload.
</div>

对于大多数应用，HTTP 是下载  AssetBundle 最简单的方式。但是，实现一个基于 HTTP 的下载器并不是一个简单的任务。定制的下载器需要避免过高的内存开销，过高的线程使用率和过多的线程唤醒。Unity 的 WWW 类对这些描述来说是不适合的。因为 WWW 会消耗比较高的内存，应该避免在不适用 WWW.LoadFromCacheOrDownload 的应用中使用 WWW 类。

<div style='display:none'>
When writing a custom downloader, there are three options:

* C#'s HttpWebRequest and WebClient classes
* Custom native plugins
* Asset store packages
</div>

当要写一个定制的下载器时，有 3 个选项：

* C# 的 HttpWebRequest 和 Web Client 类
* 定制的原生插件
* AssetStore packages

<div style='display:none'>
#### 4.2.3.1.1. C# classes
</div>

##### C# 类

<div style='display:none'>
If an application does not require HTTPS/SSL support, C#'s [WebClient](https://msdn.microsoft.com/en-us/library/system.net.webclient(v=vs.110).aspx) class provides the simplest possible mechanism for downloading AssetBundles. It is capable of asynchronously downloading any file directly to local storage without excessive managed memory allocation.
</div>

如果应用不需要支持 HTTPS/SSL，C# 的 [WebClient](https://msdn.microsoft.com/en-us/library/system.net.webclient(v=vs.110).aspx) 类提供了最简单的机制用来下载 AssetBundle。它能将任何文件异步的下载到本地存储中，不需要过多的内存分配。

<div style='display:none'>
To download an AssetBundle with WebClient, allocate an instance of the class and pass it the URL of the AssetBundle to download and a destination path. If more control is required over the request's parameters, it is possible to write a downloader using C#'s [HttpWebRequest](https://msdn.microsoft.com/en-us/library/system.net.httpwebrequest(v=vs.90).aspx) class:

1. Get a byte stream from HttpWebResponse.GetResponseStream.
2. Allocate a fixed-size byte buffer on the stack.
3. Read from the response stream into the buffer.
4. Write the buffer to disk using C#'s File.IO APIs, or any other streaming IO system.
</div>

使用 WebClient 下载 AssetBundle, 只要创建一个 WebClient 实例，将 AssetBundle 的下载地址和存储地址传给实例就可以。如果需要更多的控制请求的参数，可以使用 C# 的 [HttpWebRequest](https://msdn.microsoft.com/en-us/library/system.net.httpwebrequest(v=vs.90).aspx) 类去写下载器。

<div style='display:none'>
Platform Notes: iOS, Android and Windows Phone are the only platforms for which Unity's C# runtime has HTTPS/SSL support for the C# HTTP classes. On PCs, attempting to access an HTTPS server via C#'s classes will result in certificate validation errors.
</div>

平台注意： Unity C# 运行时支持 HTTPS/SSL 的平台仅有 iOS, Android 和 Windows Phone。在 PC 平台上，试图用 C# 类去访问 HTTPS 服务器的话会得到证书验证失败的错误。

<div style='display:none'>
##### 4.2.3.1.2. Asset Store Packages

Several asset store packages offer native-code implementations to download files via HTTP, HTTPS and other protocols. Before writing a custom native-code plugin for Unity, it is recommended to evaluate available Asset Store packages.
</div>

##### Asset Store Packages

有好几个 Asset Store packages 提供 Native-code 实现的可以通过 HTTPS, HTTPS 和其他协议下载文件的功能。在为 Unity 写定制的 native-code 插件时，推荐先评估一下 Asset Store Packages。

<div style='display:none'>
##### 4.2.3.1.3. Custom Native Plugins
</div>

#### 定制原生插件

<div style='display:none'>
Writing a custom native plugin is the most time-intensive and most flexible method for downloading data in Unity. Due to the high programming-time requirements and high technical risk, this method is only recommended if no other method is capable of satisfying an application's requirements. For example, a custom native plugin may be necessary if an application must use SSL communication on platforms without C# SSL support in Unity, such as Windows, OSX, and Linux.
</div>

写一个定制下载器是在 Unity 下载数据方式中最耗时间和最灵活的。由于需要比较多的编程时间和技术要求，这个方式只推荐在其他方式不能满足应用需求的时候使用。比如，当应用必须要在 Unity 不支持的平台上使用 SSL 通讯时。这些平台有 Windows, OSX (mac OS) 和 Linux。

<div style='display:none'>
A custom native plugin will generally wrap a target platform's native downloading APIs. Examples include NSURLConnection on iOS and [java.net.HttpURLConnection](http://download.java.net/jdk7/archive/b123/docs/api/java/net/HttpURLConnection.html) on Android. Consult each platform's native documentation for further details on using these APIs.
</div>

定制原生插件一般会封装目标平台上的原生下载 API. 比如 iOS 上的 NSURLConnection 和安卓平台上的 [java.net.HttpURLConnection](http://download.java.net/jdk7/archive/b123/docs/api/java/net/HttpURLConnection.html)。关于这些 API 的更详细使用，请查看对于平台的原生文档。

<div style='display:none'>
#### 4.2.3.2. Storage
</div>

#### 存储

<div style='display:none'>
On all platforms, Application.persistentDataPath points to a writable location that should be used for storing data that should persist between runs of an application. When writing a custom downloader, it is strongly recommended to use a subdirectory of Application.persistentDataPath to store downloaded data.
</div>

在所有平台上，Application.persistentDataPath 都指向一个可以写的路径，这个路径用来保存可以程序多次运行都不会丢失的数据。当写一个定制下载器时，强烈推荐使用 Application.persistentDataPath 的子目录去存储已下载的数据。

<div style='display:none'>
Application.streamingAssetPath is not writable and is a poor choice for an AssetBundle cache. Example locations for streamingAssetsPath include:

* __OSX:__ Within .app package; not writable.
* __Windows:__ Within install directory (e.g. Program Files); usually not writable
* __iOS:__ Within .ipa package; not writable
* __Android:__ Within compressed .jar file; not writable
</div>

Application.streamingAssetPath 是只读的，是用来做 AssetBundle 缓存的一个糟糕的选择。streamingAssetPath 包括：

* __OSX (mac OS)：__ 在 .app 包内，不可以写
* __Windows：__ 在安装目录内（一般是 Promgram Files），通常不可写
* __iOS：__ 在 .ipa 包内，不可写
* __Android：__ 在压缩的 .jar 文件内，不可写

<div style='display:none'>
### 4.3. Asset Assignment Strategies
</div>

### 资产分配策略

<div style='display:none'>
Deciding how to divide a project's assets into AssetBundles is not simple. It is tempting to adopt a simplistic strategy, such as placing all Objects in their own AssetBundle or using only a single AssetBundle, but these solutions have significant drawbacks:

* Having too few AssetBundles...
    * Increases runtime memory usage
    * Increases loading times
    * Requires larger downloads
* Having too many AssetBundles...
    * Increases build times
    * Can complicate development
    * Increases total download time
</div>

决定如何将项目内的资产分配到 AssetBundle 是不容易的。光使用简单的规则，比如将所有对象都放置到他们自己的 AssetBundle 中或者将所有对象都放到一个 AssetBundle 中，但是这些方案都有明显的缺点：

* AssetBundle 数量太少
    * 会增加运行时内存使用
    * 会增加加载时间
    * 需要下载更多数据
* 有太多的 AssetBundle
    * 会增加编译的时间
    * 会加大开发的复杂性
    * 会增加总的下载时间

<div style='display:none'>
The key decision is how to group Objects into AssetBundles. The primary strategies are:

* Logical entities
* Object Types
* Concurrent content
</div>

关键之处的如何将对象分组到 AssetBundle 中。主要的策略有：

* 逻辑实体
* 对象类型
* 并行的内容

<div style='display:none'>
Note that a single project can and should mix these strategies for different categories of content. For example, a project might group UI elements together into AssetBundles meant for different platforms, but group its interactive content by level or scene. Regardless of the strategy adopted, these are good guidelines to follow:

* Split frequently-updated Objects into different AssetBundles than Objects that usually remain unchanged
* Group together Objects that are likely to be loaded simultaneously


Example: A model, its animations and its texture(s).

* If an Object is a dependency of multiple Objects in multiple different AssetBundles, move the asset into a separate AssetBundle.
    * Ideally, group child Objects together with their parent Objects.
* If two Objects are unlikely to be loaded simultaneously, such as HD and SD versions of a texture, split them into separate AssetBundles.
* If the Objects are different versions of the same Object with different importer settings or data, consider using AssetBundle Variants instead.
</div>

注意一个项目对于不同的内容分类可以将这些并且应该将这些策略混合地使用。比如一个项目可能需要将 UI 元素分组到不同平台的 AssetBundle 中，但是靠关卡或者场景来分组他们项目关联的内容。关于使用的策略，有一些好的指导去遵循：

* 相比不经常更新的内容，将经常更新的对象拆分到不同的 AssetBundle 中
* 将可能同时加载的对象分组到一起。比如模型和他的动画与纹理
* 如果一个对象被多个 AssetBundle 中的多个对象依赖，将它分配到单独的 AssetBundle 中
* 如果两个对象不太可能同时加载，比如一个纹理的高清和标清版本，可以将他们分配到不同的 AssetBundle 中
* 如果是同一个对象的不同导入设置或者数据的不同版本，考虑使用 AssetBundle 变体来替代

<div style='display:none'>
Once the above guidelines are followed, consider splitting apart an AssetBundle if less than 50% of the AssetBundle's content is loaded at any given time. Also consider combining small AssetBundles (less than 5-10 assets) that are loaded concurrently.
</div>

一旦遵循上面的指导，考虑将规定时间内小于 50% 能被加载的 AssetBundle 拆分。也可以考虑将一些小的 AssetBundle (资产数量小于 5 - 10 个) 合并。

<div style='display:none'>
### 4.3.1. Logical entity grouping
</div>

### 逻辑实体分组

<div style='display:none'>
Logical entity grouping is a strategy where Objects are grouped based on the functional part of the project they represent. When adopting this strategy, different parts of the application are separated into different AssetBundles.
</div>

逻辑实体分组是一个通过项目功能来分组对象的策略。当采用这种策略时，应用不同部分会单独分组进不同的 AssetBundle 中。

<div style='display:none'>
Examples:

* Bundling together all of the textures & layout data for a UI screen
* Bundling together the textures, models and animations for a set of characters
* Bundling together the textures and models for pieces of scenery shared across many levels

</div>

例如：

* 一个 UI 屏幕中的所有纹理和布局数据打包在一起
* 一个角色的纹理、模型和动画打包在一起
* 被多个关卡共享的场景碎片的纹理和模型打包在一起

<div style='display:none'>
Logical entity grouping is the most common AssetBundle strategy, and is particularly suitable for:

* DLC
* Entities that appear at many places throughout the application's lifetime
</div>

逻辑实体分组是最常用的 AssetBundle 策略，特别适用于：

* DLC （Downloadable Content）
* 实体在应用生命周期内多处被用到

<div style='display:none'>
Examples:

* Common characters or basic UI elements
* Entities that vary solely based on platform or performance settings
</div>

例如：

* 通用的角色或者基本 UI 元素
* 完全不依赖于平台或者性能设置的实体

<div style='display:none'>
The advantage to grouping assets by logical entity is that it permits individual entities to be easily updated without re-downloading unchanged content. This is why this strategy is particularly suitable for DLC. This strategy also tends to be the most memory-efficient, as an application needs to load only the AssetBundles representing the entities currently in-use.
</div>

逻辑实体分组的优点是不需要从新下载不变内容的情况下轻松的更新实体。这就是它为什么特别适合 DLC （Downloadable Content）的原因。这个策略也是内存效率最高的，因为应用只需要加载当前使用的实体的 AssetBundle。

<div style='display:none'>
However, this is the trickiest strategy to implement, as the developers assigning Objects to AssetBundles must be familiar with precisely how and when each individual Object will be used by the project.
</div>

尽管如此，这也是最难实现的策略，因为分配对象给 AssetBundle 的开发者必须精确地熟悉单个对象是怎么样和如何被项目使用的。

<div style='display:none'>
### 4.3.2. Type grouping
</div>

### 类型分组

<div style='display:none'>
Type grouping is the simplest strategy. In this strategy, Objects of similar or identical types are placed into the same AssetBundle. For example, one might place several different audio tracks into an AssetBundle, or several different language files into an AssetBundle.
</div>

类型分组是最简单的策略。在这个策略中，相似或者相同类型的对象被放置到同一个 AssetBundle 中。比如，将不同的音轨放置到同一个 AssetBundle 或者不同的语言文件放置到同一个 AssetBundle。

<div style='display:none'>
While this strategy is simple, it is often the least efficient in terms of build times, load times and updates. It is most often used for files that are small and are updated concurrently, such as localization files.
</div>

这个策略简单的同时，它却经常是在编译时，加载时和升级时最低效的。它最常用的对象需要同时升级的小文件，比如本地化文件。

<div style='display:none'>
### 4.3.3. Concurrent content grouping
</div>

### 并行内容分组

<div style='display:none'>
Concurrent content grouping is a strategy where content is grouped together into an AssetBundle if it will be loaded and used simultaneously. This strategy is most commonly used in projects where content is strongly local: where content rarely (or never) appears outside of specific places or times in the application. An example might be a level-based game with unique art, characters and sound effects for each level.
</div>

并行内容分组是将需要同时加载和使用内容分组到同一个 AssetBundle 的策略。这种策略最常用在具有较强本地属性的内容上，也就是说内容很少或者基本不可能在应用特定的位置或者时间外出现。举个例子，关卡游戏中没一关卡都独一无二的艺术呈现，角色和声效。

<div style='display:none'>
The most common method for performing concurrent-content grouping is to construct AssetBundles based on scenes, with each scene-based AssetBundle containing most or all of that scene's dependencies.
</div>

实现并行内容分组的最常用的方法是通过场景来构建 AssetBundle，每个 AssetBundle 包括了场景中的几乎所有的依赖。

<div style='display:none'>
For projects where content is not strongly local, and where content commonly appears at varying points in an application's lifecycle, concurrent content grouping converges with logical entity grouping. Both are essentially strategies for maximizing the utilization of a given AssetBundle's contents.
</div>

对没有较强本地属性的项目，和在应用声明周期内很少出现的内容，应该通过逻辑实体策略来分组。这两种都是最大化使用 AssetBundle 内容的大体策略。

<div style='display:none'>
An example of this scenario might be an open-world game where characters are randomly spawned and distributed in world-space. In this case, it is not easy to predict which characters will appear simultaneously, and therefore they generally should be grouped using a different strategy.
</div>

这个场景的一个例子就是，一个角色在世界中随机生成的开发世界游戏。这种情况中，很难预测交个角色会同时出现，所以他们一般需要使用不同的策略。