title: 10 个鲜为人知的 Unity 技巧 - 代码篇
date: 2016-09-01 08:12
category: UnityKB
tags: Unity Tips
---

#### 1. DidReloadScripts 属性 (Attribute)

这个 Attribute 可以让打上这个 Attribute 的静态方法在每次 Unity 重载代码之后执行。

    public class DidReloadScriptsTest : MonoBehaviour
    {
        [DidReloadScripts]
        private static void OnScriptsReloaded()
        {
            Debug.Log("Loaded");
        }
    }

#### 2. 利用 HelpUrl 属性 (Attribute) 给组件加上帮助链接


    [HelpURL("http://example.com/docs/MyComponent.html")]
    public class MyComponent
    {
    
    }


<!--more-->

#### 3. 