title: 资产, 对象和序列化
date: 2016-12-15 17:40:00
category: UnityKB
tags: AssetBundle
---

<div style='display:none'>
This is the second chapter in a [series of articles covering Assets, Resources and resource management](https://unity3d.com/learn/tutorials/topics/best-practices/guide-asset-bundles-and-resources/) in Unity 5.
</div>

这是 Unity 5 {% post_link GuideToABAndRes [资产, 资源和资源管理系列文章] %}的第二篇。

<div style='display:none'>
This chapter covers the deep internals of Unity's serialization system and how Unity maintains robust references between different Objects, both in the Unity Editor and at runtime. It also discusses the technical distinctions between Objects and Assets. The topics covered here are fundamental to understanding how to efficiently load and unload Assets in Unity. Proper Asset management is crucial to keeping loading times short and memory usage low.
</div>

这篇文章涵盖了 Unity 序列化系统的底层知识和 Unity  怎么在它的编辑器及运行时维持不同对象的稳定的引用，理解怎么样在 Unity 中高效的加载和卸载资产。正确的资产管理是保持低内存和快速加载的关键。

<div style='display:none'>
### 1. Inside Assets and Objects
</div>

### 资产和对象的内部

<div style='display:none'>
To understand how to properly manage data in Unity, it is important to understand how Unity identifies and serializes data. The first key point is the distinction between Assets and __UnityEngine.Objects__.
</div>

要理解怎么样正确的管理数据，Unity 怎么鉴别和序列化数据很重要。其中首先的关键点是理解 __资产__ 和 __对象（UnityEngine.Objects）__ 的区别。

<div style='display:none'>
An Asset is a file on disk, stored in the Assets folder of a Unity project. For example, texture files, material files and FBX files are all Assets. Some Assets contain data in formats native to Unity, such as materials. Other Assets need to be processed into native formats, such as FBX files.
</div>

一个资产是存储在 Unity Project 中资产文件夹下的文件。比如纹理文件，材质文件和 FBX 文件都是资产。有些资产包含 Unity 原生数据格式，比如材质。而有些资产需要转换成 Unity 原生数据格式，比如 FBX 文件。

<div style='display:none'>
A __UnityEngine.Object__, or __Object__ with a capitalized 'O', is a set of serialized data collectively describing a specific instance of a resource. This can be any type of resource which the Unity Engine uses, such as a mesh, a sprite, an AudioClip or an AnimationClip. All Objects are subclasses of the [UnityEngine.Object](http://docs.unity3d.com/ScriptReference/Object.html) base class.
</div>

一个 __UnityEngine.Object__ 或者大写字母 O 的 __Object__，是个序列化数据集合，用来表述某个资源的具体实例。它可以是任何 Unity 引擎使用的资源，比如一个网格，一个精灵，一个音频剪辑和一个动画片段。所有的对象都是 [UnityEngine.Object](http://docs.unity3d.com/ScriptReference/Object.html) 的子类。

<div style='display:none'>
While most Object types are built-in, there are two special types.
</div>

在 Unity 中基本所有的对象类型都是内置的，除了两种特殊的类型。
<!-- more -->
<div style='display:none'>
1. A [ScriptableObject](http://docs.unity3d.com/ScriptReference/ScriptableObject.html) provides a convenient system for developers to define their own data types. These types can be natively serialized and deserialized by Unity, and manipulated in the Unity Editor's Inspector window.
2. A [MonoBehaviour](http://docs.unity3d.com/ScriptReference/MonoBehaviour.html) provides a wrapper that links to a [MonoScript](http://docs.unity3d.com/ScriptReference/MonoScript.html). A MonoScript is an internal data type that Unity uses to hold a reference to a specific scripting class within a specific assembly and namespace. The MonoScript does not contain any actual executable code.
</div>

1. [ScriptableObject](http://docs.unity3d.com/ScriptReference/ScriptableObject.html) 给开发者提供了一个便捷的，可以定义自己数据类型的系统。这些类型能被 Unity 序列化和反序列化和在 Unity 编辑器的 Inspector Window 中使用。
2. A [MonoBehaviour](http://docs.unity3d.com/ScriptReference/MonoBehaviour.html) 提供了一个链接到 [MonoScript](http://docs.unity3d.com/ScriptReference/MonoScript.html) 的封装。MonoScript 是一个内置的数据类型，在 Unity 中用来保持程序集或者命名空间中一个脚本的引用。MonoSript 不包含任何可以执行的代码。

<div style='display:none'>
#### 1.2. Inter-Object references
</div>

### 内置对象的引用

<div style='display:none'>
All UnityEngine.Objects can have references to other UnityEngine.Objects. These other Objects may reside within the same Asset file, or may be imported from other Asset files. For example, a material Object usually has one or more references to texture Objects. These texture Objects are generally imported from one or more texture Asset files (such as PNGs or JPGs).
</div>

所有的 UnityEngine.Objects 都能拥有其他 UnityEngine.Objects 的引用。而这些其他的 UnityEngine.Objects 可能同一个资产文件，或者从其他资产文件中导入。比如，一个材质对象通常拥有一个或者多个纹理对象的引用。这些纹理对象一般都是从一个或者多个纹理资产文件中导入的（比如 PNG 和 JPG 文件）。

<div style='display:none'>
When serialized, these references consist of two separate pieces of data: a __File GUID__ and a __Local ID__. The File GUID identifies the Asset file where the target resource is stored. A locally unique Local ID identifies each Object within an Asset file because an Asset file may contain multiple Objects.
</div>

当被序列化之后，由两部分数据组成了这些引用：一个是 __文件 GUID__ 另外一个是 __本地 ID__。文件 GUID 用来 标识目标资源存储位置下的资产文件。本地ID（唯一的 <a href='#f1'>[1]</a>）用来标识一个资产文件中的每个对象，因为一个资产文件可能包含多个对象。

<div style='display:none'>
File GUIDs are stored in .meta files. These .meta files are generated when Unity first imports an Asset, and are stored in the same directory as the Asset.
</div>

文件 GUID 存储在 .meta 文件中。这些 .meata 文件在 Unity 导入资产的时候创建，存储在和资产文件同一个目录中。

<div style='display:none'>
The above identification and referencing system can be seen in a text editor: create a fresh Unity project and change its Editor Settings to expose Visible Meta Files and to serialize Assets as text. Create a material and import a texture into the project. Assign the material to a cube in the scene and save the scene.
</div>

上面提到的鉴别和引用系统可以在文本编辑器中看到：创建一个新 Unity 项目，然后将 __编辑器__ 设置为 __Visible Meta Files__ 和 __序列化为文本__。然后创建一个材质和导入一个纹理到项目中。将新创建的材质指定到场景中的一个立方体上面，然后保存场景。

<div style='display:none'>
Using a text editor, open the .meta file associated with the material. A line labeled "guid" will appear near the top of the file. This line defines the material Asset's File GUID. To find the Local ID, open the material file in a text editor. The material Object's definition will look like this:
</div>

我们用文本编辑器打开和材质关联的 .meta 文件。在文件头部会有标识了 “guid” 的行。这行定义了材质的文件 GUID。查找本地 ID, 我们可以在文本编辑器中打开材质文件。我们会看到类似于如下所示的材质对象的定义：

> --- !u!21 &2100000  
> Material:  
>  serializedVersion: 3  
>  ... more data ...  

<div style='display:none'>
In the above example, the number preceded by an ampersand is the material's Local ID. If this material Object were located inside an Asset identified by the File GUID "abcdefg", then the material Object could be uniquely identified as the combination of the File GUID "abcdefg" and the Local ID "2100000".
</div>


在上面的例子中，前面带 & 符号的数字就是材质的本地 ID。如果一个材质对象在一个文件 GUID 为 `abcdefg` 的资产里面，这个材质对象就可以用文件 GUID `abcdefg` 和本地 ID `2100000` 组合唯一地标识。

<div style='display:none'>
### 1.3. Why File GUIDs and Local IDs?
</div>

### 为什么要文件 GUID 和本地 ID

<div style='display:none'>
Why is Unity's File GUID and Local ID system necessary? The answer is robustness and to provide a flexible, platform-independent workflow.
</div>

为什么需要 Unity 的文件 GUID 和本地 ID 系统？答案是为了健壮性和提供一个灵活和平台独立的工作流。

<div style='display:none'>
The File GUID provides an abstraction of a file's specific location. As long as a specific File GUID can be associated with a specific file, that file's location on disk becomes irrelevant. The file can be freely moved without having to update all Objects referring to the file.
</div>

文件 GUID 提供了文件位置的抽象。只要文件 GUID 和一个文件关联上，那文件在磁盘上的位置就变得无关紧要了。这个文件可以随意移动，而不必更新所有引用了该文件的对象。

<div style='display:none'>
As any given Asset file may contain (or produce via import) multiple UnityEngine.Object resources, a Local ID is required to unambiguously distinguish each distinct Object.
</div>

一个资产文件可能包含多个 UnityEngine.Object，为了清楚的区分它们，需要本地 ID。

<div style='display:none'>
If the File GUID associated with an Asset file is lost, then references to all Objects in that Asset file will also be lost. This is why it is important that the .meta files must remain stored with the same filenames and in the same folders as their associated Asset files. Note that Unity will regenerate deleted or misplaced .meta files.
</div>

如果和资产文件相关的文件 GUID 丢失了，所有对象对这个文件的引用就会丢失。这就是为什么 .meta 文件必须和它们相关联的资产文件存储在同一个位置，并且拥有相同的文件名很重要。注意 Unity 会重新生成被删除的或者被乱放的 .meta 文件。

<div style='display:none'>
The Unity Editor has a map of specific file paths to known File GUIDs. A map entry is recorded whenever an Asset is loaded or imported. The map entry links the Asset's specific path to the Asset's File GUID. If the Unity Editor is open when a .meta file goes missing and the Asset's path does not change, the Editor can ensure that the Asset retains the same File GUID.
</div>

Unity 编辑器拥有已知文件 GUID 到文件路径的映射。这个映射实体会把资产的文件路径和文件 GUID 关联起来。如果 Unity 编辑器打开时，一个 .meta 文件丢失而资产的路径并没有改变的资产，编辑器会确保这个资产得到相同的文件 GUID。

<div style='display:none'>
If the .meta file is lost while the Unity Editor is closed, or the Asset's path changes without the .meta file moving along with the Asset, then all references to Objects within that Asset will be broken.
</div>

如果 .meta 文件在 Unity Editor 关闭时丢失，或者资产的路径变化时没有把 .meta 文件一起跟资产文件移动，所有对资产内对象的引用都会丢失。

<div style='display:none'>
### 1.4. Composite Assets and importers
</div>

### 组合资产和 Importers 

<div style='display:none'>
As mentioned in the [Inside Assets and Objects](https://unity3d.com/cn/learn/tutorials/topics/best-practices/assets-objects-and-serialization#Inside_Assets_and_Objects) section, non-native Asset types must be imported into Unity. This is done via an asset importer. While these importers are usually invoked automatically, they are also exposed to scripts via the [AssetImporter](http://docs.unity3d.com/ScriptReference/AssetImporter.html) API, and its subclasses. For example, the TextureImporter API provides access to the settings used when importing individual texture Assets, such as PNGs and JPGs.
</div>

在 [资产和对象的内部](https://unity3d.com/cn/learn/tutorials/topics/best-practices/assets-objects-and-serialization#Inside_Assets_and_Objects) 章节中提到，非原生的资产类型需要导入到 Unity 中。这是靠 Assets Importer 完成的。这些 Importers 都是自动调用的，他们靠 [AssetImporter](http://docs.unity3d.com/ScriptReference/AssetImporter.html) API 和它的子类来暴露给脚本。比如，TextureImporter API 提供了导入 PNG 和 JPG 等纹理资产时的设置访问。

<div style='display:none'>
The result of the import process is one or more UnityEngine.Objects. These are visible in the Unity Editor as multiple sub-assets within the parent Asset, such as multiple sprites nested beneath a texture Asset that has been imported as a sprite atlas. Each of these Objects will share a File GUID as their source data is stored within the same Asset file. They will be distinguished within the imported texture Asset by a Local ID.
</div>

导入过程的结果是一个或者多个 UnityEngine.Objects。这些对象在 Unity 编辑器中显示为一个资产的子资产。比如设置成精灵图集方式导入纹理资产，会有多个精灵嵌套在这个资产下。这些精灵对象会共享一个文件 UIID 作为他们的源资产文件。而在导入的纹理资产中靠本地 ID 来区分他们。

<div style='display:none'>
The import process converts source Assets into formats suitable for the target platform selected in the Unity Editor. The import process can include a number of heavyweight operations, such as texture compression. It would be extremely inefficient to run the import process every time the Unity Editor was opened.
</div>

导入过程会将源资产文件转换成在 Unity 编辑器中选中的目标平台合适的格式。导入过程也可能会带有比较重的操作，比如纹理压缩。如果每次 Unity 编辑器打开的时候都要执行导入过程的话会是 Unity 编辑器变得特别没有效率。

<div style='display:none'>
Instead, the results of Asset importing are cached in the Library folder. Specifically, the results of the import process are stored in a folder named for the first two digits of the Asset's File GUID. This folder is stored inside the Library/metadata/ folder. The individual Objects are serialized into a single binary file that has a name identical to the Asset's File GUID.
</div>

作为解决方案，Unity 会讲资产导入后的结果缓存到 Libraray 文件夹。导入后的结果会缓存到以资产的文件 GUID 前两个字母命名的文件夹中。这个文件夹在 Library/metadat/ 文件夹内。每个独立的对象都会被序列化为单独的以它们资产文件 GUID 命名的二进制文件。

<div style='display:none'>
This is actually true for all Assets, not just non-native Assets. However, native assets do not require lengthy conversion processes or re-serialization.
</div>

这对所有的资产都适用，而不仅仅是非原生的资产。但是原生的资产不需要做长时间的转换或者重新序列化。

<div style='display:none'>
### 1.5. Serialization and instances
</div>

### 序列化和实例

<div style='display:none'>
While File GUIDs and Local IDs are robust, GUID comparisons are slow and a more performant system is needed at runtime. Unity internally maintains a cache(2) that translates File GUIDs and Local IDs into simple integers that are unique only during a single session. These are called Instance IDs, and are assigned in a simple, monotonically-increasing order when new Objects are registered with the cache.
</div>

文件 GUID 和本地 ID 系统健壮的同时，GUID 的比较是比较慢的，这就需要一个在运行期时更高效的系统。Unity 内部维持了一个能把文件 GUID 和本地 ID 换成在独立会话内唯一的，简单的数字的缓存<a href='#f2'>[2]</a>。这个数字叫做实例 ID。当新的对象注册到缓存时，会给它分配一个严格递增的值。

<div style='display:none'>
The cache maintains mappings between a given Instance ID, the File GUID and Local ID defining the location of the Object's source data, and the instance of the Object in memory (if any). This allows UnityEngine.Objects to robustly maintain references to each other. Resolving an Instance ID reference can quickly return the loaded Object represented by the Instance ID. If the target Object is not yet loaded, the File GUID and Local ID can be resolved to the Object's source data and Unity can then load the object just-in-time.
</div>

这个缓存维护了给定的实例 ID、对象源文件中定义的文件 GUID 和本地 ID 和内存中对象（如果有的话）的映射关系。它让 UnityEngine.Objects 稳定的维护各个对象间的引用成为可能。通过一个实例 ID 的引用可以快速的返回这个 ID 对应的对象。如果这个对象没有加载，Unity 就可以根据 FileID 和本地  ID 来实时的加载对象。

<div style='display:none'>
At startup, the Instance ID cache is initialized with data for all Objects that are built-in to the project (i.e. referenced in Scenes), as well as all Objects contained in the Resources folder. Additional entries are added to the cache when new assets are imported at runtime(3) and when Objects are loaded from AssetBundles. Instance ID entries are only removed from the cache when they become stale. This happens when an AssetBundle providing access to a specific File GUID and Local ID is unloaded.
</div>

在启动的时候，实例 ID 缓存会初始化所有被场景引用的的对象和 Resources 文件夹下的所有对象数据。运行时导入的新资产<a href='#f3'>[3]</a>和从 AssetBundles 里面加载的对象会被额外的添加到缓存中。当实例 ID 不在有用的时候他们会从缓存中移除。当一个 AssetBunld 访问未加载的文件 GUID 和本地 ID 时会生这种情况。

<div style='display:none'>
When the unloading of an AssetBundle causes an Instance ID to become stale, the mapping between the Instance ID and its File GUID and Local ID is deleted to conserve memory. If the AssetBundle is re-loaded, a new Instance ID will be created for each Object loaded from the re-loaded AssetBundle.
</div>

卸载 AssetBundle 时引起实例 ID 无效时，为了节省内存，实例 ID 和文件 GUID 及 本地 ID 间的映射将会被移除。当 AssetBundle 重新被加载时，将会给从 AssetBundle 中重新加载的对象分配一个新的实例 ID。

<div style='display:none'>
For a deeper discussion of the implications of unloading AssetBundles, see the [Managing Loaded Assets](https://unity3d.com/ru/learn/tutorials/topics/best-practices/asset-bundle-usage-patterns#Managing_Loaded_Assets) section in the [AssetBundle Usage Patterns](https://unity3d.com/ru/learn/tutorials/topics/best-practices/asset-bundle-usage-patterns) article.
</div>

更深入的探讨卸载 AssetBundles 带来的问题，可以参照 [AssetBundle 使用模式](https://unity3d.com/ru/learn/tutorials/topics/best-practices/asset-bundle-usage-patterns) 中的  [管理加载的资产](https://unity3d.com/ru/learn/tutorials/topics/best-practices/asset-bundle-usage-patterns#Managing_Loaded_Assets) 这一节。

<div style='display:none'>
Note that certain events on specific platforms can force Objects out of memory. For example, graphical Assets can be unloaded from graphics memory on iOS when an app is suspended. If these Objects originated in an AssetBundle that has been unloaded, Unity will be unable to reload the source data for the Objects. Any extant references to these Objects will also be invalid. In the preceding example, this would appear as invisible (missing) meshes or models rendering with magenta (missing) textures & materials.
</div>

注意，在某些平台上的特定的事件会强制从内存中删除对象。比如，在 iOS平台，当程序挂起的时候，可以从图形内存里面卸载图形资产。如果这些对象是从已卸载的 AssetBundle 里加载的，Unity 将会无法从对象的源数据重新加载对象了。所有对这些对象的引用也会变成无效。在这个例子中可能会出现看不见的网格或者模型带有洋红色的纹理和材质的现象。

<div style='display:none'>
Implementation note: At runtime, the above control flow is not literally accurate. Comparing File GUIDs and Local IDs at runtime would not be sufficiently performant during heavy loading operations. When building a Unity project, the File GUIDs and Local IDs are deterministically mapped into a simpler format. However, the concept remains identical, and thinking in terms of File GUIDs and Local IDs remains a useful analogy during runtime.
</div>

__提示：__ 在运行时，上述控制流程不是特别精确。对于重度加载操作，比较文件 GUID 和本地 ID 是非常不高效的。当构建一个 Unity 项目时，文件 GUID 和本地 ID 都被映射到了一个简单的格式上。但是概念依然一样，运行时考虑使用文件 GUID 和本地 ID 来做对比依然很有用。

<div style='display:none'>
This is also the reason why Asset File GUIDs cannot be queried at runtime.
</div>

这也是为什么资产的文件 GUID 不能再运行时查询的一个原因。（因为被转换成了其他简单格式。）

<div style='display:none'>
### 1.6. MonoScripts
</div>

### MonoScripts

<div style='display:none'>
It is important to understand that a MonoBehaviour has a reference to a MonoScript, and MonoScripts simply contain the information needed to locate a specific script class. Neither type of Object contains the executable code of script class.
</div>

理解 MonoBehaviour 拥有一个 MonoScript 的引用和 MonoScript 仅包含简单的用来定位特定脚本的信息是比较重要的。MonoScript  并不包括脚本的执行代码。

<div style='display:none'>
A MonoScript contains three strings: an assembly name, a class name, and a namespace.
</div>

MonoScript 包含 3 个字符串：程序集的名字， 一个类名和一个命名空间。

<div style='display:none'>
While building a project, Unity collects all the loose script files in the Assets folder and compiles them into Mono assemblies. Specifically, Unity builds an assembly for each distinct language used in the Assets folder, as well as separate assemblies for the scripts contained in the Assets/Plugins folder. C# scripts outside of the Plugins subfolder are placed into Assembly-CSharp.dll. Scripts within the Plugins subfolder are placed into Assembly-CSharp-firstpass.dll, and so on.
</div>

当构建项目的时候，Unity 收集所有 Assets 文件下零散放置的脚本，然后将他们编译成 Mono 程序集。Unity 会为 Assets 文件夹下的不同语言和 Assets/Plugins 文件夹下的脚本构建单独的程序集。在 Plugins 子文件夹外的 C# 脚本会编译到 Assembly-CSharp.dll 中，而 Plugins 子文件夹内的脚本会编译到 Assembly-CSharp-firstpass.dll 中。

<div style='display:none'>
These assemblies (plus prebuilt assembly DLLs) are included in the final build of a Unity application. They are also the assemblies to which a MonoScript refers. Unlike other resources, all assemblies included in a Unity application are loaded when the application first starts.
</div>

这些程序集（包括预先编译好的程序集的 DLL）会被包含到 Unity 应用的最终构建里面。他么也是 MonoScript 引用的程序集。与其他资源不同，所有 Unity 程序内的程序集会在程序第一次启动时加载。

<div style='display:none'>
This MonoScript Object is the reason why an AssetBundle (or a Scene or a prefab) does not actually contain executable code in any of the MonoBehaviour Components in the AssetBundle, Scene or prefab. This allows different MonoBehaviours to refer to specific shared classes, even if the MonoBehaviours are in different AssetBundles.
</div>

因为有 MonoScript 对象，AssetBundle（或者是场景文件，或者是预设）中 MonoBehaviour 组件可以不包含实际运行代码。这使得不同的 MonoBehaviour 可以指向特定的共享的类，即使这些不同的 MonoBehaviour 在不同的 AssetBundle 中。

<div style='display:none'>
### 1.7. Resource lifecycle
</div>

### Resouce 的生命周期

<div style='display:none'>
UnityEngine.Objects are loaded into/unloaded from memory at specific and defined times. To reduce loading times and manage an application's memory footprint, it's important to understand the resource lifecycle of UnityEngine.Objects.
</div>

UnityEingine.Objects 会在具体或者特定的时间从内存中加载/卸载。为了减少加载时间和管理应用的内存，理解 UnityEngine.Objects 的生命周期是比较重要的。

<div style='display:none'>
There are two ways to load UnityEngine.Objects: automatically or explicitly. An Object is loaded automatically whenever the Instance ID mapped to that Object is dereferenced, the Object is currently not loaded into memory, and the Object's source data can be located. Objects can also be explicitly loaded in scripts, either by creating them or by calling a resource-loading API (e.g. [AssetBundle.LoadAsset](http://docs.unity3d.com/ScriptReference/AssetBundle.LoadAsset.html)).
</div>

有两种方式可以加载 UnityEngine.Objects: 自动的和显式的。当一个实例 ID 映射到一个源数据存在，但是没有加载进内存并被间接引用的对象时，对象会被自动创建。对象可以在脚本中显式的加载。显式加载方式要可以是直接创建他们，也可以是通过资源加载的 API, 例如 [AssetBundle.LoadAsset](http://docs.unity3d.com/ScriptReference/AssetBundle.LoadAsset.html)。

<div style='display:none'>
When an Object is loaded, Unity tries to resolve any references by translating each reference's File GUID and Local ID into an Instance ID.
</div>

当一个对象被加载，Unity 会尝试将所有引用从文件 GUID 和本地 ID 转换成实例 ID。

<div style='display:none'>
An Object will be loaded on-demand the first time its Instance ID is dereferenced if two criteria are true:
</div>

当满足下面两个条件时，一个对象在它的实例 ID 被第一次引用时按需加载：

<div style='display:none'>
1. The Instance ID references an Object that is not currently loaded
2. The Instance ID has a valid File GUID and Local ID registered in the cache
</div>

1. 实例 ID 引用了没有加载的对象
2. 实例 ID 在缓存中有有效的、对应文件 GUID 和本地 ID

<div style='display:none'>
This generally occurs very shortly after the reference itself is loaded and resolved.
</div>

这通常发生在引用被加载和处理后的非常短的时间里。

<div style='display:none'>
If a File GUID and Local ID do not have an Instance ID, or if an Instance ID with an unloaded Object references an invalid File GUID and Local ID, then the reference is preserved but the actual Object will not be loaded. This appears as a "(Missing)" reference in the Unity Editor. In a running application, or in the Scene View, "(Missing)" Objects will be visible in different ways, depending on their types: meshes remain invisible, textures will appear magenta, etc.
</div>

如果一个文件 GUID 和本地 ID 不包含实例 ID, 或者一个实例 ID 关联一个引用无效的文件 GUID 和本地 ID 的未加载的对象，实例 ID 引用将会保留但是实际对象缺不能加载。这个在 Unity 编辑器里面显示为 `(Missing)`。在程序运行时或者场景视图里， 基于 `(Missing)` 对象的类型，会有下面几种显示：比如网格不可见，纹理显示成洋红色。

<div style='display:none'>
Objects are unloaded in three specific scenarios:
</div>

对象会在下面 3 种情况下被卸载：

<div style='display:none'>
1. Objects are automatically unloaded when unused Asset cleanup occurs. This process is triggered automatically when scenes are changed destructively (i.e. when invoking a non-additive Application.LoadLevel API), or when a script invokes the Resources.UnloadUnusedAssets API. This process only unloads unreferenced Objects: an Object will only be unloaded if no Mono variable holds a reference to the Object, and there are no other live Objects holding references to the Object.

2. Objects sourced from the Resources folder can be explicitly unloaded by invoking the Resources.UnloadAsset API. The Instance ID for these Objects remains valid and will still contain a valid File GUID and LocalID entry. If any Mono variable or other Object holds a reference to an Object that is unloaded with Resources.UnloadAsset, then that Object will be reloaded as soon as any of the live references are dereferenced.

3. Objects sourced from Asset Bundles are automatically and immediately unloaded when invoking the AssetBundle.Unload(true) API. This invalidates the Object's InstanceID's File GUID and Local ID reference, and any live references to the unloaded Objects will become "(Missing)" references. From C# scripts, attempting to access methods or properties on an unloaded object will produce a NullReferenceException.
</div>

1. 对象会在未使用的资产被清理时卸载。这个过程当场景破坏性的改变时（例如使用非增量的 Application.LoadLevel API）或者在代码里面调用 Resources.UnloadUnusedAssets API 时自动发生。这个过程只能卸载未被引用的对象：一个对象仅当没有 Mono 变量引用它，和没有其他对象保持其引用时才会卸载。
2. 从 Resources 文件夹内加载的对象可以用 Resources.UnloadAsset API 来卸载。它们的实例 ID 会保持有效，依然对应着有效的文件 GUID 和本地 ID。如果任何 Mono 变量或者对象保留着被 Resources.UnloadAsset 卸载的对象的引用，这些对象则会被重新加载。
3. 当我们调用 [AssetBundle.Unload(true)](http://docs.unity3d.com/ScriptReference/AssetBundle.Unload.html) API 时，从 AssetBundle 加载的对象会被立即自动的卸载。这会使对象的实例 ID 的文件 GUID 和本地 ID 引用无效，并且任何引用的已卸载的对象的引用将会变成 `(Missing)`。从 C# 脚本中尝试访问已卸载的对象的方法和属性会抛出 NullReferenceException 异常。

<div style='display:none'>
If [AssetBundle.Unload](http://docs.unity3d.com/ScriptReference/AssetBundle.Unload.html)(false) is called, live Objects sourced from the unloaded AssetBundle will not be destroyed, but Unity will invalidate the File GUID and Local ID references of their Instance IDs. It will be impossible for Unity to reload these Objects if they are later unloaded from memory and live references to the unloaded Objects remain. (4)
</div>

如果调用 [AssetBundle.Unload(false)](http://docs.unity3d.com/ScriptReference/AssetBundle.Unload.html)，从已卸载的 AssetBundle 中得到的活动的对象将不会被销毁，但是 Unity 会使这些对象的实例 ID 对其文件 GUID 和本地 ID 引用无效。如果这些对象从内存中卸载并且对这些已卸载的对象的引用依然保持着，Unity 将无法重新加载对象。 

<div style='display:none'>
### 1.8. Loading large hierarchies
</div>

### 加载大层次结构

<div style='display:none'>
When serializing hierarchies of Unity GameObjects (such as when serializing prefabs), it is important to remember that the entire hierarchy will be fully serialized. That is, every GameObject and Component in the hierarchy will be individually represented in the serialized data. This has interesting impacts on the time required to load and instantiate hierarchies of GameObjects.
</div>

当序列化有大层次结构的 Unity 游戏对象（比如序列化预设）时，重要的是要记住整个层次结构都会被序列化。也就是说层次结构中的每个游戏对象和组件都会被单独的序列化到序列化后的数据里面。这对加载和实例化对象层次需索的时间有影响。

<div style='display:none'>
When creating any GameObject hierarchy, CPU time is spent in several different ways:

* Time to read the source data (from storage, from another GameObject, etc.)
* Time to set up the parent-child relationships between the new Transforms
* Time to instantiate the new GameObjects and Components
* Time to awaken the new GameObjects and Components
</div>

当创建游戏对象层次结构时，CPU 时间会花费在下面几种方面上

*  从存储，别的游戏对象等读取源数据的时间
*  构建新 Transform 间父-子关系的时间
*  实例化新游戏对象和组件的时间
*  激活新游戏对象和组件的时间

<div style='display:none'>
The latter three time costs are generally invariant regardless of whether the hierarchy is being cloned from an existing hierarchy or is being loaded from storage (such as an AssetBundle). However, the time to read the source data increases linearly with the number of Components and GameObjects serialized into the hierarchy, and is also multiplied by the speed of the data source.
</div>

后面三种时间花费一般是不变的，无论是从现成的层次结构中拷贝或者从存储中加载（比如 AssetBundle)。但是读取源数据的时间与层次结构中的组件和游戏对象成线性增加的关系，当然还要乘以读取源数据的速度。

<div style='display:none'>
On all current platforms, it is considerably faster to read data from elsewhere in memory rather than loading it from a storage device. Further, the performance characteristics of the available storage media vary widely between different platforms -- desktop PCs load data from disk much faster than a mobile device.
</div>

在当前支持的所有平台中，从内存中读取数据会比从设备存储中读取明显快不少。而且不同平台上的存储媒介在性能上有很大差别--比如从 PC 上加载数据的数据会比移动设备快很多。

<div style='display:none'>
Therefore, when loading prefabs on platforms with slow storage, the time spent reading the prefab's serialized data from storage can rapidly exceed the time spent instantiating the prefab. That is, the cost of the loading operation is dominated by storage I/O time.
</div>

所以在低速存储设备的平台上加载预设，读取从存储上读取预设的实际会快速的超过实例化预设所花费的实际。也就是说，设备 I/O 的时间主导了加载操作所消耗的时间。

<div style='display:none'>
As mentioned before, when serializing a monolithic prefab, each and every GameObject and component's data is serialized separately - even if that data is duplicated. A UI screen with 30 identical elements will serialize the identical element 30 times. This produces a very large blob of binary data. At load time, the data for all of the GameObjects and Components on each one of those thirty duplicate elements must be read from disk before being transferred to the newly-instantiated Object. It is this file reading time that dominates the cost of instantiating large prefabs.
</div>

前面提到过，序列化大预设的时候，每个游戏对象和组件的数据都会单独的被序列化，即使这些数据是重复的。一个拥有 30 个一样的元素的 UI，这 30 一样的元素都会被序列化。这将会产生大量的数据。当在加载时期，这些重复数据元素必须从磁盘中读取，然后传递给新实例化的对象。文件读取时间主导了大预设实例化花费的时间。

<div style='display:none'>
Until such time as Unity supports nested prefabs, projects which instantiate extremely large hierarchies of GameObjects may be able to significantly reduce the loading times of their large prefabs by moving reused elements to separate prefabs and instantiating them at runtime, instead of relying entirely on Unity's serialization and prefab system.
</div>

直到 Unity 支持可嵌套预设之前，对于加载大层次游戏对象预设的项目，可以通过将冗余的元素拆分出来，然后在运行时加载它们的，而不依赖于 Unity 的序列化和预设系统来加载整个大对象的方式来大幅减少加载时间

<div style='display:none'>
Further, once a prefab or GameObject hierarchy has been constructed, it is faster to clone the existing hierarchy than to load a new copy from storage.
</div>

一旦预设或者对象已经构建了，从拷贝已存在的对象会比从存储中加载快一个新拷贝快很多。

<div style='display:none'>
Unity 5.4 note: Unity 5.4 altered the representation of transforms in memory. Each root transform's entire child hierarchy is stored in compact, contiguous regions of memory. When instantiating new GameObjects that will be instantly reparented into another hierarchy, consider using the new GameObject.Instantiate overloads which accept a parent argument.
</div>

__Unity 5.4:__ Unity 5.4 修改了内存中 tranform 的呈现方式。每个根 tranform 的所有子物体都存在内存中一段紧凑的，连续的区域中。实例化会重指定父级的新游戏对象时，考虑用 __GameObject.Instantiate__ 的接受父物体为参数的新重载。

<div style='display:none'>
Using this overload avoids the allocation of a root transform hierarchy for the new GameObject. In tests, this speeds up the time required for an instantiate operation by about 5-10%.
</div>

使用这个重载可以避免给新物体新分配根 tranform 层次。测试结果中，这个可以提高 5 - 10 % 的实例化时间。

<div style='display:none'>
### Footnotes
</div>

### 脚记

<div style='display:none'>
[1] A Local ID is unique within its own file. That is, it will be different from all the other Local ID for the same Asset file. ↩
</div>

* <div id='f1'>[1] 本地 ID 在包含它文件中是唯一的。也就是说在同一个资产文件中一个本地 ID 会区别于其他本地 ID。</div> 

<div style='display:none'>
[2] Internally, this cache is called the PersistentManager. The actual translation takes place within Unity's C++ Remapper class. The Remapper class is not exposed via any C# APIs. ↩
</div>

* <div id='f2'>[2] 在 Unity 内部，这个缓存叫做 __PresistenManager__。这个转换过程在 Unity 的 C++ Remapper 类中发生。Remapper 类当前不能被任何 C# API 访问。</div>

<div style='display:none'>
An example of an Asset created at runtime would be a Texture2D Object created in script, like so:

>   var myTexture = new Texture2D(1024, 768); 

</div>

* <div id='f3'>[3] 一个在运行时创建资产的例子就是在脚本中创建 Texture2D 对象，例如 </div> 

{% codeblock lang:python %}
var myTexture = new Texture2D(1024, 768); 
{% endcodeblock %}

<div style='display:none'>
[4] The most common case where Objects are removed from memory at runtime without being unloaded occurs when Unity loses control of its graphics context. For example, this can occur when a mobile app is suspended and the app is forced into the background. In this case, the mobile OS usually evicts all graphical resources from GPU memory. When the app returns to the foreground, Unity must re-upload all needed Textures, Shaders and Meshes to the GPU before it can resume rendering the scene. ↩
</div>

* <div id='f4'>[4] 最常见的是，当 Unity 丢失了对已在运行时从内存中移除的对象的 图形上下文的控制的时候，对象不会被 Unity 卸载。例如，这会发生在一个移动端应用被强制切到后台并挂起的时候，移动端系统通常会将从 GPU 显存中删除所有图形资源。当应用切回到前台，Unity 在恢复渲染当前场景之前， 必须重新上次所有需要的纹理，着色器和网格到 GPU 中。</div>

原文地址：<https://unity3d.com/learn/tutorials/topics/best-practices/assets-objects-and-serialization>