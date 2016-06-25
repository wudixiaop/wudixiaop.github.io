title: 一起看看MonoBehavior内部事件执行顺序
date: 2014-11-10 21:38
category: UnityKB
tags: UnityKB
---

### 写在最前面
或许对于大部分Unity3D程序员来说，第一次接触脚本编写的时候都是从MonoBehavior开始的。MonoBehavior是Uniy3d脚本编写核心的类之一， 它预先定义好了很多事件，并且这些事件按照预先定义好顺序执行。了解MonoBehavior提供的这些事件的执行顺序，是我们进一步提高脚步编程和了解Unity3D内部逻辑的必要一步。我们先从MonoBehavior提供的事件说起。

### MonoBehavior都提供了什么事件
MonoBehavior提供的事件从编辑器到游戏结束都有涉及。下面列举一些常用的，更详列表可以参照 [这个页面](http://docs.unity3d.com/ScriptReference/MonoBehaviour.html)。

#### 与编辑相关

| 名称 | 注释 |
|:-----|:---|
|Reset| Reset to default values. |

<!--more-->

#### Update相关

| 名称 | 注释 |
|:----|:----|
|FixedUpdate|This function is called every fixed framerate frame, if the MonoBehaviour is enabled.|
|Update|Update is called every frame, if the MonoBehaviour is enabled.|
|LateUpdate|LateUpdate is called every frame, if the Behaviour is enabled.|

#### 生命周期相关
  
| 名称 | 注释 |
|:----|:----|
|Awake|Awake is called when the script instance is being loaded.|
|OnEnable|This function is called when the object becomes enabled and active.|
|OnDisable|This function is called when the behaviour becomes disabled () or inactive.|
|OnDestroy|This function is called when the MonoBehaviour will be destroyed.|
|OnApplicationFocus|Sent to all game objects when the player gets or loses focus.|
|OnApplicationPause|Sent to all game objects when the player pauses.|
|OnApplicationQuit|Sent to all game objects before the application is quit.|
|Start|Start is called on the frame when a script is enabled just before any of the Update methods is called the first time.|

#### 物理系统相关

| 名称 | 注释 |
|:----|:----|
|OnCollisionEnter|OnCollisionEnter is called when this collider/rigidbody has begun touching another rigidbody/collider.|
|OnCollisionStay|OnCollisionStay is called once per frame for every collider/rigidbody that is touching rigidbody/collider.|
|OnCollisionExit|OnCollisionExit is called when this collider/rigidbody has stopped touching another rigidbody/collider.|
|OnCollisionEnter2D|Sent when an incoming collider makes contact with this object's collider (2D physics only).
|OnCollisionStay2D|Sent each frame where a collider on another object is touching this object's collider (2D physics only).|
|OnCollisionExit2D|Sent when a collider on another object stops touching this object's collider (2D physics only).|
|OnTriggerEnter|OnTriggerEnter is called when the Collider other enters the trigger.|
|OnTriggerStay|OnTriggerStay is called once per frame for every Collider other that is touching the trigger.|
|OnTriggerExit|OnTriggerExit is called when the Collider other has stopped touching the trigger.|
|OnTriggerEnter2DSent when another object enters a trigger collider attached to this object (2D physics only).|
|OnTriggerStay2D|Sent each frame where another object is within a trigger collider attached to this object (2D physics only).|
|OnTriggerExit2D|Sent when another object leaves a trigger collider attached to this object (2D physics only).|

#### 输入系统相关

| 名称 | 注释 |
|:----|:----|
|OnMouseDown|OnMouseDown is called when the user has pressed the mouse button while over the GUIElement or Collider.|
|OnMouseOver|OnMouseOver is called every frame while the mouse is over the GUIElement or Collider.|
|OnMouseUp|OnMouseUp is called when the user has released the mouse button.|
|OnMouseDrag|OnMouseDrag is called when the user has clicked on a GUIElement or Collider and is still holding down the mouse.|
|OnMouseEnter|OnMouseEnter is called when the mouse entered the GUIElement or Collider.|
|OnMouseExit|OnMouseExit is called when the mouse is not any longer over the GUIElement or Collider.|
|OnMouseUpAsButton|OnMouseUpAsButton is only called when the mouse is released over the same GUIElement or Collider as it was pressed.|

#### 渲染相关

| 名称 | 注释 |
|:----|:-----|
|OnPreCull|OnPreCull is called before a camera culls the scene.|
|OnBecameVisible|OnBecameVisible is called when the renderer became visible by any camera.|
|OnBecameInvisible|OnBecameInvisible is called when the renderer is no longer visible by any camera.|
|OnWillRenderObject|OnWillRenderObject is called once for each camera if the object is visible.|
|OnPreRender|OnPreRender is called before a camera starts rendering the scene.|
|OnRenderObject|OnRenderObject is called after camera has rendered the scene.|
|OnPostRender|OnPostRender is called after a camera finished rendering the scene.|
|OnRenderImage|OnRenderImage is called after all rendering is complete to render image.|
|OnGUI|OnGUI is called for rendering and handling GUI events.|
|OnDrawGizmos|Implement OnDrawGizmos if you want to draw gizmos that are also pickable and always drawn.|

### 用图来表示MonoBehavior事件执行顺序

![monobehavior](/images/monobehaviour_flowchart.svg)

### 总结:
* 首次加载场景时执行**Awake()**
* **Start()**只在第一帧才执行, **Start()**在**Awake()**之后执行
* Update的执行顺序是: **FixedUpdate()** -> **Update()** -> **LateUpdate()**
* 以每一帧的**Update()**事件作分界线：  
    * **Update()之前**：**物理系统**和**输入系统**相关事件先执行，如**OnTriggerXXX**和**OnMouseXXX**事件。此处**XXX**是占位符，如**OnTriggerXXX**可以代表**OnTriggerEnter**或者**OnTriggerExit**
    * **Update()之后**：**场景渲染**和**协程**，如**OnRenderImage()**和**yield WWW**语句
* 协程中，除了**WaitForFixedUpdate**是在**FixedUpdate**之后，**Update**之前执行，其他的都是在**Update**之后，**场景渲染**前执行
* GUI事件**OnGUI**在场景渲染完之后执行
* 当对象被销毁时执行**OnDestory()**事件
* 当游戏退出时执行**OnApplicationQuit()**
* **OnEnable()**和**OnDisable()**  
    * **OnEnable()**只有在Object是Active的状态下才能用，一般是Object被初始化或者Object从disable到active过程中被调用
    * **OnDisable()**只有到Object从active到disable状态才被调用
