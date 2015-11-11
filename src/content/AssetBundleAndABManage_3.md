Title: Unity 5: 使用 Asset Bundle 和 Asset Bundle Manager
Date: 2015
Modified: 
Category: Unity
Tags: Unity
Status: skip
Keywords: Unity, Asset Bundle, Asset Bundle Manager

这篇是 Unity 官方教程 [AssetBundles and the AssetBundle Manager](http://unity3d.com/cn/learn/tutorials/topics/scripting/assetbundles-and-assetbundle-manager?playlist=17117) 的翻译， 分三部分，这是第三部分。翻译不到之处请不吝指出。非常谢谢！
<hr>

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