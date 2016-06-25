title: 在不同平台运行不同代码的几种方式  
Date: 2016-06-25 16:50
category: UnityKB
tags: UnityKB
---

由于 Unity 支持多平台，所以写代码时，我们总会碰到一些需要在不同的平台实现不同的逻辑的情况。那在 Unity 中怎么实现呢？

总体来说有这么几种方法：

* 最常见的就是使用预编译宏
* 第二种方法是使用 C# 的 ConditionalAttribute 属性（Attribute)
* 第三种运行期读取 Application.platform 字段的值判断当前是哪个平台

### 预编译宏

下面是一段简单的示范：

{% codeblock %}

private void CompilationDirectivesWay()
{
#if UNITY_IOS
    Debug.Log("在 iOS 上运行，使用预编译宏方式");
#elif UNITY_ANDROID
    Debug.Log("在 Android 上运行，使用预编译宏方式");
#endif
}

{% endcodeblock %}

其中 `UNITY_IOS` 和 `UNITY_ANDROID` 是预编译宏。通过 `#if`， `#else`，`#elif` 等指令来做逻辑判断，记住末尾需要加上 `#endif` 来结束。

除了 `UNITY_IOS` 和 `UNITY_ANDROID` 之外还有其他一些常用的预编译宏，比如：

预编译宏 | 表示平台
--- | --- 
UNITY_EDITOR |  Unity 编辑器
UNITY_EDITOR_WIN | Windows 平台上的 Unity 编辑器
UNITY_EDITOR_OSX | Mac OSX 平台上的 Unity 编辑器
UNITY_STANDALONE_OSX | Mac OSX 应用
UNITY_STANDALONE_WIN | Windows 应用
UNITY_STANDALONE_LINUX | Linux 引用
UNITY_STANDALONE | 桌面应用
UNITY_WSA | Windows 商城应用
UNITY_WEBGL | WebGL

其他宏可以参照 [这个链接](http://docs.unity3d.com/Manual/PlatformDependentCompilation.html)。

### ConditionalAttribute

`ConditionalAttribute` 是 C# 的功能，使用前需要引入 `System.Diagnostics`。代码示范如下：

{% codeblock %}
private void ConditionalAttributeWay()
{
    RunOnIOS();
    RunOnAndroid();
}

[ConditionalAttribute("UNITY_IOS")]
private void RunOnIOS()
{
    Debug.Log("在 iOS 上运行, 使用 ConditionalAttribute 方式");
}

[ConditionalAttribute("UNITY_ANDROID")]
private void RunOnAndroid()
{
    Debug.Log("在 Android 上运行, 使用 ConditionalAttribute 方式");
}

{% endcodeblock %}

注意，跟预编译是编译期时起作用不一样，`ConditionalAttribute` 是运行期起作用，也就是说上面的 `RunOnIOS()` 和 `RunOnAndroid()` 都
会被编译进 DLL 里面。

### Application.platform

`Application.platform` 表示当前游戏运行的平台，需要在运行期做判断。废话不多说，Show you the code：

{% codeblock %}
private void OnRuntimeWay()
{
    switch (Application.platform)
    {
        case RuntimePlatform.IPhonePlayer:
            Debug.Log("在 iOS 上运行, 使用 Application.platform 方式");
            break;
        case RuntimePlatform.Android:
            Debug.Log("在 Android 上运行, 使用 Application.platform 方式");
            break;
        default:
            break;
    }
}
{% endcodeblock%}


### 代码

（好吧，我真不是为了占篇幅才贴下面代码的）

{% codeblock %}
using UnityEngine;
using System.Diagnostics;
using Debug = UnityEngine.Debug;

public class DifferentPlatform : MonoBehaviour
{
    void Start()
    {
        CompilationDirectivesWay();
        ConditionalAttributeWay();
		OnRuntimeWay();
    }

    private void CompilationDirectivesWay()
    {
#if UNITY_IOS
        Debug.Log("在 iOS 上运行，使用预编译宏方式");
#elif UNITY_ANDROID
		Debug.Log("在 Android 上运行，使用预编译宏方式");
#endif
    }

    private void ConditionalAttributeWay()
    {
        RunOnIOS();
        RunOnAndroid();
    }

    [ConditionalAttribute("UNITY_IOS")]
    private void RunOnIOS()
    {
        Debug.Log("在 iOS 上运行, 使用 ConditionalAttribute 方式");
    }

    [ConditionalAttribute("UNITY_ANDROID")]
    private void RunOnAndroid()
    {
        Debug.Log("在 Android 上运行, 使用 ConditionalAttribute 方式");
    }

    private void OnRuntimeWay()
    {
        switch (Application.platform)
        {
            case RuntimePlatform.IPhonePlayer:
				Debug.Log("在 iOS 上运行, 使用 Application.platform 方式");
                break;
			case RuntimePlatform.Android:
				Debug.Log("在 Android 上运行, 使用 Application.platform 方式");
				break;
            default:
                break;
        }
    }
}

{% endcodeblock %}

Enjoy!