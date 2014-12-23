Title: 一起看看MonoBehavior内部事件执行顺序
Date: 2014-11-10 21:38
Modified: 2014-12-23 18:20
Category: 一点一滴
Tags: Unity3D

###**写在最前面**
或许对于大部分Unity3D程序员来说，第一次接触脚本编写的时候都是从MonoBehavior开始的。MonoBehavior是Uniy3d脚本编写核心的类之一， 它预先定义好了很多事件，并且这些事件按照预先定义好顺序执行。了解MonoBehavior提供的这些事件的执行顺序，是我们进一步提高脚步编程和了解Unity3D内部逻辑的必要一步。我们先从MonoBehavior提供的事件说起。

###**MonoBehavior都提供了什么事件**
MonoBehavior提供的事件从编辑器到游戏结束都有涉及。下面列举一些常用的，更详列表可以参照[这个页面](http://docs.unity3d.com/ScriptReference/MonoBehaviour.html)。

**与编辑相关**  
<table class="table table-striped table-hover">
    <theader>
        <th>名称</th>
        <th>注释</th>
    </theader>
    <tbody>
        <tr>
            <td>Reset</td>
            <td>Reset to default values.</td>
        </tr>
    </tbody>
</table>

**Update相关**
<table class="table table-striped table-hover">
    <theader>
        <th>名称</th>
        <th>注释</th>
    </theader>
    <tbody>
        <tr>
            <td>FixedUpdate</td>
            <td>This function is called every fixed framerate frame, if the MonoBehaviour is enabled.</td>
        </tr>
        <tr>
            <td>Update</td>
            <td>Update is called every frame, if the MonoBehaviour is enabled.</td>
        </tr>
        <tr>
            <td>LateUpdate</td>
            <td>LateUpdate is called every frame, if the Behaviour is enabled.</td>
        </tr>
    </tbody>
</table>


**生命周期相关**  
<table class="table table-striped  table-hover">
    <theader>
        <th>名称</th>
        <th>注释</th>
    </theader>
    <tbody>
        <tr>
            <td>Awake</td>
            <td>Awake is called when the script instance is being loaded.</td>
        </tr>
        <tr>
            <td>OnEnable</td>
            <td>This function is called when the object becomes enabled and active.</td>
        </tr>
        <tr>
            <td>OnDisable</td>
            <td>This function is called when the behaviour becomes disabled () or inactive.</td>
        </tr>
        <tr>
            <td>OnDestroy</td>
            <td>This function is called when the MonoBehaviour will be destroyed.</td>
        </tr>
        <tr>
            <td>OnApplicationFocus</td>
            <td>Sent to all game objects when the player gets or loses focus.</td>
        </tr>
        <tr>
            <td>OnApplicationPause</td>
            <td>Sent to all game objects when the player pauses.</td>
        </tr>
        <tr>
            <td>OnApplicationQuit</td>
            <td>Sent to all game objects before the application is quit.</td>
        </tr>
        <tr>
            <td>Start</td>
            <td>Start is called on the frame when a script is enabled just before any of the Update methods is called the first time.</td>
        </tr>
    </tbody>
</table>

**物理系统相关**
<table class="table table-striped  table-hover">
    <theader>
        <th>名称</th>
        <th>注释</th>
    </theader>
    <tbody>
        <tr>
            <td>OnCollisionEnter</td>
            <td>OnCollisionEnter is called when this collider/rigidbody has begun touching another rigidbody/collider.</td>
        </tr>
        <tr>
            <td>OnCollisionStay</td>
            <td>OnCollisionStay is called once per frame for every collider/rigidbody that is touching rigidbody/collider.</td>
        </tr>
        <tr>
            <td>OnCollisionExit</td>
            <td>OnCollisionExit is called when this collider/rigidbody has stopped touching another rigidbody/collider.</td>
        </tr>
        <tr>
            <td>OnCollisionEnter2D</td>
            <td>Sent when an incoming collider makes contact with this object's collider (2D physics only).</td>
        </tr>
        <tr>
            <td>OnCollisionStay2D</td>
            <td>Sent each frame where a collider on another object is touching this object's collider (2D physics only).</td>
        </tr>
        <tr>
            <td>OnCollisionExit2D</td>
            <td>Sent when a collider on another object stops touching this object's collider (2D physics only).</td>
        </tr>
        <tr>
            <td>OnTriggerEnter</td>
            <td>OnTriggerEnter is called when the Collider other enters the trigger.</td>
        </tr>
        <tr>
            <td>OnTriggerStay</td>
            <td>OnTriggerStay is called once per frame for every Collider other that is touching the trigger.</td>
        </tr>
        <tr>
            <td>OnTriggerExit</td>
            <td>OnTriggerExit is called when the Collider other has stopped touching the trigger.</td>
        </tr>
        <tr>
            <td>OnTriggerEnter2D</td>
            <td>Sent when another object enters a trigger collider attached to this object (2D physics only).</td>
        </tr>
        <tr>
            <td>OnTriggerStay2D</td>
            <td>Sent each frame where another object is within a trigger collider attached to this object (2D physics only).</td>
        </tr>
        <tr>
            <td>OnTriggerExit2D</td>
            <td>Sent when another object leaves a trigger collider attached to this object (2D physics only).</td>
        </tr>
    </tbody>
</table>

**输入系统相关**
<table class="table table-striped  table-hover">
    <theader>
        <th>名称</th>
        <th>注释</th>
    </theader>
    <tbody>
        <tr>
            <td>OnMouseDown</td>
            <td>OnMouseDown is called when the user has pressed the mouse button while over the GUIElement or Collider.</td>
        </tr>
        <tr>
            <td>OnMouseOver</td>
            <td>OnMouseOver is called every frame while the mouse is over the GUIElement or Collider.</td>
        </tr>
        <tr>
            <td>OnMouseUp</td>
            <td>OnMouseUp is called when the user has released the mouse button.</td>
        </tr>
        <tr>
            <td>OnMouseDrag</td>
            <td>OnMouseDrag is called when the user has clicked on a GUIElement or Collider and is still holding down the mouse.</td>
        </tr>
        <tr>
            <td>OnMouseEnter</td>
            <td>OnMouseEnter is called when the mouse entered the GUIElement or Collider.</td>
        </tr>
        <tr>
            <td>OnMouseExit</td>
            <td>OnMouseExit is called when the mouse is not any longer over the GUIElement or Collider.</td>
        </tr>
        <tr>
            <td>OnMouseUpAsButton</td>
            <td>OnMouseUpAsButton is only called when the mouse is released over the same GUIElement or Collider as it was pressed.</td>
        </tr>
    </tbody>
</table>

**渲染相关**
<table class="table table-striped table-hover">
    <theader>
        <th>名称</th>
        <th>注释</th>
    </theader>
    <tbody>
        <tr>
            <td>OnPreCull</td>
            <td>OnPreCull is called before a camera culls the scene.</td>
        </tr>
        <tr>
            <td>OnBecameVisible</td>
            <td>OnBecameVisible is called when the renderer became visible by any camera.</td>
        </tr>
        <tr>
            <td>OnBecameInvisible</td>
            <td>OnBecameInvisible is called when the renderer is no longer visible by any camera.</td>
        </tr>
        <tr>
            <td>OnWillRenderObject</td>
            <td>OnWillRenderObject is called once for each camera if the object is visible.</td>
        </tr>
        <tr>
            <td>OnPreRender</td>
            <td>OnPreRender is called before a camera starts rendering the scene.</td>
        </tr>
        <tr>
            <td>OnRenderObject</td>
            <td>OnRenderObject is called after camera has rendered the scene.</td>
        </tr>
        <tr>
            <td>OnPostRender</td>
            <td>OnPostRender is called after a camera finished rendering the scene.</td>
        </tr>
        <tr>
            <td>OnRenderImage</td>
            <td>OnRenderImage is called after all rendering is complete to render image.</td>
        </tr>
        <tr>
            <td>OnGUI</td>
            <td>OnGUI is called for rendering and handling GUI events.</td>
        </tr>
        <tr>
            <td>OnDrawGizmos</td>
            <td>Implement OnDrawGizmos if you want to draw gizmos that are also pickable and always drawn.</td>
        </tr>
    </tbody>
</table>

###**用图来表示MonoBehavior事件执行顺序**   
![MonoBehavior事件执行顺序](http://wudixiaop.github.io/images/monobehaviour_flowchart.svg)

###**总结:**
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

