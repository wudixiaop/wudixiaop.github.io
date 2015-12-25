title: Unity 5：使用 Asset Bundle 和 Asset Bundle Manager (2)
date: 2015-11-11 20:28:07
tags: Unity
---

这篇是 Unity 官方教程 [AssetBundles and the AssetBundle Manager](http://unity3d.com/cn/learn/tutorials/topics/scripting/assetbundles-and-assetbundle-manager?playlist=17117) 的翻译， 分三部分，这是第二部分。翻译不到之处请不吝指出。非常谢谢！
<hr>

<div style='display:none'>
##WORKING WITH ASSETBUNDLES AND THE ASSETBUNDLE MANAGER
###INTRODUCTION
</div>

### 介绍

<div style='display:none'>
One of the key areas of effort in working with AssetBundles is the building and testing of bundles. Often, during development, the Assets themselves are changing regularly. Normally this would require regularly building AssetBundles, uploading them to a host and testing these remotely hosted AssetBundles through a network connection with the working project.
</div>

使用 AssetBundle 中一个关键的地方是编译和测试 bundles。一般情况下，资源在开发过程中是会变的。正常地，可能需要要求有规律的编译 AssetBundle, 上传到服务器和然后通过网络连接在当前项目中测试远程的 AssetBundle.

<div style='display:none'>
This section focuses on using the AssetBundle Manager when working with AssetBundles. The AssetBundle Manager provides a High-level API for a massively improved workflow compared to manipulating AssetBundles directly with the foundation Low-level API.
</div>

这节主要关注 AssetBundle Manager 使用 AssetBundle。相对利用基础的低层 API 来操作 AssetBundle, AssetBundle Manager 为太幅改进的流程提供了高层的 API。

<div style='display:none'>
###WORKING WITH ASSETBUNDLES

The steps of working with AssetBundles in the editor fall roughly into these steps: - Organizing & Setting-up AssetBundles in the editor. - Building AssetBundles. - Uploading AssetBundles to external storage. - Downloading AssetBundles at run-time. - Loading objects from AssetBundles.
</div>

### 使用 AssetBundle  

在编辑器中使用 AssetBundle 的大体步骤：- 在编辑器中组织 & 设置 AssetBundle。 - 编译 AssetBundle。 - 上传 AssetBundle 到外部存储 - 运行期下载 AssetBundle - 从 AssetBundle 加载对象。  

<div style='display:none'>
It is worth noting that some AssetBundles can be stored locally for immediate loading as a default setup. This is useful to protect against an install where the application cannot reach remote external storage to download desired AssetBundles. For example, the application would load default language and localization data from a local AssetBundle when the application has no access to downloadable content.  
</div>

值得注意的一点，有些 AssetBundle 可以存储在本地作为即时加载的默认设置。这样对不能访问远程存储下载期望的资源的安装特别有用。比如，当不能访问可下载内容的时候，程序可以从本地的 AssetBundle 中加载默认的语言和本地化数据。

<div style='display:none'>
It is also worth noting that an AssetBundle contains platform ready Assets. The contents of an AssetBundle have been compiled and optimized for the current target platform according to the Import Settings and the Target Platform set in the Build Settings. Because of this, AssetBundles should be built for each target platform.
</div>

值得注意的是一个 AssetBundle 包括平台准备资源。AssetBundle 的内容会根据 Import Settings 里设置的当前平台和 Build Settings 里面的目标平台做编译和优化。因为这样，需要为每个平台编译 AssetBundle。

<div style='display:none'>
In the following simple scene, one legitimate way of organizing the scene into AssetBundles for the greatest versatility would be to have a base scene, which would include the ground, dunes, rock columns, tree and cactus. This scene could be allowed to include the dependent Materials, as these are fairly simple and would not likely need to be changed depending upon resolution or device. The tank model would be in an AssetBundle of it’s own, which would allow changes or updates to the player Asset. Two additional AssetBundles would be used to complete the tank GameObject. These would be the dependent Materials in one, and the dependent Texture in another. This would allow for changes and updates to the texture and material as needed with the least amount of trouble. This particular organization will also allow for alternative versions, or variants, of these Assets to be loaded from a choice of AssetBundle Variants on demand depending upon need, such as platform, location or resolution of the target device.
</div>

在接下来的简单的场景中, 为了AssetBundle 最大的用途，有个合理的组织 AssetBundle 场景内容的方式就是把草地，沙丘，岩石柱，树和仙人掌都打包到一个基础场景里面。这个基础场景可能包含依赖的材质，因为他们很简单，以后不太可能会基于分辨率或者设备而改变。坦克模型将需要一个自己的 AssetBundle, 这样允许改变或者更新玩家资源。为了实现坦克游戏对象，还需要两个额外的 AssetBundle. 一个是独立的材质资源，另外是独立的纹理资源。这将会给需要给纹理和材质的更改和更新时带来最小的麻烦。这个特别的组织方式也允许有其他版本或者基于平台、位置或者目标设备分辨率选择 AssetBundle 的变体。

![simpleScene](http://unity3d.com/sites/default/files/simple_scene.png) 
<div style='display:none'>
<small>_A Simplified Example Scene_</small>
</div>
<small>_一个简单的示例场景_</small>

<div style='display:none'>
To organize and setup AssetBundles in the editor, the Assets themselves need to be assigned to an AssetBundle. When viewing an Asset, the AssetBundle Name and AssetBundle Variant can be found at the bottom of the preview window in the Inspector. The preview window must be open to see them.
</div>

为了在编辑器中组织和设置 AssetBundle, 资源需要指定一个 AssetBundle。 查看资源的时候，可以在 Inspector 的底部查看 AssetBundle 的名字和变体。在打开的预览窗口中能看到他们。

![assetbundleName](http://unity3d.com/sites/default/files/assetbundlename.png)

<div style='display:none'>
descriptionAn Asset that has not been assigned to an AssetBundle.
</div>

<small>一个还没有指定 AssetBundle 的资源</small>  

<div style='display:none'>
To assign an Asset to an AssetBundle, use the AssetBundle Name drop down menu. Here, either create a new AssetBundle name or choose an existing one. AssetBundle Variants and the AssetBundle Variant Name menu will be covered later in this lesson.
</div>

使用 AssetBundle 名字下拉菜单来给资源指定 AssetBundle。在这可以创建一个新的 AssetBundle 或者选择已经存在的 AssetBundle。教程的后面会谈到 AssetBundle 变体和 AssetBundle 变体名字。

![abmenu2](http://unity3d.com/sites/default/files/ab-menu2.png) 


<div style='display:none'>
descriptionAssigning an Asset to an AssetBundle
</div>

<small>_给一个资源指定 AssetBundle_</small>  

<div style='display:none'>
To create a new AssetBundle, choose New and a text field will become active to name a new AssetBundle.
</div>

创建新的 AssetBundle, 选择 **New**，文本区域将会激活用来命名新的 AssetBundle。

<div style='display:none'>
To remove an Asset from an AssetBundle, choose None and the Asset will now be unassigned.
</div>

从 AssetBundle 中删除资源，选择 **None**，资源现在就变成为没有指定 AssetBundle 了。

<div style='display:none'>
To remove an AssetBundle Name from the list, all Assets assigned to that AssetBundle Name must be removed from that AssetBundle name, and then “Remove Unused Names” can be selected. This will remove all unused AssetBundle Names.
</div>

要从列表中删除一个  AssetBundle 名字，需要把所有指定到这个 AssetBundle 中的资源从 AssetBundle 名字中删除，然后选择 **Remove Unused Names**。这会删除所有没有被使用的 AssetBundle 名字。

![creat a new name](http://unity3d.com/sites/default/files/creating_a_new_ab_name.png)

<div style='display:none'>
descriptionCreating a new AssetBundle Name (Note Illegal Capital “T” in the AssetBundle Name)
</div>

<small>_创建一个新的 AssetBundle 名字（注意 大写的 "T" 在 AssetBundle 名字中非法）_</small>

<div style='display:none'>
Assets will be assigned to the AssetBundle selected in the AssetBundle Name menu. AssetBundle names are strictly lower case. If an uppercase letter is used, as in the example above, Unity will replace the capital letter with a lowercase one.
</div>

资源将会指定到在 AssetBundle 名字菜单中选择的 AssetBundle。AssetBundle 名字是严格小写的。如果使用了大写字母，就像上面的例子一样，Unity 将会用小写字母来代替。

![tank assign to ab](http://unity3d.com/sites/default/files/tank_assigned_to_ab.png)  
<div style='display:none'>
descriptionThe Tank Asset is now assigned to the AssetBundle “tank”.
</div>

<small>_坦克资源现在已经被指定到 "tanke" AssetBundle 上了_</small>

<div style='display:none'>
Note how the AssetBundle Name has been corrected to lowercase letters automatically.
</div>

注意 AssetBundle 的名字已经被自动纠正到了小写字母。

<div style='display:none'>
###USING ASSETBUNDLE VARIANTS

Being able to load Assets on demand from AssetBundles allows for many creative solutions to difficult issues related to loading, storing and updating Assets. One specific case where AssetBundles can help is the need to load a different set of Assets into a project depending upon the device, location or user preference. This is done by using AssetBundle Variants.
</div>

### 使用 AssetBundle 变体

从 AssetBundle 中按需加载资源的可能让很多困难问题有很多创意的解决方案，比如加载，存储和更新资源。一个典型的 AssetBunle 能有帮助的用例就是需要基于设备，位置或者用户习惯加载资源的项目。这个可以用 AssetBundle 变体来实现。

<div style='display:none'>
AssetBundle Variants deliver different versions of the same Asset to be assigned to an object in the scene. AssetBundle Variants completely remap different Assets to the same object. Only one Variant of an AssetBundle is ever loaded at any given time. Asset Variants can be created for many different situations. Asset Variants can be different resolutions of the same Asset: Standard Definition graphics vs High Definition graphics or models with different polycounts. Asset Variants can be created with different content for an object: text, images, textures and typefaces can be different for each supported language, region or theme. These Assets are saved in a series of identically constructed AssetBundles and identified by their Variant Name.
</div>

AssetBundle 变体提供场景中指定到一个对象上同一个资源的不同版本。AssetBundle 变体完全是重新映射不同的资源到同一个对象上。在同一时间只能有一种 AssetBundle 被加载。我们可以为不同的方案创建资源变体。同一个资源可以有不同分辨率的资源变体：标准图形 VS 高清图形或者不同多边形数的模型。可以为一个对象创建不同内容的资源变体：为每个支持语言，区域或主题的文字，图片，纹理和字体。这些资源都可以存储到一系列统一构建的 AssetBundle 中并用名字来区分他们。

<div style='display:none'>
For this to work, all of the matching AssetBundle Variants must be constructed and named identically. The only difference between AssetBundle Variants are the individual Assets contained in the AssetBundle and the AssetBundle Variant Name which is appended to the AssetBundle Name to identify it. To be a compatible AssetBundle Variant, the folder structure and contents of the AssetBundle must match. All the Assets need to be present in each AssetBundle, and must have the same name and in the same hierarchical order.
</div>

为了这些可以工作，所有匹配的 AssetBundle 变体必须构建和命名都一样。AssetBundle 变体间仅仅不同的地方就是 AssetBundle 内的资源和 加到 AssetBudle 后面的用来区分 AssetBundle 变体的名字。为了 AssetBundle 变体的兼容性，AssetBundle 的文件夹结构和内容需要匹配。所有的资源都要在 AssetBundle 里，具有相同的名字和在相同的分级顺利（hierarchial order）。

<div style='display:none'>
The following example can be found in the AssetBundle Sample.
</div>

下面的示例可以在  AssetBundle 示例中找到。

![variant structure](http://unity3d.com/sites/default/files/matching_variant_structure.png) 

<div style='display:none'>
descriptionExample of AssetBundle Variants.
</div>

<small>_AssetBundle 变体示例_</small>

<div style='display:none'>
In the above example, both folders - MyAssets-HD and MyAssets-SD - have been assigned to the AssetBundle Name “myassets”. Each then has been given an AssetBundle Variant Name to identify it, in these cases hd and sd, respectively. Note how the two sets of Assets have the same name and share the same hierarchical structure. As the parent directory has been assigned to an AssetBundle and none of the children have been assigned to an AssetBundle, all of the children will be added to the parent’s AssetBundle when it is built.
</div>

在上面的例子中，**MyAsset-HD** 和 **MyAssets-SD** 两个文件夹都被指定了 AssetBundle 名字 "myassets"。每个都给予了 AssetBundle 变体名字去区分他们，在这里分别是 `hd` 和 `sd`。注意两个资源集都有相同的名字和分级结构。父目录被指定到了一个 AssetBundle 而它所有的子对象都没有指定到 AssetBundle 中，当父目录被编译的时候，所有的子对象都会加到父目录的 AssetBundle 中。

![variant name hd](http://unity3d.com/sites/default/files/variant_name_hd.png) 

<small>_MyAsset-HD 设置了 AssetBundle 名字和变体名字_</small>

![variant name sd](http://unity3d.com/sites/default/files/variant_name_sd.png)

<small>_MyAssets-SD 设置了 AssetBundle 名字和变体名字_</small>

<div style='display:none'>	
descriptionMyAssets-HD with AssetBundle Name and AssetBundle Variant Name set.

descriptionMyAssets-SD with AssetBundle Name and AssetBundle Variant Name set.
</div>

<div style='display:none'>
It is worth noting that a hierarchical menu structure can be created for the AssetBundle Names. Note in the above images the AssetBundle Name has a path: variant/myassets. This will create a new menu item as a parent, called “variants” for the AssetBundle Name “myassets”.
</div>

注意，我们可以为 AssetBundle 名字创建层级菜单。上面的图片中 AssetBundle 名字有个路径：variant/myassets。 这会为 "myassets" 名字的 AssetBundle 创建一个 "variants" 名字为父级的新菜单项。

<div style='display:none'>	
descriptionAssetBundle Name with hierarchical menus.
</div>

<small>_层级菜单的 AssetBundle 名字_</small>

<div style='display:none'>
Once Assets have been assigned to AssetBundles, the AssetBundles will need to be built and tested.
</div>

一旦资源被指定到 AssetBundle, 这个 AssetBundle 将要被编译和测试。

<div style='display:none'>
###USING THE ASSETBUNDLE MANAGER

Unity has a Low-level API to work with AssetBundles directly. This tutorial will not cover the Low-level API. For more information on the Low-level AssetBundle API, please see the information linked below.
</div>

### 使用 AssetBundle Manager

Unity 提供了直接使用 AssetBundle 的底层 API. 但是这篇教程不会覆盖这些底层 API。关于底层 API 的更多信息，请阅读这个链接。

<div style='display:none'>
For building, testing and managing AssetBundles, this tutorial will concentrate on the AssetBundle Manger and its High-level API.
</div>

关于编译，测试和管理 AssetBundle，这篇教程会专注到 AssetBundle Manager 和它的高层 API 上。

<div style='display:none'>
The AssetBundle Manager is a downloadable package that can be installed in any current Unity project and will provide a High-level API and improved workflow for managing AssetBundles. The AssetBundle Manager can be downloaded here. To use the AssetBundle Manager in a project, simply add the AssetBundle Manager folder to the project’s Assets folder.
</div>

AssetBundle Manager 是一个可下载的，可以安装在当前 Unity 项目中的包，它提供高层 API 和改进了 AssetBundle 的流程。AssetBundle Manager 可以再 [这里](http://u3d.as/jyk) 下载。要在项目中使用 AssetBundle Manager，简单的将它加到当前的项目的 **Asset** 文件夹中。

<div style='display:none'>
Building and testing AssetBundles can be a pain-point during development. Assets are often changing on a regular basis. With the Low-level AssetBundle API, testing would require regular building and uploading of the AssetBundles to a remote host and testing these remotely hosted AssetBundles through a network connection with the working project. The AssetBundle Manager allows for a massively improved workflow compared to manipulating AssetBundles directly with the Low-level API. The AssetBundle Manager helps manage the key steps in building and testing AssetBundles. The key features provided by the AssetBundle Manager are a Simulation Mode, a Local AssetBundle Server and a quick menu item to Build AssetBundles to work seamlessly with the Local AssetBundle Server.
</div>

编译和测试 AssetBundle 可能是在开发过程中的一个痛点。资源会时常的改变。使用底层 AssetBunle API 时，测试需要规律的编译和上传 AssetBundle 到一个远程服务器上，然后从当我的项目建立一个网络连接来测试远程服务器上的 AssetBundle。相对于直接操作 AssetBundle 的底层 API, AssetBundle Manager 大幅度的优化了流程。AssetBundle Manager 提供的最核心的功能是一个模拟模式，一个本地的 AssetBundle 服务器和一些快捷的菜单去编译 AssetBundle 和无间隙地和本地 AssetBundle 服务器合作。

<div style='display:none'>
Adding the AssetBundle Manager to a project will create a new item in the Assets Menu called “AssetBundles”. 
</div>

把 AssetBundle Manager 加入到项目之后将会在 **Asset** 菜单中创建一个叫 **AssetBundles** 的新菜单项。

![assetbundle](http://unity3d.com/sites/default/files/assetbundle-menu.png)

<div style='display:none'>
descriptionAssets > AssetBundles
</div>

<small>_Assets > AssetBundles_</small>

<div style='display:none'>
Selecting the AssetBundles menu item will show a small selection of menu items.
</div>

选中 **AssetBundles** 菜单将会显示一个小菜单选项。

![assetbundle menu item](http://unity3d.com/sites/default/files/assetbundle_menu_item.png)  

<div style='display:none'>
descriptionAssets > AssetBundles menu items
</div>

<small>_Assets > AssetBundles 菜单项_</small>

<div style='display:none'>
Simulation Mode, when enabled, allows the editor to simulate AssetBundles without having to actually build them. To enable Simulation Mode, select the menu item “Simulation Mode”. A checkmark will appear indicating that Simulation Mode is enabled. To disable Simulation Mode, select the menu item again. Simulation Mode will be disabled and the check-mark will be removed.
</div>

模拟模式开启后，允许编辑器不用实际编译就可以模拟 AssetBundle。要打开模拟模式，选择 **Simulation Mode** 菜单项。对勾符号表示模拟模式已经开启。要关闭模拟模式就再选择一次菜单项目。然后对勾符号会被移除，模拟模式会被禁用。

<div style='display:none'>
With Simulation Mode enabled, the editor looks to see which Assets are assigned to AssetBundles and uses these Assets directly from the Project’s hierarchy as if they were in an AssetBundle. These AssetBundles, however, do not need to be built. From this point on, work within the editor can continue as if AssetBundles were built and hosted remotely.
</div>

当模拟模式开启后，编辑器会查看哪些资源被指定到了 AssetBundle，然后从项目的 hierarchy 中直接使用他们，就像他们在 AssetBundle 中一样。但是这些 AssetBundle 不需要编译。从这点来看，在编辑可以工作到了 AssetBundle 编译后放到远程服务器上一样可以工作。 

<div style='display:none'>
The huge advantage to the workflow when simulation mode is enabled is that Assets can be changed, manipulated, imported, removed and as long as they are correctly assigned to an AssetBundle, work on the project does not need to stop to build and deploy AssetBundles before testing. Testing with the Simulation Mode enabled is immediate.
</div>

开启模拟模式最大的好处是，只要资源被正确地指定到 AssetBundle ，在当前运行的项目测试前不需要停下来去编译和重新部署 AssetBundle 就可以修改，操作，导入，删除资源。当开启模拟模式之后，测试是马上生效的。

<div style='display:none'>
It is worth noting that AssetBundle Variants do not work under Simulation Mode. To test AssetBundle Variants, the AssetBundles will need to be built and deployed. AssetBundle Variants do work with the Local Asset Server, however.
</div>

注意 AssetBundle 变体在模拟模式下不支持。测试 AssetBundle 变体，AssetBundle 需要重新编译和部署。但是，本地的资源服务器支持 AssetBundle 变体。

<div style='display:none'>
The ABM can also enable a Local Asset Server for testing from either the editor or from local builds - including Mobile. When Local Asset Server is enabled, AssetBundles must be built and placed in a folder explicitly called “AssetBundles” in the root of the Project, which is on the same level as the “Assets” folder.
</div>

AssetBundle Manager 也可以开启一个本地资源服务器来从编辑器或者本地或移动端的 build 来测试。当本地资源服务器开启后，AssetBundle 必须编译，然后放到项目跟目录中，跟 **Assets** 文件夹同级的 **AssetBundles** 文件夹里。

![assetbundles folder](http://unity3d.com/sites/default/files/assetbundles_folder.png)  

<div style='display:none'>
descriptionThe location of the AssetBundles folder required by the Local Asset Server
</div>

<small>_本地资源服务器要求的 AssetBundes 文件夹位置_</small>

<div style='display:none'>
With the AssetBundles hosted locally, it is easy to access the Local Asset Server from the working project with a few simple lines of code. Please see the example in the AssetBundle Sample project, which will be covered later in this lesson.
</div>

AssetBundles 本地托管之后, 从当前项目中访问本地资源服务器只需要几行的代码就可以方便的访问。请阅读 AssetBundle 示例项目中的示例，我们会在教程的下面覆盖到。

<div style='display:none'>
Building AssetBundles and saving them into the “AssetBundles” folder on the root of the Project can be done simply by selecting “Build AssetBundles” from the “Assets/AssetBundles” menu. When “Build AssetBundles” is selected, Unity will build all of the AssetBundles that have had Assets assigned to them, compiling and optimizing them for the current build target, and finally saving them and a master Manifest to the “AssetBundles” folder in the root of the project. If there is no “AssetBundles” folder, Unity will make one. Inside the “AssetBundles” folder, the AssetBundles are organized by build target.
</div>

编译和保存到 AssetBundle 到项目根目录的 **AssetBundles** 文件夹中可以从 **Assets/AssetBundles** 菜单中选择 **Build AssetBundles** 来完成。当 **Build AssetBundles** 被选择之后， Unity 将会编译所有有资源指定的 AssetBundle, 然后为当前的平台编译和优化他们，最后保存他们和一个主清单到项目根目录下的 **AssetBundles** 文件夹下。如果没有 **AssetBundles**文件夹，Unity 会创建一个。在 **AssetBundles** 文件夹里，AssetBudle 按照编译目标平台来组织。

![grouped by target](http://unity3d.com/sites/default/files/grouped_by_target.png)

<div style='display:none'>
descriptionContents of the “AssetBundles” folder, grouped by build target.
</div>

<small>_"AssetBundles" 文件夹，按照编译目标平台来分组_</small>

<div style='display:none'>
With AssetBundles built and either deployed, or by enabling the Local AssetBundle Server, these AssetBundles can be downloaded and incorporated into a Project at run-time.
</div>

AssetBundle 被编译后部署到远程服务器或者开始本地资源服务器，这些 AssetBundles 可以在运行期下载和插入到项目中。


<div style='display:none'>
###USING ASSETBUNDLES IN PRACTICE

To use AssetBundles in practice, this lesson will be using the AssetBundle Manager. The AssetBundle Manager will take care of loading AssetBundles and their associated Asset Dependencies. To load Assets from AssetBundles using the AssetBundle Manager, a script needs to be written using the API provided by the AssetBundle Manager.
</div>

### AssetBundle 练习

练习 AssetBundle, 这教程将会使用 AssetBundle Manager。AssetBundle Manager 会应付 AssetBundle 的加载和他们相关的资源依赖。利用 AssetBundle Manager 来从 AssetBundle 中加载资源，脚本需要使用 AssetBundle Manager 提供的 API。

<div style='display:none'>
The AssetBundle Manager’s API includes:

* Initialize() Initializes the AssetBundle manifest object.
* LoadAssetAsync() Loads a given asset from a given AssetBundle and handles all the dependencies.
* LoadLevelAsync() Loads a given scene from a given AssetBundle and handles all the dependencies.
* LoadDependencies() Loads all the dependent AssetBundles for a given AssetBundle.
* BaseDownloadingURL Sets the base downloading url which is used for automatic downloading dependencies.
* SimulateAssetBundleInEditor Sets Simulation Mode in the Editor.
* Variants Sets the active variant.
* RemapVariantName() Resolves the correct AssetBundle according to the active variant.
</div>

AssetBundle Manager 的 API 包括：

* **Initialize()** 初始化 AssetBundle 清单对象
* **LoadAssetAsync()** 从指定的一个 AssetBundle 中加载资源并处理所有的依赖
* **LoadLevelAsync()** 从指定的一个 AssetBundle 中加载场景并处理所有的依赖
* **LoadDependencies()** 加载指定的 AssetBundle 的所有独立的 AssetBundle
* **BaseDownloadingURL** 设置用来自动下载依赖的基本地址
* **SimulateAssetBundleInEditor** 在编辑器中设置模拟模式
* **Vraiants** 设置当前的变体
* **RemapVariantName()** 根据当前的变体决定正确的 AssetBundle

<div style='display:none'>
Sample files are included with the AssetBundle Manager in a folder called "AssetBundle Sample". There are three basic sample scenes and one more advanced sample scene in the "AssetBundleSample/Scenes" folder:
</div>

示例文件放置在 AssetBundle Manager 内的 **AssetBundle Sample** 文件加下。有 3 个基础的示例场景和一个高级的示例场景在 **AssetBundleSample/Scenes** 文件夹下：

<div style='display:none'>
* "AssetLoader" demonstrates how to load a normal Asset from AssetBundles.
* "SceneLoader" demonstrates how to load a Scene from AssetBundles.
* "VariantLoader" demonstrates how to load AssetBundle Variants.
* “LoadTanks” is more advanced and will demonstrate a more complex example with loading a Scene, 
Assets and AssetBundle Variants into the same scene.
</div>

* "AssetLoader" 演示了怎么样从 AssetBundle 加载普通资源
* "SceneLoader" 演示了怎么样从 AssetBundle 加载场景
* "VariantLoader" 演示了怎么样加载 AssetBundle 变体
* "LoadTanks" 更高级，演示了复杂一点的，从同一个场景中加载场景，资源，和 AssetBundle 变体的示例。

<div style='display:none'>
Each one of these scenes is driven by a very basic script: LoadAssets.cs, LoadScenes.cs, LoadVariants.cs and LoadTanks.cs respectively.
</div>

每个场景都各个被非常基础的脚本驱动着：LoadAsset.cs，LoadScenes.cs，LoadVariants.cs 和 LoadTanks.cs。

<div style='display:none'>
At this point it is important to reiterate the workflow provided by the AssetBundle Manager.
</div>

当前重申一下 AssetBundle Manager 提供的流程还是很重要的。

<div style='display:none'>
To successfully test the use of AssetBundles, there are three possible scenarios.
</div>

为了能成功的试验 AssetBundle 的使用，这里有三种可能的情景：

<div style='display:none'>
In the first scenario, without using the AssetBundle Manager, AssetBundles will need to be built and deployed and all testing is done with the complete and final system in place. In this scenario, with every change to the Assets in a Project, new AssetBundles need to be built and deployed.
</div>

第一个情景，没有使用 AssetBundle Manager, AssetBundle 将需要被编译和部署，所有的测试都会在最终完整准备后完成。在这个场景中，每次项目中资源的改变，都需要编译和部署新的 AssetBundle。

<div style='display:none'>
There are two improvements to the workflow provided by the AssetBundle Manager. These are the Local AssetBundle Server and Simulation Mode.
</div>

AssetBundle Manager 在流程上提供了两个改进。他们是本地资源服务器和模拟模式。

<div style='display:none'>
In Simulation Mode, the AssetBundle Manager simulates built AssetBundles when running the Project within the editor. This is the fastest workflow to use. Simply enable “Simulation Mode” using the menu item “Assets/AssetBundles/Simulation Mode” and test the project. No AssetBundles will be built. It is important to note, however, that AssetBundle Variants do not work with Simulation Mode. It is also important to note that Assets can be manipulated in the project when Simulation Mode is enabled, and the effect of these changes can seen in the scene view, which will not be possible with deployed AssetBundles.
</div>

在模拟模式中，编辑器内运行项目时，AssetBundle Manager 会模拟编译后的 AssetBundles。这是使用 AssetBundle 的最快的流程。只需简单的使用 "Assets/AssetBundles/Simulation Mode" 菜单打开 "模拟模式", 然后测试项目。没有 AssetBundle 会被编译。尽管如此，要注意 AssetBundle 变体在模拟模式下不工作。还有要注意的是，模拟模式开始后，资源可以再项目中操作，并且改变后的效果在 Sence 视图中可以看到，而这使用部署后的 AssetBundle 是不行的。

<div style='display:none'>
The Local AssetBundle Server provides a more accurate representation of deployed AssetBundles, but requires that the AssetBundles be built and stored in a default folder within the project. When the Local AssetBundle Server is enabled, the built AssetBundles will be available to the Editor and all builds running locally that can reach the Editor on the local network. It is worth noting that this is the only way to test AssetBundle Variants locally.
</div>

本地资源服务器提供了部署的 AssetBundle 更精确的演示，但是需要 AssetBundle 被编译和存储到项目中的默认文件夹。当本地资源服务器开启之后，被编译的 AssetBundle 将可以被编辑器和所有运行在本地的，可以通过本地网络连接编辑器的 build 使用。注意这个是能本地测试 AssetBundle 变体的唯一方式。

<div style='display:none'>
To run one of the sample scenes, the AssetBundle Manager must be running in one of these modes. To run the AssetBundle Variant scene successfully, AssetBundles must be built and the Local AssetBundle Server must be enabled.
</div>

要运行示例场景，AssetBundle Manager 必须运行在这些模式中的一种。要成功运行 AssetBundle 变体，AssetBundle 必须被编译并且本地资源服务器必须被开启。

[译者：剩下的内容请关注本文的第三部分]

<hr>

文章连接：  
* [Unity 5: Asset Bundle 和 Asset Bundle Manager (1)]({filename}/AssetBundleAndABManage_1.md)  
* [Unity 5: Asset Bundle 和 Asset Bundle Manager (2)]({filename}/AssetBundleAndABManage_2.md)   
* [Unity 5: Asset Bundle 和 Asset Bundle Manager (3)]({filename}/AssetBundleAndABManage_3.md)  

