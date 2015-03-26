Title: 一个例子学习Swift中的闭包用法
Date: 2015-03-26 15:37
Category: 一点一滴
Tags: Swift

初学习Swift, 觉得Swift中的闭包用法比较灵活, 所以在学习的时候编了个小例子来把用法罗列了出来, 分享出来给大家。

在讲例子之前我们来看下什么是闭包(Closure).《The Swift Programming Language》是这样定义的:
>   Closures are self-contained blocks of functionality that can be passed around and used in your code
 
中文版中这样翻译：
> 闭包是自包含的函数代码块，可以在代码中被传递和使用。

看解释我们知道，闭包是代码段，它能实现一些逻辑（函数），它可以被传递和使用（就像类型一样）。

然后我们来看看闭包长的什么样子。下面是闭包的定义:
> { (parameters) -> returnType in
>    statements
> }

上面定义中 **parameters** 是指参数， **returnType** 是返回类型，而 **statements** 指的是我们要实现的逻辑的代码, 闭包的代码都被 **{}** 包含着。
观察力强的同学们估计发现了，它怎么跟Swift的函数长的差不多，难道它们是亲戚? Swift中函数是一种特殊的闭包，记住函数是闭包，不是闭包是函数哦。

接下来我们说说文章开头提到的那个栗子。

假设我们要找出某一些人中最小年龄是多少，我们要通过排序的方法来得到这个年龄。有这么一组年龄数字:

    :::swift
    let ages = [10, 23, 15, 13, 19]

首先我们使用最原始的办法，自己定义排序方法:

    :::swift
    func sortAge(age1: Int, age2: Int) -> Bool {
        return age1 > age2
    }

    sorted(ages, sortAge)

上面代码中我们定义了一个叫做 sortAge 的函数, 它传递给了第二个参数的类型是 ``(Int, Int) -> Bool`` 的 sorted 函数。 如果用闭包来代替自定义的函数, 写法就变成了这样:

    :::swift
    sorted(ages, { (age1:Int, age2:Int) -> Bool in return age1 > age2 })

一个闭包用法就写好了。上面闭包中，定义了参数的个数，名字还有其类型，定义了返回值，还有代码体(in 关键词之后的代码)。
看起来就像重新写了一个 sortAage 函数。你可能会想，这样也没省多少事，只不过是把自定义的函数写到了 sorted 函数的参数里而已。
别急, 学会聪明的偷懒是一个好程序员属性，我们来看看怎么简化上面的代码。

首先**闭包中如果能从上下文推断出其参数类型，我们可以省略其类型的定义**。sorted 函数的, 所以我们可以简化代码为:

    :::swift
    sorted(ages, { (age1, age2) -> Bool in return age1 > age2 })

然后，用来包含参数的括号我们可以省略掉, 变成了下面这个样子：

    :::swift
    sorted(ages, { age1, age2 -> Bool in return age1 > age2 })

如果**闭包代码体中只包含单行代码, 我们可以省略 return 关键词**, 然后变成了这个样子:
    
    :::swift
    sorted(ages, { age1, age2 -> Bool in age1 > age2 })

如果**闭包中返回类型能从上下文推断出，我们可以省略返回值定义**。参照上面 sorted 函数第二个参数的定义，是可以推断出闭包返回值是 Bool。省略之后就变成了这个样子：

    :::swift
    sorted(ages, { age1, age2 in age1 > age2 })

到了这里，代码已经比较清爽了。但是偷懒的步伐还可以继续（懒惰是人类文明进化的动力）。Swift 闭包中允许用 $0, $1 $2 这样用 $n 这种符号后面接数字的形式来表示其第n个参数. 然后就可以变成这个样子:

    :::swift
    sorted(ages, { $0 > $1 })

好了，已经很短了。人类的偷懒的方法是无止境的。Swift中定义了运算符函数 ``>``, 我们可以把它传递给 sorted 函数。于是乎变成了这个样子：

    :::swift
    sorted(ages, >)

如果你还想问有没有更偷懒的方法？我只想说，兄台你醒醒吧，都只要输入一个字符而已了，你还要怎么样。。。

除了上面的一些用法外，还有一种叫做尾随闭包（就是跟在调用它的函数的屁股后面的闭包），当调用它的函数的最后一个参数是闭包时，可以使用。我们可以把

    :::swift
    sorted(ages, { $0 > $1 })

写成尾随闭包形式：
    
    :::swift
    sorted(ages) { $0 > $1 }


大概就这些。。。

 
