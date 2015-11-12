Title: Unity 5: 使用 Asset Bundle 和 Asset Bundle Manager (3)
Date: 2015-11-12 16:08:22
Modified: 2015-11 16:08:22
Category: Unity
Tags: Unity
Status: published
Keywords: Unity, Asset Bundle, Asset Bundle Manager

这篇是 Unity 官方教程 [AssetBundles and the AssetBundle Manager](http://unity3d.com/cn/learn/tutorials/topics/scripting/assetbundles-and-assetbundle-manager?playlist=17117) 的翻译， 分三部分，这是第三部分。翻译不到之处请不吝指出。非常谢谢！

译者注：英文太啰嗦了，但是还是坚持的把它翻译完了。因为啰嗦的好处是起码能让概念多复习几遍，更容易记得住。如果读者觉得啰嗦，可以自行执行 **跳读技能** 来阅读译文。

本文的项目连接：<http://u3d.as/jyk>
<hr>

<div style='display:none'>
###EXAMPLE 1: LOADING ASSETS

* Enable Simulation Mode using the menu item “Assets/AssetBundles/Simulation Mode”.
* Open the scene “AssetBundleSample/Scenes/AssetLoader”.
* Note that the scene is essentially empty and only contains a Main Camera, Directional 
 Light and “Loader” GameObject.
* Enter Playmode.
* Note that a cube has been loaded into the scene from an AssetBundle.

This scene is driven by the script “LoadAssets.cs”.
</div>

###示例 1：加载资源

* 使用 "Asset/AssetBundles/Simulation Mode" 菜单打开模拟模式
* 打开 "AssetBundleSample/Scenes/AssetLoader" 场景
* 注意场景是个空的只有一个主摄像机，方向光和游戏对象 "Loader"
* 进入 PlayMode
* 然后会注意到一个 cube 已经从 AssetBundle 加载到场景里面了

这个场景是被 "LoadAssts.cs" 脚本驱动的。

<div style='display:none'>
Open “AssetBundleSample/Scripts/LoadAssets.cs” in a script editor.
</div>

在脚本编辑器里面打开脚本 "AssetBundleSample/Scripts/LoadAssets.cs"

<div style='display:none'>
There are two public variables: public string assetBundleName; and public string assetName;
</div>

脚本里有两个公共变量： `public string assetBundleName;` 和 `public string assetName;`

<div style='display:none'>
* public string assetBundleName; holds the name of the AssetBundle to be loaded.
* public string assetName; holds the name of the Asset to be loaded from the loaded AssetBundle.
</div>

* **public string assetBundleName;** 保存了要被加载的 AssetBundle 的名字
* **public string assetName;** 保存了要已加载的 AssetBundle 中加载的资源的名字

<div style='display:none'>
The script comprises of a Start() function and two Coroutines, called from Start(). In Initialize(), DontDestroyOnLoad() is called, the path to the AssetBundles is set and the AssetBundle Manifest is initialized. In InstantiateGameObjectAsync() the Asset and AssetBundle name are requested using AssetBundleManager.LoadAssetAsync() and if the Asset requested is not null, it is instantiated.
</div>

这个脚本是由一个 `Start()` 函数和被 `Start()` 调用的两个协程组成的。`Initialize()` 调用了 `DontDestoryOnLoad()`, 设置了 AssetBundle 的路径和初始化了 AssetBundle 清单。在 `InstantiateGameObjectAsync()` 中，如果资源不为空，`AssetBundleManager.LoadAssetAsync()` 调用资源和 AssetBundle 的名字。

<div style='display:none'>
What is important to note here, by looking at the Asset “MyCube” in “AssetBundleSample/Assets” is that “MyCube” is dependent upon “MyMaterial” which is then dependent on “UnityLogo”. Only the Asset “MyCube” was requested, and all of the dependent Assets were correctly loaded.
</div>

重点注意下，在 "AssetBundleSample/Assets" 路径下查看 "MyCube" 资源，会发现 "MyCube" 依赖于 "MyMaterial"，而 "MyMaterial" 依赖于 "UnityLogo"。脚本中只有 "MyCube" 资源被调用，但是所有的依赖资源都被正确的加载了。

<div style='display:none'>
It is also worth noting how the path to the AssetBundles is being set. This code will set the location for the AssetBundles to the Local AssetBundle Server when the scene is running within the Editor or from a Development Build. (For more information on development builds, please see the documentation on publishing builds.) When working in the Editor while Simulation Mode is enabled, AssetBundles will be simulated and this setting will not be used.
</div>

AssetBundle 的路径怎么设置也值得注意下。当场景在编辑器中或者从一个开发版 Build 中运行时，这段代码会给本地资源服务器设置 AssetBundle 的位置。（更多关于开发版 Build，请查看[发布 Builds 文档](http://docs.unity3d.com/Manual/PublishingBuilds.html)。）模拟模式开启后，AssetBundle 会在编辑器中被模拟，这个设置将不会被使用。

<div style='display:none'>
To understand the use of DontDestroyOnLoad() it is worth understanding that even though this is a very simple script and in this context it is not absolutely necessary, it is present here with the assumption that this script will become the basis of an AssetBundle loader for a more complex project and will need to survive scene changes.
</div>

对 `DontDestoryOnLoad()` 作用的理解。虽然在这个非常简单的脚本中并不是绝对需要它，但是他的存在是假设这个脚本会作为一个更复杂的项目的 AssetBundle 加载器基础，它需要在场景变化的以后依然存在。

<div style='display:none'>
###EXAMPLE 2: LOADING SCENES

* Make sure Simulation Mode is enabled by using the menu item “Assets/AssetBundles/Simulation Mode”.
* Open the scene “AssetBundleSample/Scenes/SceneLoader”.
* Note that the scene is essentially empty and only contains a Main Camera, Directional Light and “Loader” GameObject.
* Enter Playmode.
* Note that a cube and a plane have been loaded into the scene from an AssetBundle.

This scene is driven by the script “LoadScenes.cs”.
</div>

###示例 2：加载场景

* 使用 "Asset/AssetBundles/Simulation Mode" 菜单打开模拟模式
* 开始 "AssetBundleSample/Scenes/SceneLoader" 场景
* 注意场景是个空的只有一个主摄像机，方向光和游戏对象 "Loader"
* 开打 PlayMode
* 然后会注意到一个 cube 和 plane 已经从 AssetBundle 加载到场景里面了

这个场景被 "LoadScene.cs" 脚本驱动着。

<div style='display:none'>
Open “AssetBundleSample/Scripts/LoadScenes.cs” in a script editor.
</div>

在脚本编辑其中打开 "AssetBundleSample/Scripts/LoadScenes.cs" 脚本。

<div style='display:none'>
There are two public variables: public string sceneAssetBundle; and public string sceneName;
</div>

脚本里有个两个公共变量：`public string sceneAssetBundle;` 和 `public string sceneName;`

<div style='display:none'>
* sceneAssetBundle; holds the name of the AssetBundle to be loaded.
* sceneName; holds the name of the Scene to be loaded from the loaded AssetBundle.
</div>

* **sceneAssetBundle;** 保持了要加载的 AssetBundle 的名字
* **sceneName;** 保持了要从已加载的 AssetBundle 里加载的场景的名字

<div style='display:none'>
The script comprises of a Start() function and two Coroutines, called from Start(). In Initialize(), DontDestroyOnLoad() is called, the path to the AssetBundles is set and the AssetBundle Manifest is initialized. In InitializeLevelAsync() the Scene name and isAdditive are used to request a Scene using AssetBundleManager.LoadLevelAsync(). If the Scene requested is null, the AssetBundle Manager will display an error in the console and the Coroutine ends.
</div>

这个脚本是有一个 `Start()` 函数和被 `Start()` 调用的两个协程组成的。`Initialize()` 调用了 `DontDestoryOnLoad()`, 设置了 AssetBundle 的路径和初始化了 AssetBundle 清单。在 `InitializeLevelAsync()` 里使用 `AssetBundleManager.LoadLevelAsync()` 调用场景名字和 `isAdditive` 来请求一个场景。如果场景为空，AssetManager 会在控制台显示出错误，然后协程结束。

<div style='display:none'>
What is important to note here, by looking at the Asset “MyCube” in “AssetBundleSample/Assets” is that “Cube” is dependent upon “MyMaterial” which is then dependent on “UnityLogo”. Only the Scene “TestScene” was requested. “Cube” was included in “TestScene” and all of the dependent Assets were correctly loaded by the AssetBundle Manager.
</div>

重点注意下，在 "AssetBundleSample/Assets" 路径下查看 "MyCube" 资源，会发现 "MyCube" 依赖于 "MyMaterial"，而 "MyMaterial" 依赖于 "UnityLogo"。只有 "TestScene" 场景被请求了。但在 “TestScene” 中的 "Cube" 和所有依赖的资源都被 AssetBundle Manager 正确的加载了。

<div style='display:none'>
It is also worth noting how the path to the AssetBundles is being set. This code will set the location for the AssetBundles to the Local AssetBundle Server when the scene is running within the Editor or from a Development Build. (For more information on development builds, please see the documentation on publishing builds.) When working in the Editor while Simulation Mode is enabled, AssetBundles will be simulated and this setting will not be used.
</div>

AssetBundle 的路径怎么设置也值得注意下。当场景在编辑器中或者从一个开发版 Build 中运行时，这段代码会给本地资源服务器设置 AssetBundle 的位置。（更多关于开发版 Build，请查看 [发布 Builds 文档](http://docs.unity3d.com/Manual/PublishingBuilds.html)。）模拟模式开启后，AssetBundle 会在编辑器中被模拟，这个设置将不会被使用。

<div style='display:none'>
To understand the use of DontDestroyOnLoad() it is worth understanding that even though this is a very simple script and in this context it is not absolutely necessary, it is present here with the assumption that this script will become the basis of an AssetBundle loader for a more complex project and will need to survive scene changes.
</div>

对 `DontDestoryOnLoad()` 作用的理解。虽然在这个非常简单的脚本中并不是绝对需要它，但是他的存在是假设这个脚本会作为一个更复杂的项目的 AssetBundle 加载器基础，它需要在场景变化的以后依然存在。

<div style='display:none'>
###EXAMPLE 3: VARIANTS

To work with AssetBundle Variants, the AssetBundles will need to be built, as AssetBundle Variants do not work with Simulation Mode. To build AssetBundles and their Variants, make sure all of the Assets are properly assigned to an AssetBundle Name and, if being used as an AssetBundle Variant, an appropriate AssetBundle Variant Name needs to be assigned as well.
</div>

###示例 3：变体

要使用 AssetBundle 变体，需要编译 AssetBundle, 因为模拟模式下不支持它。在编译 AssetBundle 和它的变体钱，确保所有的资源以及被正确地指定 AssetBundle 名字和如果要被 AssetBundle 变体利用到的话，AssetBundle 变体的名字也要指定。

![variant name hd](http://unity3d.com/sites/default/files/variant_name_hd.png){: width='40%'}

<div style='display:none'>
descriptionAn Asset with both AssetBundle Name and AssetBundle Variant Name set.
</div>

<small>同时拥有 AssetBundle 名字和 AssetBundle 变体名字的资源</small>

<div style='display:none'>
When all Assets have been assigned to an AssetBundle or AssetBundle Variant, AssetBundles can be built by selecting “Assets/AssetBundles/Build AssetBundles”.
</div>

当所有的资源都指定到 AssetBundle 或者 AssetBundle 变体后，选择 "Assets/AssetBundles/Build AssetBundles" 菜单来编译它们。

![build assetbundles](http://unity3d.com/sites/default/files/build_assetbundles.png){: width='50%'}

<div style='display:none'>
descriptionAssets/AssetBundles/Build AssetBundles
</div>

<small>_Assets/AssetBundles/BuildAssetBundles_</small>

<div style='display:none'>
By default, the AssetBundles will be optimized for the current build target and built into a folder called “AssetBundles” in the Project’s root directory, grouped by build target.
</div>

默认情况下，AssetBundle 会根据当前的平台优化，并编译进项目跟目录下的 "AssetBundles" 文件夹内，并按平台分组。

<div style='display:none'>
For ease of workflow and to use these newly built AssetBundles without deploying them, the Local AssetBundle Server should be enabled. Use “Assets/AssetBundles/Local AssetBundle Server” to enable the Local AssetBundle Server.
</div>

为了简化流程，不部署新编译出来的 AssetBundle 远程，需要开启本地资源服务器。通过 “Assets/AssetBundles/Local AssetBundle Server” 可以开启本地资源服务器。

![local assetbundles server](http://unity3d.com/sites/default/files/local_assetbundle_server.png){: width='50%'}

<div style='display:none'>
descriptionStarting the Local AssetBundle Server
</div>

<small>_启动本地资源服务器_</small>

<div style='display:none'>
This local server should run seamlessly, but, as with any network communication, the local server will have the same restrictions as any network communication and may be subject to permissions requirements, firewalls, and other limitations. Be aware that the Local AssetBundle Server is enabling a Local AssetBundle Server that is set to the default IP Address and Port, which is usually http://192.168.1.115:7888/. This information is temporarily stored in the file AssetBundleManager/Resources/AssetBundleServerURL. This information will be set or changed automatically by the AssetBundleManager, and should not need any attention by the user.
</div>

本地资源服务器应该想其他任何网络连接一样受限制，可能是权限需求，防火墙和其他限制。本地资源服务器启动时会被设置到默认 IP 地址和端口的本地资源访问的服务器，通常是 http://192.168.1.115:7888/. 这个只是暂时的，它被存储在 **AssetBundleManager/Resources/AssetBundleServerURL** 文件里面。这些信息会被 AssetBundleManager 设置或自动改变，用户不需要关注它们。

![assetbundle server url](http://unity3d.com/sites/default/files/assetbundle_serer_url.png){: width='25%'}  

<div style='display:none'>
descriptionAssetBundleServerURL contains the current URL and Port
</div>

<small>_包含当前 URL 和 端口的 AssetBundleServerURL_</small>

<div style='display:none'>
When the the Local AssetBundle Server is running, the built AssetBundles can be tested locally.
</div>

当本地资源服务器运行的时候，编译后 AssetBundle 可以被本地测试。

<div style='display:none'>
* Make sure Simulation Mode is disabled by using the menu item “Assets/AssetBundles/Simulation Mode”.
* Make sure the Local AssetBundle Server is enabled by using the menu item “Assets/AssetBundles/Local AssetBundle Server”.
* Open the scene “AssetBundleSample/Scenes/VariantLoader”.
* Note that the scene is essentially empty and only contains a Main Camera, Directional Light and “Loader” GameObject.
* Enter Playmode.
* Choose “Load SD”.
* Note that a cube and a Sprite have been loaded into the scene from an AssetBundle.
* Exit Playmode.
* Enter Playmode.
* Choose “Load HD”.
* Note that the same cube and Sprite have been loaded in the scene, but the Material, its dependent texture and the Sprite texture have been loaded from a different AssetBundle. The materials have different colors and the images are at a significantly higher resolution.
</div>

* 选择 “Assets/AssetBundles/Simulation Mode” 确保模拟模式被禁用了
* 选择 "Assets/AssetBundles/Local AssetBundle Server" 确保本地资源服务器开启
* 打开 "AssetBundleSample/Scenes/VariantLoader"
* 注意场景是个空的只有一个主摄像机，方向光和游戏对象 "Loader"
* 退出 PlayMode (如果在 PlayMode 下)
* 打开 PlayMode
* 选择 "Load HD"
* 注意同一个 Cube 和 Sprite 加载进场景了，但是材质和他依赖的独立纹理和 Sprite 纹理却从不同的 AssetBundle 加载。这些材质有不同的颜色，图片有更高的分辨率。

<div style='display:none'>
This scene is driven by the script “LoadVariants.cs”.
</div>

这个场景是被 "LoadVariant.cs" 脚本驱动的。

<div style='display:none'>
Open “AssetBundleSample/Scripts/LoadVariants.cs” in a script editor.
</div>

从编辑器中打开 "AssetBundleSample/Scripts/LoadVariants"。

<div style='display:none'>
This script is nearly identical to “LoadScenes.cs”. The main differences are the variable identifying the AssetBundle Variant to be loaded, and code to set the active Variant. There is additional code to create the UI Buttons.
</div>

这个脚本跟 "LoadScenes.cs" 几乎差不多。主要的区别就是用来区别需要加载的 AssetBundle 变体的变量和设置当前变体的代码。还有用来创建 UI 按钮的额外的代码。

<div style='display:none'>
* public string variantSceneAssetBundle; holds the name of the AssetBundle to be loaded.
* public string variantSceneName; holds the name of the Scene to be loaded from the loaded AssetBundle.
* private string[] activeVariants; holds the AssetBundleVariantNames to identify which AssetBundle Variants to load.
* private bool bundlesLoaded; is used to hide the UI when the Assets have been loaded.
</div>

* **public string variantSceneAssetBundle;** 保存要加载的 AssetBundle 的名字
* **public string variantSceneName;** 保存要从已加载的 AssetBundle 中加载的场景名字
* **private string[] activeVariants;** 保存用来区分需要加载的 AssetBundle 变体的 `AsssetBundleVariantNames`
* **private bool bundlesLoaded** 用来在加载完资源之后隐藏 UI

<div style='display:none'>
The script comprises of a BeginExample() function and two Coroutines, called from Start(). BeginExample is called by the “Load HD” or “Load SD” button in OnGUI. In Initialize(), DontDestroyOnLoad() is called, the path to the AssetBundles is set and the AssetBundle Manifest is initialized. In BeginExample(), between calling Initialize() and InitializeLevelAsync(), the active Variants are set. The value being set here is created by the “Load HD” or “Load SD” button in OnGUI. In InitializeLevelAsync() the Scene name and isAdditive are used to request a Scene using AssetBundleManager.LoadLevelAsync(). If the Scene requested is null, the AssetBundle Manager will display an error in the console and the Coroutine ends.
</div>

脚本由一个 `BeginExample()` 函数和被 `Start()` 调用的两个协程组成。 `BeginExample()` 在 `OnGUI()`函数中 被 `Load HD` 或者 `Load SD` 按钮调用。`Initialize()` 调用了 `DontDestoryOnLoad()`, 设置了 AssetBundle 的路径和初始化了 AssetBundle 清单。在 `BeginExample()` 方法里，在调用 `Initialize()` 和 `InitializeLevelAsync()` 之间，当前的变体被设置了。这里被设置的值从靠 `OnGUI` 里的 "Load HD" 或者 "Load SD" 按钮创建的。在 `InitializeLevelAsync()` 里使用 `AssetBundleManager.LoadLevelAsync()` 调用场景名字和 `isAdditive` 来请求一个场景。如果场景为空，AssetManager 会在控制台显式出错误，然后协程结束。

<div style='display:none'>
What is important to note here is how AssetBundle Variants are loaded. The array activeVariants contains a list of all of the possible Variant Names that are “active”. This array is used to set the AssetBundleManager.ActiveVariants property. When loading an AssetBundle that has a variant, the AssetBundle Manager will choose the AssetBundles that have “active” Variant Names in the ActiveVariants property. In the current example the ActiveVariants property contains only one element; the Active Variant is either “sd” or “hd”. It is possible to have multiple entries in the ActiveVariants property. For example there could be the following AssetBundles: my-material.sd, my-material.hd, my-text.english, my-text.danish, my-text.catalan, my-text.welsh. The ActiveVariants property could contain both “hd” and “danish”, or “sd” and “english” and so on for any of the other possible combinations of these Variant Names. This way, the AssetBundle Manager can load hd/sd images and the language choices separate from each other.
</div>

这里需要重视的是 AssetBundle 变体是怎么样加载的。**activeVariants** 数组包含了所有可能的 “激活的” 变量名列表。这个数组用来设置 **AssetBundleManager.ActiveVariants** 属性。当加载一个含有变体的 AssetBundle 时，AssetBundle Manager 将会选择在 **ActiveVariants** 属性里含有 “激活” 的变体名字的 AssetBundle。当前的示例中，**ActiveVariants** 属性只包含一个元素。当前的变体要么是 "sd"，要么是 “hd”。在 **ActiveVariants** 属性中有多个实体是有可能的。比如，可能有下面一些 AssetBundle: my-material.sd，my-material.hd， my-text.english，my-text.catalan，my-text.welsh。**ActiveVariants** 属性可以包含 “hd” 和 “danish” 两者或者 “sd” 和 "english" 等等任何可以有其他可能组合的变体名。这种方式下，AssetBundle Manager 分开可以加载 hd/sd 图片和语言选择。

<div style='display:none'>
There are some rules to this that are worth noting. If, for some reason, there are AssetBundles that have Variants assigned, but no Active Variant Name is set in the ActiveVariants property- for example neither “sd” nor “hd” are in the ActiveVariants property for the current example - the AssetBundle Manager will simply use the first AssetBundle it finds with the correct AssetBundle Name, ignoring the Variant Name. If, for some reason, there are multiple Active Variant Names in the ActiveVariants property for the same set of AssetBundles - for example, both “sd” and “hd” are in the ActiveVariants property for the current example - the AssetBundle Manager will choose the AssetBundle Variant whose Variant Name comes first in the ActiveVariants property.
</div>

有些规则值得注意下。如果，因为一些因素，有一些指定了变体的 AssetBundle，但是在 **ActiveVariants** 属性里没有 “激活” 的变体名 - 比如当前例子中的 “sd” 或者 “hd” 不在 **ActiveVraiants** 属性中 - AssetBundle Manager 将会简单的选择第一个它发现的正确名字的 AssetBundle 而忽略变体名。再如果，又因为一些因素，在 **ActiveVariants** 属性里对同一个 AssetBundle 集合有多个 “激活” 的变体名 - 比如， 在当前的例子里，“sd” 和 “hd” 都在 **ActiveVariants** 属性里 - AssetBundle Manager 将选择在 **ActiveVariants** 属性中的第一个变体名。

<div style='display:none'>
###EXAMPLE 4: TANKS EXAMPLE

This more complex example will sum up everything in this article, including loading a scene from an AssetBundle and loading AssetBundle Variants for resolution, content and localization.
</div>

###示例 4：坦克示例

这个更复杂的示例将包括这篇文章中的所有内容，包括从 AssetBundle 中加载场景和为分辨率，内容和位置加载 AssetBundle 变体。

<div style='display:none'>
* Make sure Simulation Mode is disabled by using the menu item “Assets/AssetBundles/Simulation Mode”.
* Make sure the Local AssetBundle Server is enabled by using the menu item “Assets/AssetBundles/Local AssetBundle Server”.
* Open the scene “AssetBundleSample/Scenes/TanksLoader”.
* Note that the scene is essentially empty and only contains only the “Loader” GameObject.
* Enter Playmode.
* Select one choice for resolution, style and language.
* Note that the assets loaded are the options chosen in the UI.
* Note that if none of the choices are explicitly chosen, the AssetBundleManager will choose one automatically (as per the rules above) and print a warning in the console.
</div>

* 选择 “Assets/AssetBundles/Simulation Mode” 确保模拟模式被禁用了
* 选择 "Assets/AssetBundles/Local AssetBundle Server" 确保本地资源服务器开启
* 打开 "AssetBundleSample/Scenes/TanksLoader"
* 注意场景是个空的只有一个主摄像机，方向光和游戏对象 "Loader"
* 进入 PlayMode
* 选择一个分辨率，风格和语言
* 注意在 UI 里的选择项就是加载的资源
* 如果没有显式的选择一个，AssetBundleManager 将自动选择（基于上面的原则）一个并且在命令行输出一个警告。

<div style='display:none'>
This scene is driven by the script “LoadTanks.cs”.
</div>

场景靠 "LoadTanks.cs" 脚本驱动。

<div style='display:none'>
Open “AssetBundleSample/Scripts/LoadTanks.cs” in a script editor.
</div>

在编辑器里面打开 “AssetBundleSample/Scripts/LoadTanks.cs” 脚本。

<div style='display:none'>
This script is very similar to “LoadScenes.cs” and “LoadAssets.cs”. This script uses code to both load a scene which depends upon a variant and to load an additional GameObject that also depends upon a variant. There is additional code to create the UI Buttons.
</div>

这个脚本与 “LoadScenes.cs” 和 "LoadAssets.cs" 非常像。脚本使用代码去加载依赖变体的场景和一样依赖变体的额外的游戏对象。也有一些额外的代码创建 UI 按钮。

<div style='display:none'>
* public string sceneAssetBundle; holds the name of the Scene bearing AssetBundle to be loaded.
* public string sceneName; holds the name of the Scene to be loaded from the loaded AssetBundle.
* public string textAssetBundle; holds the name of the Text Asset bearing AssetBundle to be loaded.
* public string textAssetName; holds the name of the Text Asset to be loaded from the loaded AssetBundle.
* private string[] activeVariants; holds the ActiveVariants to pass to the AssetBundleManager.
* private bool bundlesLoaded; is used to hide the UI when the Assets have been loaded.
* private bool sd, hd, normal, desert, english, danish; holds values used to set the ActiveVariant.
* private string tankAlbedoStyle, tankAlbedoResolution, language; holds values used to set the ActiveVariant.
</div>

* **public string sceneAssetBundle;** 保存携带场景的 AssetBundle 的名字
* **public string sceneName;** 保存要从已加载的 AssetBundle 中加载的场景名字。
* **public string textAssetBundle;** 保存携带文字资源的 AssetBundle 的名字
* **public string textAssetName;** 保存要从已加载的 AssetBundle 中加载的文字资源的名字
* **private string activeVariants;** 保存要传给 AssetBundleManager 的 `ActiveVariants`
* **private bool bundlesLoaded;** 用来资源加载之后隐藏 UI
* **private bool sd, hd, normal, desert, englisth, danish;** 保存用来设置 `ActiveVariants` 的值
* **private string tankAlbedoStyle, tankAlbedoResolution, languge;** 保存用来设置 `ActiveVariants` 的值

<div style='display:none'>
The script comprises of a BeginExample() function and three Coroutines, called from Start(). The BeginExample() function is called by the button “Load Scene” in OnGUI(). In Initialize(), DontDestroyOnLoad() is called, the path to the AssetBundles is set and the AssetBundle Manifest is initialized. In BeginExample(), between calling Initialize() and InitializeLevelAsync(), the active Variants are set. The value being set here is created by the button “Load Scene” based on the user input in OnGUI(). In InitializeLevelAsync() the Scene name and isAdditive are used to request a Scene using AssetBundleManager.LoadLevelAsync(). If the Scene requested is null, the AssetBundle Manager will display an error in the console and the Coroutine ends. In InstantiateGameObjectAsync() the Asset and AssetBundle name are requested using AssetBundleManager.LoadAssetAsync() and if the Asset requested is not null, it is instantiated. If the AssetBundle cannot be loaded or the Asset cannot be requested, an error will be printed in the console.
</div>

脚本由一个 `BeginExample()` 函数和被 `Start()` 调用的两个协程组成。 `BeginExample()` 在 `OnGUI()`函数中 被 "Load Scene" 按钮调用。`Initialize()` 调用了 `DontDestoryOnLoad()`, 设置了 AssetBundle 的路径和初始化了 AssetBundle 清单。在 `BeginExample()` 方法里，在调用 `Initialize()` 和 `InitializeLevelAsync()` 之间，当前的变体被设置了。这里被设置的值从靠 `OnGUI` 里的 "Load Scene" 按钮创建的。在 `InitializeLevelAsync()` 里使用 `AssetBundleManager.LoadLevelAsync()` 调用场景名字和 `isAdditive` 来请求一个场景。如果场景为空，AssetManager 会在控制台显式出错误，然后协程结束。在 `InstantiateGameObjectAsync()` 中资源和 AssetBundle 名字被 `AssetBundleManager.LoadAssetAsync()` 调用。如果调用的资源不为空，它会被实例化。如果 AssetBundle 不能被加载或者资源不能被请求，控制台会打印出错误来。

<div style='display:none'>
What is important to note here is how several Asset, AssetBundles and AssetBundleVariants are being accessed and loaded in this scene, and how these values can be set at run-time.
</div>

这小结要注意的内容是，多个 资源，AssetBunle 和 AssetBunle 变体怎么被访问和加载进场景里，和怎么样在运行期设置这些值。

<hr>

文章连接：  
* [Unity 5: Asset Bundle 和 Asset Bundle Manager (1)]({filename}/AssetBundleAndABManage_1.md)  
* [Unity 5: Asset Bundle 和 Asset Bundle Manager (2)]({filename}/AssetBundleAndABManage_2.md)  
* [Unity 5: Asset Bundle 和 Asset Bundle Manager (3)]({filename}/AssetBundleAndABManage_3.md)  
