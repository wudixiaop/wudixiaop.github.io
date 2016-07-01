title: Unity 5： Asset Bundle 和 Asset Bundle Manager (1)
date: 2015-11-10 16:16:56
tags: AssetBundle
category: UnityKB
---

这篇是 Unity 官方教程 [AssetBundles and the AssetBundle Manager](http://unity3d.com/cn/learn/tutorials/topics/scripting/assetbundles-and-assetbundle-manager?playlist=17117) 的翻译， 分三部分，这是第一部分。翻译不到之处请不吝指出。非常谢谢！
<hr>

<div style="display:none">
#~###INTRODUCTION

AssetBundles allow on demand streaming and loading of Assets from a local or remote location. With AssetBundles, Assets can be stored remotely and accessed as needed, increasing the flexibility of the project and reducing the initial application size.
</div>

### 介绍  

AssetBundle 允许按需地从本地或者远程服务器上加载资源(Asset)。通过 AssetBundle 的方式，资源可以远程存储，有需要的时候访问，这样提升了项目的灵活性和降低初始程序的大小。

<div style="display:none">
This lesson will introduce AssetBundles and discuss how to work with them, the steps and stages of the AssetBundle workflow, how to assign Assets to an AssetBundle, how and when to use AssetBundle Variants, how to build and test AssetBundles and Variants - all in the context of using the AssetBundle Manager to simplify creating, testing and deploying AssetBundles. The final section of the lesson will cover specific examples of loading and using AssetBundles and AssetBundle Variants with simple use-cases and simple example scripts.
</div>

这篇教程将会介绍 AssetBundle 和及其应用，AssetBundle 流程的步骤和各阶段和怎么样编译和测试 AssetBundle 及其变体 - 所有的一切可以用 AssetBundle Manager 来简化创建，测试和部署 AssetBundle。教程的最后一部分将使用一些加载和使用 AssetBundle 变体的简单用例和脚本示例。

<div style='display:none'>
###SAMPLE PROJECT
</div>

### 演示项目

<div style='display:none'>
Before starting this Tutorial Article, it would be best to download the AssetBundle Manager with the AssetBundle Sample project here.
</div>

在开始教程之前，最后先下载好 AssetBundle 和 AssetBundle Manager 的[示例程序](http://u3d.as/jyk)。

<div style='display:none'>
###WHAT IS AN ASSETBUNDLE?

AssetBundles are files created in the Unity editor during edit-time, which can be used later by a build of a project at run-time. AssetBundles can contain asset files such as models, materials, textures and scenes. AssetBundles cannot contain scripts.
</div>

### 什么是 AssetBundle

AssetBundle 是由 Unity 编辑器在编辑时期创建的，可以被编译出来的程序在运行期使用的文件。AssetBundle 可以包含模型，材质，纹理和场景文件等资源。但是 AssetBundle 不能包含脚本。

<div style='display:none'>
Specifically, an AssetBundle is a collection of assets and/or scenes from a project saved in a compact file with the purpose of being loaded separately to the built executable application. AssetBundles can be loaded on demand by a game or application built in Unity. This allows streaming and asynchronous loading of content such as models, textures, audio clips, or even entire scenes. AssetBundles can be “pre-cached” and stored locally for immediate loading when first running an application. The primary purpose of AssetBundles, however, is to stream content on demand from a remote location, to be loaded into the application as necessary. AssetBundles can contain any kind of asset type recognized by Unity, including custom binary data. The only exception is that script assets are not allowed.
</div>

明确一点说，一个 AssetBundle 就是存储项目资源和 / 或场景集合的文件，目的是为了之后在游戏或者程序中加载。
AssetBundle 可以被在 Unity 中编译出来的游戏或者程序按需加载。它允许传送和异步加载像模型，材质，声音剪辑，
甚至是整个场景。当在程序中初次运行时， AssetBundle 会被存储到本地 “预缓存” 以备以后被立即加载。Assetbundle 的主要目是为了需要的时候能从远程传送内容并加载进程序。AssetBundle 可以包含可以被 Unity 识别的任何资源类型，包括二进制文件。唯一的另外就是不允许是脚本资源。

<div style='display:none'>
There are many use-cases for AssetBundles. New content can be dynamically loaded and unloaded from an application. Post-release DLC can easily be implemented. An application’s disk footprint or size can be reduced when first deployed, with assets being loaded after installation of the application and only as the assets are needed. Platform and device specific assets can be loaded without having to download or store redundant assets for other platforms or resolutions. Localization of applications becomes easy by downloading and installing only the assets needed based on the user’s location, language or preferences. Applications can be fixed, changed or updated with new content without having to resubmit the application for approval.
</div>

AssetsBundle 有很多用处。比如新的内容可以动态地在程序中加载和释放。可以很简单实现发布后的可下载内容(DLC, Downloadable Content)。
程序第一次安装的的时候的大小或者磁盘占用空间会减少，资源只有安装的程序需要的时候才会被加载。平台或者设备相关的资源加载时可以不必要下载或冗余存储其他平台和方案中的资源。本地化的程序可以更容易来下载和安装基于用户位置，语言和偏好的资源。新的内容可以下修复，改变或更新，而不需要重新发布程序。

<div style='display:none'>
The detailed organization of any project’s assets into AssetBundles will be heavily dependent upon the needs of that particular project. There are, however, some basic tenets to understand about AssetBundles.
</div>

AssetBundle 内项目资源的组织严重依赖于项目的需求。但是，也有一些可以更好的理解 AssetBundle 的原则。

<!--more-->

<div style='display:none'>
* AssetBundles are downloaded and cached in their entirety.
* AssetBundles do not need to be loaded in their entirety.
* Assets in AssetBundles can have dependencies on other assets.
* Assets in AssetBundles can share dependencies with other assets.
* Each AssetBundle has some technical overhead, both in the size of the file and the need to manage that file.
* AssetBundles should be built for each target platform.
</div>

* AssetBundle 是整体被下载和缓存的
* AssetBundle 不需要整体被加载
* AssetBundle 中的资源可以包括依赖的其他资源
* AssetBundle 中的资源可以共享依赖的其他资源
* 每个 AssetBundle 在文件大小和处理上都有一些技术上的开销。
* 每个平台上的 AssetBundle 都需要单独编译

<div style='display:none'>
AssetBundles are downloaded in their entirety. If an AssetBundle contains Assets that are not immediately needed, even though they won’t necessarily be loaded into the scene, they will take up both bandwidth to download and disk-space to store.
</div>

AssetBundle 是整体被下载的。如果在一个 AssetBundle 中包含不需要立即加载，甚至不需要加载进场景的资源，它们也会占用下载带宽和存储空间。

<div style='display:none'>
The contents of AssetBundles do not need to be loaded in their entirety. Once an AssetBundle has been downloaded, Assets can be selectively loaded from the AssetBundle.
</div>

AssetBundle 的内容不需要整体加载的。一旦 AssetBundle 被下载过了，资源可以有选择性的从 AssetBundle 中加载。

<div style='display:none'>
Assets can have dependencies on other assets. For example, a model can have several dependencies. The final model in the game is not just mesh data, but it is a GameObject with all of its Components and all of the Component’s dependencies.
</div>

资源能包括依赖的其他资源。比如，一个模型有好几个依赖。最终在游戏里的摩西不光只有网格数据，它会是一个包含所有组件和组件的依赖项的游戏对象(GameObject)。

![meshmodelwmaterial](http://unity3d.com/sites/default/files/meshmodelwmaterial.png) 
<small>_应用了材质的模型_</small>

<div style='display:none'>
This model is dependent on a Material Asset in the model’s Mesh Renderer, and that Material Asset is dependent on a Texture Asset for the Material’s Albedo Texture. As a matter of fact, this tank is dependent upon three Materials, not just one.
</div>

这个模型依赖于在模型的 Mesh Renderer 组件中的一个材质资源，而这个材质资源依赖于应用在材质的 Albedo 纹理上的纹理资源。实际上，这个坦克依赖了三个材质，而不是仅仅一个。

![dependencies](http://unity3d.com/sites/default/files/dependencies2.png)
<div style='display:none'>
_The tank model’s Asset dependency chain: Model > Material > Texture_
</div>
<small>_坦克模型资源的依赖链：模型 > 材质 > 纹理_</small>

<div style='display:none'>
Assets can share dependencies with other assets. For example, two different models can share the same Material, which in turn could be dependent on a Texture.
</div>


资源可以共享依赖的其他资源。比如，两个模型可以共享同一个材质, 相应的可能依赖于同一个纹理。

<div style='display:none'>
_Both rock columns are different models that share the same Material_
</div>	

![two rock columns](http://unity3d.com/sites/default/files/two_rock_columns.png) 
<small>_两个共享同一个材质的不同的岩石柱模型_</small>

<div style='display:none'>
Each AssetBundle has some technical overhead. AssetBundles are files that wrap Assets. This wrapper adds to the overall size of the AssetBundle. Even though this is not a significant increase in size, it is measureable. AssetBundles also require a certain amount of management to organize, create, upload and maintain. The more AssetBundles being used increases overhead for a project, both technical and managerial.
</div>

每个 AssetBundle 都会有一些技术上的开销。AssetBundles 是包装资源的文件。这个包装会增加 AssetBundle 的总大小。即使这个增量不大，可测量。AssetBundle 还要求一定量的处理来组织，创建，上传和维护。从技术上和处理上，使用的 AssetBundle 越多，其在项目中的开销越大。

<div style='display:none'>
When organizing AssetBundles, a balance must be struck between too many small AssetBundles that need to be tracked and generate overhead, and too few AssetBundles that are large and contain unnecessary or redundant data. The exact balance will depend heavily upon the needs of the project.
</div>

当组织 AssetBundle 时，需要在 **使用数量多体积小但需要跟踪和生成开销的 AssetBundle ** 还是 
**数量小但体积大且包含很多不必要的多余的数据的 AssetBundle** 中做出平衡。具体的平衡策略严重依赖于项目的需求。

<div style='display:none'>
The contents of an AssetBundle are compiled and optimized for the current target platform according to the Import Settings and the current Target Platform. Because of this, AssetBundles should be built for each target platform.
</div>

AssetBundle 的内容是根据当前的 Import Settings 和 平台来编译和优化的。所以，AssetBundle 需要为不同平台编译。

<div style='display:none'>
###MANIFESTS AND DEPENDENCY MANAGEMENT

There are several important points to understand regarding dependencies and dependency management.
</div>

### 清单和依赖管理

理解关于依赖和依赖管理，有几个重要的点。

<div style='display:none'>
Asset dependencies are never lost. Dependent Assets will be added to the AssetBundle automatically along with the selected Asset if that dependent Asset has not been assigned to any AssetBundle when the AssetBundles are built. This is very convenient and prevents the loss of dependent assets. However, this can also cause the duplication of Assets. For example, using the two rock columns above which share the same Material, if both rock columns are in separate AssetBundles and the Material is not explicitly assigned to an AssetBundle, that Material will be added to both AssetBundles containing the rock columns. It is worth noting that when this happens, both duplicate Assets are stored in their respective AssetBundles and the Asset dependencies are now split. Each model Asset will now depend upon the local copy of the Material Asset, removing any advantage of having shared Material Assets. To prevent this from happening, the Material needs to be explicitly assigned to an AssetBundle. This can be an AssetBundle of its own, or shared with other Assets. In either case, the AssetBundles with the rock columns will now be dependent upon the AssetBundle with the rocks’ Material.
</div>

资源依赖永远不会丢失。当 AssetBundle 编译的时候，即便独立的资源没有指定到任何的 AssetBundle，也会跟着被选中的资源中被自动的加入 AssetBundle中。这样很便捷并且可以防止独立资源的丢失。尽管如此，这还是会引起资源的重复。比如，以上面使用同一个材质的两个岩石柱为例，如果两个岩石柱分开在不同的两个 AssetBundles 中并且这个材质没有显式的指定到一个 AssetBundle 上，这个材质就会被加入到这两个包含岩石柱的 AssetBndles 中。这个值得注意，两个重复的资源现在被存储到各自的 AssetBundle 中，资源的依赖性被分离了。每个模型资源现在依赖于各自的材质资源的本地拷贝，丢失了共享材质的优势。为了比避免这个发生，这个材质需要显式的指定到一个 AssetBundle 中。这样 AssetBundle 可以自己使用它也，也可以和其他资源一起共享。这种情况下，拥有岩石柱的 AssetBundles 依赖于拥有岩石材质的 AssetBundle 了。

<div style='display:none'>
The dependencies and other information for a project’s AssetBundles are stored in a Manifest. The manifest is very much like a “table of contents” for the project’s AssetBundles. When AssetBundles are built, Unity generates a large amount of data. The details of this data are saved in the Manifest. There is one Manifest created for each target platform. The Manifest lists all of the AssetBundles created from the project for the current build target, and stores and tracks all of their dependencies. With the Manifest, it is possible to query all AssetBundles and all their dependencies.
</div>

项目的 AssetBundle 的依赖和其他信息存储在 **清单(Manifest)** 中。清单非常像关于项目的 AssetBundles 的 "目录"。当 AssetBundle 在编译的时候，Unity 会生产大量的数据。数据的细节存储在清单里。每个平台都会创建一个清单。清单为编译对象列举了所有从项目创建的 AssetBundles，存储位置和跟踪他们的依赖。利用清单，可以查询所有的 AssetBundles 和他们的依赖。

<div style='display:none'>
There is one special setup for AssetBundles called AssetBundle Variants. AssetBundle Variants are designed to support one specific use case - remapping a choice of different Assets to individual objects in a project. This is particularly useful when working with projects that need to select one Asset from a wide variety of different possible choices based on criteria like resolution, language, localization, or user preference. AssetBundle Variants can hold the variety of Assets required to cover all supported options for an object and the desired Asset can be mapped to that object as needed from the chosen AssetBundle Variant.
</div>

对于 AssetBundles 有一种特殊设置，叫做 AssetBundle 变体。AssetBundle 变体被设计来支持更特殊的使用场景 - 对单独的对象映射不同的资源选择。这对于需要依据一些标准，如分辨率，语言，地区或者用户偏好来从很多可能中选择一个资源的项目特别有用。AssetBundle 变体可以包含用来覆盖所有支持的选项的多种资源，
并且按需从选择的 AssetBundle 变体中映射期望的资源到对象上。

<div style='display:none'>
AssetBundles are files which contain asset files such as models, materials, textures and scenes. AssetBundles are created by the Unity editor during edit-time and can be used later at run-time by a built application. AssetBundles are designed to load Assets on demand from a local or remote source. AssetBundles can have Variants which can be mapped to objects in the scene depending upon the user’s preference.
</div>

AesstBundles 是包含模型，材质，纹理和场景文件等资源文件的文件。AssetBundles 在编辑器的编辑期创建，可以被编译出来的程序之后使用。AssetBundles 被设计来从本地或远程源中按需加载资源。AssetBundles 可以拥有变体，可以基于用户偏好映射到对象上。

<div style='display:none'>
For more detailed information about working with AssetBundles and the AssetBundle Manager, please see the next tutorial lesson in this series.
</div>

关于使用 AssetBundle 和  AssetBundle Manger 的更多细节，请看这系列的下一个教程。