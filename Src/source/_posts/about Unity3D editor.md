title: 关于 Unity 编辑器一些事儿
date: 2014-11-05 22:30
category: UnityKB
tags: Editor
---

** 本文只适合Unty 4.x**

这里描述下Unity3D编辑器使用过程中遇到的坑及其解决方法

#### 事件一：Unity3d编辑器启动时默认打开最近一次打开的项目 

默认设置中，Unity3D启动时会自动打开默认最近一次打开的项目。每当只想打开小项目，而偏偏上次打开过一个大项目时，这点让人很抓狂。 
 
**解决方法:**  
> 1. 在编辑器中打开**Unity Preferences**窗口,通过 **Edit->Preferences...**打开
> 2. 在**General**选项卡中把**Always Show Project Wizard**勾选上

#### 事件二：Project Wizard中最近打开项目记录删除不了 

一直不明白为啥不让删除呢？  

**解决方法：**  
> * **方法一：让项目地址失效**  
>> * 重名名项目文件夹
>> * 把项目移动到别的文件夹
> * **方法二：修改注册表**  
>> 删除 HKEY_CURRENT_USER\Software\Unity Technologies\Unity Editor 4.x 下面以 RecentlyUsedProjectPaths 开头的项

以后继续补充...
