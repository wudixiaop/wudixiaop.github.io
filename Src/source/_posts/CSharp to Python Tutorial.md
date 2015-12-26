title: 从C#到Python
date: 2015-1-07 20:13
category: 一点一滴
tags: Python
---

项目组最近可能要用Python写一插件，虽然自己只是会用，但是还是被要求给大家做个简单的Python入门培训。只能冲个胖子，硬着头皮上了。
由于项目组里大部分童鞋们都会C#，可能如果从C#做类比的角度来阐述Python语法会更好点，然后下面奇怪的Python教程出来了。大家可以在这里得到PPT和代码:  <https://github.com/wudixiaop/Nana/tree/master/Python/Tutorial/Python%20Quick%20Start>。


下面是讲语法的代码，语法部分在注释中有描述。


{% codeblock lang:python %}
    # -*- encoding:utf-8 -*-

    """
    本代码主要展示Python的基本数据类型和语法, 及其用法，希望可以帮助大家快速入门。
    如果不是C#程序员, 请忽略‘C#伪代码’, 直接通过参考‘Python规则’部分来学习
    """




    # ---------------------------------注释----------------------------------------------
    """
    语法 - 注释

    Python规则:
        1. 用#打头表示注释
        2. 用三引号的字符串块，也可以表示注释（因为编译器会忽略3引号的块）

    """



    # -----------------------------------赋值-------------------------------------------------
    """
    语法 - 赋值

    Python规则: 
        Python是动态语言，变量类型在赋值阶段决定，不像其他语言一样需要先声明变量的数据类型(如C#).

    C#伪代码: 
        string var_sample = "something"
    """
    var_sample = "someting" #变量var_sample是字符串类型




    # ------------------------------Python基本数据类型-----------------------------------------------
    #   1. 空, 用None表示。
    #   2. 布尔类型: 
    #   3. 数值类型。
    #   4. 字符串
    #   5. 列表, 也就是数组。
    #   6. 字典
    #   7. 集合(set)，无序的，不重复的元素集。
    #   8. 元组(Tuple), 和列表类似，但是一旦初始化就不能改变。

    """
    -----------------------  数据类型 - 空  -----------------------------------------
    Python规则:
        空类型用None表示, 类似C#中的null.

    C#伪代码:
        T s = null; // T表示可空类型
    """
    var_none = None

    """
    -----------------------  数据类型 - 布尔类型  --------------------------------------
    Python规则：
        True和False. 对应C#中的true和false。
        基本类型中空、任何数值类型中的0、空字符串、空元组()、空列表[]、空字典{}都被当作 False.
        布尔运算有3中not, and和or, 他们的优先级是 not > and > or

    C#伪代码:
        bool var_bool1 = true;
        bool var_bool2 = false;
        bool var_bool3 = 3 > 2;
        bool var_bool4 = !true;
        bool var_bool5 = true && true;
        bool var_bool6 = true || false;
        bool var_bool7 = false || ((!false) && true);
    """
    var_bool1 = True        # 变量值为True
    var_bool2 = False       # 变量值为False
    var_bool3 = 3 > 2       # 变量值为True
    var_bool4 = not True    # 变量值为False
    var_bool5 = True and True  # 变量值为True
    var_bool6 = True or False  # 变量值为True
    var_bool7 = False or not False and True # 变量值为 True


    """
    -----------------------  数据类型 - 数值类型  --------------------------------------
    Python规则:
        数值类型包括整型(int)和浮点数(float)
        整型前缀0b表示二机制，0O表示八进制，0X表示十六进制

    C#伪代码:
        int var_int = 1;
        int var_binary = Convert.ToInt32("0010", 2);
        int var_octal = Convert.ToInt32("0010", 8);
        int var_hex = 0x0010;
        double var_float = 1.0; // 或者 float var_float = 1.0;
    """
    var_int = 1
    var_binary = 0b0010 # 变量值为2
    var_octal = 0O0010 # 变量值为8, 0O第二个是字母O
    var_hex = 0x0010 # 变量值为16
    var_float = 1.0


    """
    -----------------------  数据类型 - 字符串  -------------------------------------- 
    python规则:
        字符串有多种表示方法，可以是
        1. 单引号
        2. 双引号
        3. 三引号, 字符串块，如果没有赋值给变量，会被编译器忽略，在这种情况下可以拿来当注释用

        字符串可以带r前缀，表示raw string, 不用转义
        字符串可以带u前缀，表示Unicode编码

    C#伪代码:
        string var_str2 = "some string";
        string var_str3 = @"C:\mydir\file.txt";
        string var_str4 = @"C:\mydir\文件.txt"; 
    """
    var_str1 = 'some string'
    var_str2 = "some string"
    var_str3 = r"C:\mydir\file.txt"
    var_str4 = u"""C:\mydir\文件.txt"""

    #下面两种字符串格式是等价的
    var_str_fromat1 = "%s %s" % (1, 2)
    var_str_format2 = "{0} {1}".format(1, 2)

    """
    -----------------------  数据类型 - 列表  -------------------------------------- 
    python规则：
        列表，即数组, 用[]表示, 可以包含不同类型的元素。 C#中的数组或者List<>与其类似，但是C#必须指明元素数据类型

    C#伪代码:
        C#的数组或List<>不能包含不同类型的元素，这里不提供类比代码。  
    """
    var_list = [1, 2, [3]]  # 初始化
    var_list[1] = '2'       # 索引下标从0开始，这段代码把第2位元素赋值为字符串'2'，取代了原来的整型2. 此时var_list值为 [1, '2', [3]]
    var_list.append(1)      # 添加一元素，此时var_list值为 [1, '2', [3], 1]
    var_list.remove(1)      # 删除一元素，从头遍历，删除第一个元素1, 此时var_list值为 ['2', [3], 1]
    var_list.remove(1)      # 继续删除1， 此时var_list值为 ['2', [3]]


    """
    ----------------------- 数据类型 - 字典  -------------------------------------- 
    python规则:
        字典，用{}表示，可以用不同的类型做key和value, key和value之间用:号连接
        C#中的Dictionary<>和这个类似，但是C#必须指明Key和Value的类型

    C#伪代码:
        C#的Dictionary<>不能包含不同类型的元素，这里不提供类比代码。  
    """
    var_dict = { 1: 'hello dictionary', '2': [1, 2, 3] }
    var_dict['2'].append('4') # 通过Key访问元素
    var_dict[3] = '3' # 添加一元素
    del var_dict[1]   # 删除已元素，用del关键词


    """
    ----------------------- 数据类型 - 集合  -------------------------------------- 
    Python规则:
        集合(set)，是一个无序的，元素不重复的集，元素可以是不同类型。C#中的HashSet<>和这个类似，但是C#中必须指定类型

    C#伪代码:
        C#的HashSet<>不能包含不同类型的元素，这里不提供类比代码。
    """
    var_set = set() # 初始化
    var_set.add(1)  # 添加一元素
    var_set.add('2') # 添加一元素, 此时var_set值为 set([1, '2']) 


    """
    ----------------------- 数据类型 - 元组 -------------------------------------- 
    Python规则:
        元组(Tuple), 用()表示，能包含不同类型元素。 和列表类似，但是一旦初始化就不能改变。C#中的Tuple<>和这个类似

    C#伪代码:
       Tuple<int, int> var_tuple = new Tuple<int, int>(10, 20); 
    """
    var_tuple = (10, 20) # 初始化
    var_tuple_item = var_tuple[1] # 访问item, 下标从0开始



    # ------------------------------循环控制-----------------------------------------------
    """
    Python规则:
        python支持for和while循环

    C#伪代码:
        for(int i; i < 10; i ++) 
        {
            // do something
        }

        foeach(var item in List) 
        {
            //do something
        }

        int count = 0;
        while (count < 10)
        {
            count += 1;
        }
    """
    for i in range(10):
        print i

    for t in var_list:
        print t

    count = 0;
    while count < 10:
        count += 1


    # ------------------------------条件判断-----------------------------------------------
    """
    Python规则:
        条件判断 if, if-else, if-elif-else，或者包含多个elif的if-elif-elif...-else, 每个关键词后要带冒号

    C#伪代码:
        if (3 > 2) {}
        
        if (3 < 2)
        {
            //pass
        }
        else
        {
           //pass 
        }

        if ( 3 < 2 )
        {
            //pass
        }
        else if (3 < 3)
        {
            //pass 
        }
        else if (3 < 4)
        {
             //pass
        }
        else
        {
             //pass
        }

    """
    if 3 > 2:
        pass

    if 3 < 2:
        pass
    else: 
        pass

    if 3 < 2:
        pass
    elif 3 < 3:
        pass
    elif 3 < 4:
        pass
    else:
        pass



    # ------------------------------异常处理-----------------------------------------------
    """
    Python规则:
        关键词try...excpet

    C#伪代码:
        try
        {
           int i = 1/0; 
        }
        catch
        {
            //pass
        }

        try
        {
            //pass
        }
        catch(ZeroDivisionError)
        {
            //pass
        }
    """
    try:
        1/0
    except:
        pass

    try:
        1/0
    except ZeroDivisionError:
        pass



    # ------------------------------函数-----------------------------------------------
    """
    Python规则:
        函数用def来声明
        没有返回值声明，返回值由函数语句中的return来指明，并且可以有多个返回值。
        参数不需要带类型名字
        函数可以赋值给变量
        函数可以嵌套

        特别关注： 一些函数会用 *args和 **kwargs当作参数来表示可变参数：
            * --  以元组作为参数传入
            ** -- 以字典做为参数传入

    C#伪代码:
        T test_function<T>(T a, T b)
        {
            return a + b;
        } 

        C#的return 没有多返回值，且可变参方法不支持不同类型，这里不提供类比代码
    """
    def test_function(a, b):
        """
        按照python的风格，方法的注释用三引号字符块表示，并且方法函数声明与其
        第一行语句中间
        """
        return a + b

    var_test_function = test_function # 函数可以赋值给变量
    var_test_function(1, 2) # 返回3
    var_test_function('1', '2') #返回'12'

    def multi_return_value_function():
        """
        多个返回值
        """
        return 1, 2, 3, 4, 5

    (one, two, three, four, five) = multi_return_value_function() 


    def multi_params_fuction(*args, **kwargs):
        """
        参数不确定时
        """
        print type(args), args
        print type(kwargs), kwargs

    multi_params_fuction(1, [1, '2'], 2, a = 3, b = [1, 2, 4, 5]) 
    """
    上面语句输出为:
    <type 'tuple'> (1, [1, '2'], 2)
    <type 'dict'> {'a': 3, 'b': [1, 2, 4, 5]}
    """

    # ------------------------------面向对象-----------------------------------------------
    """
    Python规则
        类用关键词class表示
        类可以继承，并且支持多继承
        类的构造函数名字是固定的，名字是__init__, init前后是两个下划线
        类的析构函数名字也是固定的，名字是__del__
        实例方法第一参数名字必须是self,用于传递对象本身
        静态方法用@staticmethod装饰器表示，类似于一个全局的函数
        类方法用@classmethod装饰器表示，类似于C#中的类的静态方法
        子类同名的方法会覆盖父类同名方法
        多继承中，如果不同父类有有相同明名字的字段，则其值为最近一次所赋的值。

    c#伪代码:
        class Base
        {
            public string msg;    


            public Base(string msg)
            {
                this.msg = msg;
            }

            public virtual void print_class()
            {
                Console.Writeline(this.msg);
            }

            public virtual void print_somthing()
            {
                Console.WriteLine("print something from Base")
            }
        }

        class Child : Base
        {
            public Child : base("Child")
            {
                
            }

            public override void print_somthing()
            {
                Console.WriteLine("print someting from Child");
            }
        }

        C#不支持类的多继承

    """
    class Base:
        """
        类的注释放到这里
        """
        def __init__(self, msg):
            """
            方法的注释放到这里
            __init__()是构造函数
            """
            self.msg = msg

        def __del__(self):
            """
            析构函数, 一般很少用
            """
            pass

        def print_class(self):
            print "base  {0}".format(self.msg)

        def print_somthing(self):
            print 'print something from Base'


    class Child(Base):
        """
        单继承
        """
        def __init__(self):
            Base.__init__(self, "Child") # 访问父类构造函数

        def print_somthing(self):
            """
            与父类同名，会覆盖父类的print_somthing方法
            """
            print "print someting from Child"


    class Base2:
        def __init__(self, msg):
            self.msg = msg

        def print_class(self):
            print "base2 {0}".format(self.msg)


    class Child2(Base, Base2):
        """
        多继承
        """
        def __init__(self):
            Base.__init__(self, "Child2Base") # 访问父类构造函数
            Base2.__init__(self, "Child2Base2") # 访问父类构造函数

        @staticmethod
        def static_method():
            """
            静态方法, 要带@staticmethod装饰器, 类似于一个全局的函数
            """
            print "statc methond in Child2"

        @classmethod
        def class_methond(thiscls):
            """
            类方法，要带@classmethod装饰器，类似C#中的类的静态方法, 带一个参数
            """
            print "class_method in Child2" 

        def print_child2(self):
            """
            访问父类方法
            """
            print "access static methond in class"
            Child2.static_method()  
            
            print "access class methond in class"
            Child2.class_methond() 

            print "access instance methond in parent class"
            Base.print_class(self)
            Base2.print_class(self) 


    def oop_test():
        """
        类测试方法
        """
        c = Child()
        print c.print_class()
        print c.print_somthing()

        c2 = Child2()
        Child2.static_method()
        Child2.class_methond()

        c2.print_somthing()
        c2.print_child2()
        

        # 多继承时，
        #  1. 当不同的父类有相同的字段时, 其值为最近一次所赋的值
        print c2.msg 

        #  2. 当不同父类有相同方法时, 执行继承列表中的第一个父类的方法
        c2.print_class()



    # ------------------------------模块与包-----------------------------------------------
    """
    Python规则:
        导入模块或包有好几种方式
    """
    """
    导入：  import [moudle_name or package_name]
    使用时要带上module_name或者package_name
    """
    import module
    #print module.get_module_name()

    import SamplePackage
    SamplePackage.addmodule.add(1, 2)

    """
    导入变种一： from [moudle_name or package name] import [...]
    使用时可以省略module_name或者package_name直接访问
    """
    from SamplePackage import modemodule 
    modemodule.mode(1, 2)

    """
    导入变种二： from [moudle_name or package name] import *  
    *表示导入所有
    使用时可以省略module_name或者package_name直接访问
    """
    from SamplePackage.multiplymodule import *
    multiply(1, 2)


    """
    __name__ 在默认情况下：
        1. 如果被自己模块内调用，它的值是 __main__
        2. 如果在外部模块调用，他的值是模块名字

    所以我们可以把模块内部的测试代码放到下面代码中，不会影响其他模块
    """
    if __name__ == "__main__":
        oop_test()
        
{% endcodeblock %}

上面代码地址: [Github](https://github.com/wudixiaop/Nana/blob/master/Python/Tutorial/Python%20Quick%20Start/PythonQuickStart/Python_Introduction.py)