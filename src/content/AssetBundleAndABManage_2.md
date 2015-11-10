Title: Unity 5: Asset Bundle 和 Asset Bundle Manager
Date: 2015
Modified: 
Category: Unity
Tags: Unity
Status: skip
Keywords: Unity, Asset Bundle, Asset Bundle Manager

这篇是 Unity 官方教程 [AssetBundles and the AssetBundle Manager](http://unity3d.com/cn/learn/tutorials/topics/scripting/assetbundles-and-assetbundle-manager?playlist=17117) 的翻译， 分两部分，这是第一部分。翻译不到之处请不吝指出。非常谢谢！

##WORKING WITH ASSETBUNDLES AND THE ASSETBUNDLE MANAGER
###INTRODUCTION

One of the key areas of effort in working with AssetBundles is the building and testing of bundles. Often, during development, the Assets themselves are changing regularly. Normally this would require regularly building AssetBundles, uploading them to a host and testing these remotely hosted AssetBundles through a network connection with the working project.

This section focuses on using the AssetBundle Manager when working with AssetBundles. The AssetBundle Manager provides a High-level API for a massively improved workflow compared to manipulating AssetBundles directly with the foundation Low-level API.

###WORKING WITH ASSETBUNDLES

The steps of working with AssetBundles in the editor fall roughly into these steps: - Organizing & Setting-up AssetBundles in the editor. - Building AssetBundles. - Uploading AssetBundles to external storage. - Downloading AssetBundles at run-time. - Loading objects from AssetBundles.

It is worth noting that some AssetBundles can be stored locally for immediate loading as a default setup. This is useful to protect against an install where the application cannot reach remote external storage to download desired AssetBundles. For example, the application would load default language and localization data from a local AssetBundle when the application has no access to downloadable content.

It is also worth noting that an AssetBundle contains platform ready Assets. The contents of an AssetBundle have been compiled and optimized for the current target platform according to the Import Settings and the Target Platform set in the Build Settings. Because of this, AssetBundles should be built for each target platform.

In the following simple scene, one legitimate way of organizing the scene into AssetBundles for the greatest versatility would be to have a base scene, which would include the ground, dunes, rock columns, tree and cactus. This scene could be allowed to include the dependent Materials, as these are fairly simple and would not likely need to be changed depending upon resolution or device. The tank model would be in an AssetBundle of it’s own, which would allow changes or updates to the player Asset. Two additional AssetBundles would be used to complete the tank GameObject. These would be the dependent Materials in one, and the dependent Texture in another. This would allow for changes and updates to the texture and material as needed with the least amount of trouble. This particular organization will also allow for alternative versions, or variants, of these Assets to be loaded from a choice of AssetBundle Variants on demand depending upon need, such as platform, location or resolution of the target device.

descriptionA Simplified Example Scene

To organize and setup AssetBundles in the editor, the Assets themselves need to be assigned to an AssetBundle. When viewing an Asset, the AssetBundle Name and AssetBundle Variant can be found at the bottom of the preview window in the Inspector. The preview window must be open to see them.

descriptionAn Asset that has not been assigned to an AssetBundle.

To assign an Asset to an AssetBundle, use the AssetBundle Name drop down menu. Here, either create a new AssetBundle name or choose an existing one. AssetBundle Variants and the AssetBundle Variant Name menu will be covered later in this lesson.

descriptionAssigning an Asset to an AssetBundle

To create a new AssetBundle, choose New and a text field will become active to name a new AssetBundle.

To remove an Asset from an AssetBundle, choose None and the Asset will now be unassigned.

To remove an AssetBundle Name from the list, all Assets assigned to that AssetBundle Name must be removed from that AssetBundle name, and then “Remove Unused Names” can be selected. This will remove all unused AssetBundle Names.

descriptionCreating a new AssetBundle Name (Note Illegal Capital “T” in the AssetBundle Name)

Assets will be assigned to the AssetBundle selected in the AssetBundle Name menu. AssetBundle names are strictly lower case. If an uppercase letter is used, as in the example above, Unity will replace the capital letter with a lowercase one.

descriptionThe Tank Asset is now assigned to the AssetBundle “tank”.

Note how the AssetBundle Name has been corrected to lowercase letters automatically.

###USING ASSETBUNDLE VARIANTS

Being able to load Assets on demand from AssetBundles allows for many creative solutions to difficult issues related to loading, storing and updating Assets. One specific case where AssetBundles can help is the need to load a different set of Assets into a project depending upon the device, location or user preference. This is done by using AssetBundle Variants.

AssetBundle Variants deliver different versions of the same Asset to be assigned to an object in the scene. AssetBundle Variants completely remap different Assets to the same object. Only one Variant of an AssetBundle is ever loaded at any given time. Asset Variants can be created for many different situations. Asset Variants can be different resolutions of the same Asset: Standard Definition graphics vs High Definition graphics or models with different polycounts. Asset Variants can be created with different content for an object: text, images, textures and typefaces can be different for each supported language, region or theme. These Assets are saved in a series of identically constructed AssetBundles and identified by their Variant Name.

For this to work, all of the matching AssetBundle Variants must be constructed and named identically. The only difference between AssetBundle Variants are the individual Assets contained in the AssetBundle and the AssetBundle Variant Name which is appended to the AssetBundle Name to identify it. To be a compatible AssetBundle Variant, the folder structure and contents of the AssetBundle must match. All the Assets need to be present in each AssetBundle, and must have the same name and in the same hierarchical order.

The following example can be found in the AssetBundle Sample.

descriptionExample of AssetBundle Variants.

In the above example, both folders - MyAssets-HD and MyAssets-SD - have been assigned to the AssetBundle Name “myassets”. Each then has been given an AssetBundle Variant Name to identify it, in these cases hd and sd, respectively. Note how the two sets of Assets have the same name and share the same hierarchical structure. As the parent directory has been assigned to an AssetBundle and none of the children have been assigned to an AssetBundle, all of the children will be added to the parent’s AssetBundle when it is built.

descriptionMyAssets-HD with AssetBundle Name and AssetBundle Variant Name set.

descriptionMyAssets-SD with AssetBundle Name and AssetBundle Variant Name set.

It is worth noting that a hierarchical menu structure can be created for the AssetBundle Names. Note in the above images the AssetBundle Name has a path: variant/myassets. This will create a new menu item as a parent, called “variants” for the AssetBundle Name “myassets”.

descriptionAssetBundle Name with hierarchical menus.

Once Assets have been assigned to AssetBundles, the AssetBundles will need to be built and tested.

###USING THE ASSETBUNDLE MANAGER

Unity has a Low-level API to work with AssetBundles directly. This tutorial will not cover the Low-level API. For more information on the Low-level AssetBundle API, please see the information linked below.

For building, testing and managing AssetBundles, this tutorial will concentrate on the AssetBundle Manger and its High-level API.

The AssetBundle Manager is a downloadable package that can be installed in any current Unity project and will provide a High-level API and improved workflow for managing AssetBundles. The AssetBundle Manager can be downloaded here. To use the AssetBundle Manager in a project, simply add the AssetBundle Manager folder to the project’s Assets folder.

Building and testing AssetBundles can be a pain-point during development. Assets are often changing on a regular basis. With the Low-level AssetBundle API, testing would require regular building and uploading of the AssetBundles to a remote host and testing these remotely hosted AssetBundles through a network connection with the working project. The AssetBundle Manager allows for a massively improved workflow compared to manipulating AssetBundles directly with the Low-level API. The AssetBundle Manager helps manage the key steps in building and testing AssetBundles. The key features provided by the AssetBundle Manager are a Simulation Mode, a Local AssetBundle Server and a quick menu item to Build AssetBundles to work seamlessly with the Local AssetBundle Server.

Adding the AssetBundle Manager to a project will create a new item in the Assets Menu called “AssetBundles”.

descriptionAssets > AssetBundles

Selecting the AssetBundles menu item will show a small selection of menu items.

descriptionAssets > AssetBundles menu items

Simulation Mode, when enabled, allows the editor to simulate AssetBundles without having to actually build them. To enable Simulation Mode, select the menu item “Simulation Mode”. A checkmark will appear indicating that Simulation Mode is enabled. To disable Simulation Mode, select the menu item again. Simulation Mode will be disabled and the check-mark will be removed.

With Simulation Mode enabled, the editor looks to see which Assets are assigned to AssetBundles and uses these Assets directly from the Project’s hierarchy as if they were in an AssetBundle. These AssetBundles, however, do not need to be built. From this point on, work within the editor can continue as if AssetBundles were built and hosted remotely.

The huge advantage to the workflow when simulation mode is enabled is that Assets can be changed, manipulated, imported, removed and as long as they are correctly assigned to an AssetBundle, work on the project does not need to stop to build and deploy AssetBundles before testing. Testing with the Simulation Mode enabled is immediate.

It is worth noting that AssetBundle Variants do not work under Simulation Mode. To test AssetBundle Variants, the AssetBundles will need to be built and deployed. AssetBundle Variants do work with the Local Asset Server, however.

The ABM can also enable a Local Asset Server for testing from either the editor or from local builds - including Mobile. When Local Asset Server is enabled, AssetBundles must be built and placed in a folder explicitly called “AssetBundles” in the root of the Project, which is on the same level as the “Assets” folder.

descriptionThe location of the AssetBundles folder required by the Local Asset Server

With the AssetBundles hosted locally, it is easy to access the Local Asset Server from the working project with a few simple lines of code. Please see the example in the AssetBundle Sample project, which will be covered later in this lesson.

Building AssetBundles and saving them into the “AssetBundles” folder on the root of the Project can be done simply by selecting “Build AssetBundles” from the “Assets/AssetBundles” menu. When “Build AssetBundles” is selected, Unity will build all of the AssetBundles that have had Assets assigned to them, compiling and optimizing them for the current build target, and finally saving them and a master Manifest to the “AssetBundles” folder in the root of the project. If there is no “AssetBundles” folder, Unity will make one. Inside the “AssetBundles” folder, the AssetBundles are organized by build target.

descriptionContents of the “AssetBundles” folder, grouped by build target.

With AssetBundles built and either deployed, or by enabling the Local AssetBundle Server, these AssetBundles can be downloaded and incorporated into a Project at run-time.

###USING ASSETBUNDLES IN PRACTICE

To use AssetBundles in practice, this lesson will be using the AssetBundle Manager. The AssetBundle Manager will take care of loading AssetBundles and their associated Asset Dependencies. To load Assets from AssetBundles using the AssetBundle Manager, a script needs to be written using the API provided by the AssetBundle Manager.

The AssetBundle Manager’s API includes:

Initialize() Initializes the AssetBundle manifest object.
LoadAssetAsync() Loads a given asset from a given AssetBundle and handles all the dependencies.
LoadLevelAsync() Loads a given scene from a given AssetBundle and handles all the dependencies.
LoadDependencies() Loads all the dependent AssetBundles for a given AssetBundle.
BaseDownloadingURL Sets the base downloading url which is used for automatic downloading dependencies.
SimulateAssetBundleInEditor Sets Simulation Mode in the Editor.
Variants Sets the active variant.
RemapVariantName() Resolves the correct AssetBundle according to the active variant.
Sample files are included with the AssetBundle Manager in a folder called "AssetBundle Sample". There are three basic sample scenes and one more advanced sample scene in the "AssetBundleSample/Scenes" folder:

"AssetLoader" demonstrates how to load a normal Asset from AssetBundles.
"SceneLoader" demonstrates how to load a Scene from AssetBundles.
"VariantLoader" demonstrates how to load AssetBundle Variants.
“LoadTanks” is more advanced and will demonstrate a more complex example with loading a Scene, Assets and AssetBundle Variants into the same scene.
Each one of these scenes is driven by a very basic script: LoadAssets.cs, LoadScenes.cs, LoadVariants.cs and LoadTanks.cs respectively.

At this point it is important to reiterate the workflow provided by the AssetBundle Manager.

To successfully test the use of AssetBundles, there are three possible scenarios.

In the first scenario, without using the AssetBundle Manager, AssetBundles will need to be built and deployed and all testing is done with the complete and final system in place. In this scenario, with every change to the Assets in a Project, new AssetBundles need to be built and deployed.

There are two improvements to the workflow provided by the AssetBundle Manager. These are the Local AssetBundle Server and Simulation Mode.

In Simulation Mode, the AssetBundle Manager simulates built AssetBundles when running the Project within the editor. This is the fastest workflow to use. Simply enable “Simulation Mode” using the menu item “Assets/AssetBundles/Simulation Mode” and test the project. No AssetBundles will be built. It is important to note, however, that AssetBundle Variants do not work with Simulation Mode. It is also important to note that Assets can be manipulated in the project when Simulation Mode is enabled, and the effect of these changes can seen in the scene view, which will not be possible with deployed AssetBundles.

The Local AssetBundle Server provides a more accurate representation of deployed AssetBundles, but requires that the AssetBundles be built and stored in a default folder within the project. When the Local AssetBundle Server is enabled, the built AssetBundles will be available to the Editor and all builds running locally that can reach the Editor on the local network. It is worth noting that this is the only way to test AssetBundle Variants locally.

To run one of the sample scenes, the AssetBundle Manager must be running in one of these modes. To run the AssetBundle Variant scene successfully, AssetBundles must be built and the Local AssetBundle Server must be enabled.

###EXAMPLE 1: LOADING ASSETS

Enable Simulation Mode using the menu item “Assets/AssetBundles/Simulation Mode”.
Open the scene “AssetBundleSample/Scenes/AssetLoader”.
Note that the scene is essentially empty and only contains a Main Camera, Directional Light and “Loader” GameObject.
Enter Playmode.
Note that a cube has been loaded into the scene from an AssetBundle.
This scene is driven by the script “LoadAssets.cs”.

Open “AssetBundleSample/Scripts/LoadAssets.cs” in a script editor.

There are two public variables: public string assetBundleName; and public string assetName;

public string assetBundleName; holds the name of the AssetBundle to be loaded.
public string assetName; holds the name of the Asset to be loaded from the loaded AssetBundle.
The script comprises of a Start() function and two Coroutines, called from Start(). In Initialize(), DontDestroyOnLoad() is called, the path to the AssetBundles is set and the AssetBundle Manifest is initialized. In InstantiateGameObjectAsync() the Asset and AssetBundle name are requested using AssetBundleManager.LoadAssetAsync() and if the Asset requested is not null, it is instantiated.

What is important to note here, by looking at the Asset “MyCube” in “AssetBundleSample/Assets” is that “MyCube” is dependent upon “MyMaterial” which is then dependent on “UnityLogo”. Only the Asset “MyCube” was requested, and all of the dependent Assets were correctly loaded.

It is also worth noting how the path to the AssetBundles is being set. This code will set the location for the AssetBundles to the Local AssetBundle Server when the scene is running within the Editor or from a Development Build. (For more information on development builds, please see the documentation on publishing builds.) When working in the Editor while Simulation Mode is enabled, AssetBundles will be simulated and this setting will not be used.

To understand the use of DontDestroyOnLoad() it is worth understanding that even though this is a very simple script and in this context it is not absolutely necessary, it is present here with the assumption that this script will become the basis of an AssetBundle loader for a more complex project and will need to survive scene changes.

###EXAMPLE 2: LOADING SCENES

Make sure Simulation Mode is enabled by using the menu item “Assets/AssetBundles/Simulation Mode”.
Open the scene “AssetBundleSample/Scenes/SceneLoader”.
Note that the scene is essentially empty and only contains a Main Camera, Directional Light and “Loader” GameObject.
Enter Playmode.
Note that a cube and a plane have been loaded into the scene from an AssetBundle.
This scene is driven by the script “LoadScenes.cs”.

Open “AssetBundleSample/Scripts/LoadScenes.cs” in a script editor.

There are two public variables: public string sceneAssetBundle; and public string sceneName;

sceneAssetBundle; holds the name of the AssetBundle to be loaded.
sceneName; holds the name of the Scene to be loaded from the loaded AssetBundle.
The script comprises of a Start() function and two Coroutines, called from Start(). In Initialize(), DontDestroyOnLoad() is called, the path to the AssetBundles is set and the AssetBundle Manifest is initialized. In InitializeLevelAsync() the Scene name and isAdditive are used to request a Scene using AssetBundleManager.LoadLevelAsync(). If the Scene requested is null, the AssetBundle Manager will display an error in the console and the Coroutine ends.

What is important to note here, by looking at the Asset “MyCube” in “AssetBundleSample/Assets” is that “Cube” is dependent upon “MyMaterial” which is then dependent on “UnityLogo”. Only the Scene “TestScene” was requested. “Cube” was included in “TestScene” and all of the dependent Assets were correctly loaded by the AssetBundle Manager.

It is also worth noting how the path to the AssetBundles is being set. This code will set the location for the AssetBundles to the Local AssetBundle Server when the scene is running within the Editor or from a Development Build. (For more information on development builds, please see the documentation on publishing builds.) When working in the Editor while Simulation Mode is enabled, AssetBundles will be simulated and this setting will not be used.

To understand the use of DontDestroyOnLoad() it is worth understanding that even though this is a very simple script and in this context it is not absolutely necessary, it is present here with the assumption that this script will become the basis of an AssetBundle loader for a more complex project and will need to survive scene changes.

###EXAMPLE 3: VARIANTS

To work with AssetBundle Variants, the AssetBundles will need to be built, as AssetBundle Variants do not work with Simulation Mode. To build AssetBundles and their Variants, make sure all of the Assets are properly assigned to an AssetBundle Name and, if being used as an AssetBundle Variant, an appropriate AssetBundle Variant Name needs to be assigned as well.

descriptionAn Asset with both AssetBundle Name and AssetBundle Variant Name set.

When all Assets have been assigned to an AssetBundle or AssetBundle Variant, AssetBundles can be built by selecting “Assets/AssetBundles/Build AssetBundles”.

descriptionAssets/AssetBundles/Build AssetBundles

By default, the AssetBundles will be optimized for the current build target and built into a folder called “AssetBundles” in the Project’s root directory, grouped by build target.

For ease of workflow and to use these newly built AssetBundles without deploying them, the Local AssetBundle Server should be enabled. Use “Assets/AssetBundles/Local AssetBundle Server” to enable the Local AssetBundle Server.

descriptionStarting the Local AssetBundle Server

This local server should run seamlessly, but, as with any network communication, the local server will have the same restrictions as any network communication and may be subject to permissions requirements, firewalls, and other limitations. Be aware that the Local AssetBundle Server is enabling a Local AssetBundle Server that is set to the default IP Address and Port, which is usually http://192.168.1.115:7888/. This information is temporarily stored in the file AssetBundleManager/Resources/AssetBundleServerURL. This information will be set or changed automatically by the AssetBundleManager, and should not need any attention by the user.

descriptionAssetBundleServerURL contains the current URL and Port

When the the Local AssetBundle Server is running, the built AssetBundles can be tested locally.

Make sure Simulation Mode is disabled by using the menu item “Assets/AssetBundles/Simulation Mode”.
Make sure the Local AssetBundle Server is enabled by using the menu item “Assets/AssetBundles/Local AssetBundle Server”.
Open the scene “AssetBundleSample/Scenes/VariantLoader”.
Note that the scene is essentially empty and only contains a Main Camera, Directional Light and “Loader” GameObject.
Enter Playmode.
Choose “Load SD”.
Note that a cube and a Sprite have been loaded into the scene from an AssetBundle.
Exit Playmode.
Enter Playmode.
Choose “Load HD”.
Note that the same cube and Sprite have been loaded in the scene, but the Material, its dependent texture and the Sprite texture have been loaded from a different AssetBundle. The materials have different colors and the images are at a significantly higher resolution.
This scene is driven by the script “LoadVariants.cs”.

Open “AssetBundleSample/Scripts/LoadVariants.cs” in a script editor.

This script is nearly identical to “LoadScenes.cs”. The main differences are the variable identifying the AssetBundle Variant to be loaded, and code to set the active Variant. There is additional code to create the UI Buttons.

public string variantSceneAssetBundle; holds the name of the AssetBundle to be loaded.
public string variantSceneName; holds the name of the Scene to be loaded from the loaded AssetBundle.
private string[] activeVariants; holds the AssetBundleVariantNames to identify which AssetBundle Variants to load.
private bool bundlesLoaded; is used to hide the UI when the Assets have been loaded.
The script comprises of a BeginExample() function and two Coroutines, called from Start(). BeginExample is called by the “Load HD” or “Load SD” button in OnGUI. In Initialize(), DontDestroyOnLoad() is called, the path to the AssetBundles is set and the AssetBundle Manifest is initialized. In BeginExample(), between calling Initialize() and InitializeLevelAsync(), the active Variants are set. The value being set here is created by the “Load HD” or “Load SD” button in OnGUI. In InitializeLevelAsync() the Scene name and isAdditive are used to request a Scene using AssetBundleManager.LoadLevelAsync(). If the Scene requested is null, the AssetBundle Manager will display an error in the console and the Coroutine ends.

What is important to note here is how AssetBundle Variants are loaded. The array activeVariants contains a list of all of the possible Variant Names that are “active”. This array is used to set the AssetBundleManager.ActiveVariants property. When loading an AssetBundle that has a variant, the AssetBundle Manager will choose the AssetBundles that have “active” Variant Names in the ActiveVariants property. In the current example the ActiveVariants property contains only one element; the Active Variant is either “sd” or “hd”. It is possible to have multiple entries in the ActiveVariants property. For example there could be the following AssetBundles: my-material.sd, my-material.hd, my-text.english, my-text.danish, my-text.catalan, my-text.welsh. The ActiveVariants property could contain both “hd” and “danish”, or “sd” and “english” and so on for any of the other possible combinations of these Variant Names. This way, the AssetBundle Manager can load hd/sd images and the language choices separate from each other.

There are some rules to this that are worth noting. If, for some reason, there are AssetBundles that have Variants assigned, but no Active Variant Name is set in the ActiveVariants property- for example neither “sd” nor “hd” are in the ActiveVariants property for the current example - the AssetBundle Manager will simply use the first AssetBundle it finds with the correct AssetBundle Name, ignoring the Variant Name. If, for some reason, there are multiple Active Variant Names in the ActiveVariants property for the same set of AssetBundles - for example, both “sd” and “hd” are in the ActiveVariants property for the current example - the AssetBundle Manager will choose the AssetBundle Variant whose Variant Name comes first in the ActiveVariants property.

###EXAMPLE 4: TANKS EXAMPLE

This more complex example will sum up everything in this article, including loading a scene from an AssetBundle and loading AssetBundle Variants for resolution, content and localization.

Make sure Simulation Mode is disabled by using the menu item “Assets/AssetBundles/Simulation Mode”.
Make sure the Local AssetBundle Server is enabled by using the menu item “Assets/AssetBundles/Local AssetBundle Server”.
Open the scene “AssetBundleSample/Scenes/TanksLoader”.
Note that the scene is essentially empty and only contains only the “Loader” GameObject.
Enter Playmode.
Select one choice for resolution, style and language.
Note that the assets loaded are the options chosen in the UI.
Note that if none of the choices are explicitly chosen, the AssetBundleManager will choose one automatically (as per the rules above) and print a warning in the console.
This scene is driven by the script “LoadTanks.cs”.

Open “AssetBundleSample/Scripts/LoadTanks.cs” in a script editor.

This script is very similar to “LoadScenes.cs” and “LoadAssets.cs”. This script uses code to both load a scene which depends upon a variant and to load an additional GameObject that also depends upon a variant. There is additional code to create the UI Buttons.

public string sceneAssetBundle; holds the name of the Scene bearing AssetBundle to be loaded.
public string sceneName; holds the name of the Scene to be loaded from the loaded AssetBundle.
public string textAssetBundle; holds the name of the Text Asset bearing AssetBundle to be loaded.
public string textAssetName; holds the name of the Text Asset to be loaded from the loaded AssetBundle.
private string[] activeVariants; holds the ActiveVariants to pass to the AssetBundleManager.
private bool bundlesLoaded; is used to hide the UI when the Assets have been loaded.
private bool sd, hd, normal, desert, english, danish; holds values used to set the ActiveVariant.
private string tankAlbedoStyle, tankAlbedoResolution, language; holds values used to set the ActiveVariant.
The script comprises of a BeginExample() function and three Coroutines, called from Start(). The BeginExample() function is called by the button “Load Scene” in OnGUI(). In Initialize(), DontDestroyOnLoad() is called, the path to the AssetBundles is set and the AssetBundle Manifest is initialized. In BeginExample(), between calling Initialize() and InitializeLevelAsync(), the active Variants are set. The value being set here is created by the button “Load Scene” based on the user input in OnGUI(). In InitializeLevelAsync() the Scene name and isAdditive are used to request a Scene using AssetBundleManager.LoadLevelAsync(). If the Scene requested is null, the AssetBundle Manager will display an error in the console and the Coroutine ends. In InstantiateGameObjectAsync() the Asset and AssetBundle name are requested using AssetBundleManager.LoadAssetAsync() and if the Asset requested is not null, it is instantiated. If the AssetBundle cannot be loaded or the Asset cannot be requested, an error will be printed in the console.

What is important to note here is how several Asset, AssetBundles and AssetBundleVariants are being accessed and loaded in this scene, and how these values can be set at run-time.