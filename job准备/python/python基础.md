python线程收GIL的限制，任何时候都只允许运行一个线程



一个python进程通常不能同时使用多个CPU核心



# python基础

1. 变量

   python中的变量理解为附在对象上的标注

   为了理解python中的赋值语句，应该始终先读右边。对象在右边创建或获取，在此之后左边的变量才会绑定到对象上，这就像为变量贴上标签。

   为对象贴上标签： 先有对象，随后贴上标签

   变量比作盒子：现有盒子(变量)，后有对象，把对象装进盒子

2. is与==的区别

   1. is比较对象的标识，==比较两个对象的值

      1. 常使用is检查变量绑定的值是不是None

         ~~~
         X is None    
         X is not None
         ~~~

   2. is运算符比 == 速度快

      1. 因为is不能重载，不需要寻找和调用特殊方法，而是直接比较两个整数ID。
      2. 而a == b是语法糖，等同于a.\__eq\__(b)。继承自object类的\__eq\__()方法比较两个对象的id(),结果是与is一样。但是多数内置类型使用更有意义的方式覆盖了\__eq\__()方法，会考虑对象属性的值。

3. 不可变的数据类型

   1. 元组的相对不可变性
      1. 指的是元组数据结构的物理内容(即保存的引用)不可变，与引用的对象无关。

4. 浅复制与深复制

     复制对象时，相等性和标识之间的区别有更深入的影响。**副本与源对象相等，但是ID不同**。

   1. 举例：列表的浅复制--即只复制了最外层的容器，副本的元素是源容器的元素的引用

      1. 构造方法list()或[:]做的是浅复制

         ~~~

         ~~~

      2. 浅复制容易操作，但得到的结果可能并不是你想要的

   2. 深复制--即副本不共享内部对象的引用

      ~~~ 
      import copy

      a = [1,2,3]

      #浅复制
      b = copy.copy(a)

      #深复制
      c = copy.deepcopy(a)
      ~~~

      ​			

7. 函数参数作为引用时

   1. 共享传参：指函数各个形参获得实参中各个引用的副本。也就是说，函数内部的形参是实参的别名

   后果:函数可能会修改作为参数传入的可变对象，但是无法修改那些对象的标识

   ~~~
   >>> a = [1, 2]
   >>> b = [3, 4]
   >>> f(a, b)
   [1, 2, 3, 4]
   >>> a, b 
   ([1, 2, 3, 4], [3, 4])
   ~~~

    2. 不要使用可变类型作为参数的默认值

       ~~~
       class HauntedBus:
           """备受幽灵乘客折磨的校车"""
           def __init__(self, passengers=[]): ➊
           	self.passengers = passengers 
           def pick(self, name):
           	self.passengers.append(name) 
           def drop(self, name):
           	self.passengers.remove(name)
       ~~~


       >>> bus1 = HauntedBus(['Alice', 'Bill'])
       >>> bus1.passengers
       ['Alice', 'Bill']
       >>> bus1.pick('Charlie')
       >>> bus1.drop('Alice')
       >>> bus1.passengers 
       ['Bill', 'Charlie']
    
    
       >>> bus2 = HauntedBus() ➋
       >>> bus2.pick('Carrie')
       >>> bus2.passengers
       ['Carrie']
       >>> bus3 = HauntedBus() ➌
       >>> bus3.passengers ➍
       ['Carrie']
       >>> bus3.pick('Dave')
       >>> bus2.passengers ➎
       ['Carrie', 'Dave']
       >>> bus2.passengers is bus3.passengers ➏
       True
       >>> bus1.passengers ➐
       ['Bill', 'Charlie']

   问题在于，没有指定初始乘客的HauntedBus 实例会共享同一个乘客列表。self.passengers 变成了passengers 参数默认值的别名。

   **解决方法：使用None作为接受可变值的参数的默认值。如果passagers不是None，正确的实现会把passageers的副本赋值给self.passagers，也就是使用list()构造方法**



8. del与垃圾回收

   Python中没有直接销毁对象的机制。del语句删除名称，而不是对象。

   在CPython 中，垃圾回收使用的主要算法是引用计数。

9. 鸭子类型

   是一种编程风格。比如想操作某个对象，你不会去判断它是否属于某种类型，而会直接判断哪它是不是有你需要的方法或属性。或者更激进一些，你甚至会直接尝试调用需要的方法，假如失败了，那就让它报错好了。

   优点：1. 鸭子类型不推荐做类型检查，省去大量与之相关的繁琐工作。2.提高代码的灵活性

   缺点：1.缺乏标准 2. 过于隐士

   按照预定行为实现对象所需的方法即可。

10. classmethod与staticmethod

    1. classmethod改变了调用方法的方式，类方法的第一个参数是类本身cls，而不是实例。

       1. 常见的用途：定义备选方法；定义工厂方法来生成新实例。

       2. 它属于类但是⽆须实例化也可调⽤。

       3. 当你发现某个行为不属于实例，而是属于整个类型时，可以考虑使用类方法。

          ~~~

          ~~~

          ​

    2. staticmehod，第一个参数不是特殊的值。其实，静态方法就是普通的函数，只是碰巧在类的定义体中，而不是在模块层定义。

       1. 静态⽅法不需要访问实例的任何状态，是⼀种与状态⽆关的⽅法。因此静态⽅法其实可以改写成脱离于类的外部普通函数。
       2. 如果你发现某个⽅法不需要使⽤当前实例⾥的任何内容，那可以使⽤ @staticmethod 来定义⼀个静态⽅法。
       3. staticmethod不是特别有用。如果想定义不需要与类交互的函数，那么在模块中定义就好了。

       ~~~
       def foo(x):
           print "executing foo(%s)"%(x)

       class A(object):
           def foo(self,x):
               print "executing foo(%s,%s)"%(self,x)

           @classmethod
           def class_foo(cls,x):
               print "executing class_foo(%s,%s)"%(cls,x)

           @staticmethod
           def static_foo(x):
               print "executing static_foo(%s)"%x

       a=A()
       ~~~

       这里先理解下函数参数里面的self和cls.这个self和cls是对类或者实例的绑定,对于一般的函数来说我们可以这么调用`foo(x)`,这个函数就是最常用的,它的工作跟任何东西(类,实例)无关.对于实例方法,我们知道在类里每次定义方法的时候都需要绑定这个实例,就是`foo(self, x)`,为什么要这么做呢?因为实例方法的调用离不开实例,我们需要把实例自己传给函数,调用的时候是这样的`a.foo(x)`(其实是`foo(a, x)`).类方法一样,只不过它传递的是类而不是实例,`A.class_foo(x)`.注意这里的self和cls可以替换别的参数,但是python的约定是这俩,还是不要改的好.

       对于静态方法其实和普通的方法一样,不需要对谁进行绑定,唯一的区别是调用的时候需要使用`a.static_foo(x)`或者`A.static_foo(x)`来调用.

11. 单下划线和双下划线

    1. 单下划线变量：约定表示“受保护”的属性，或叫“私有”属性
    2. 双下划线变量：python会把该属性名存入实例的\__dict__属性中，而且会在前面加上一个下划线和类名。比如Dog类中\__mood会变成_Dog\__mood。以防与父类中属性名发生冲突

12. read,readline和readlines

    - read 读取整个文件
    - readline 读取下一行,使用生成器方法
    - readlines 读取整个文件到一个迭代器以供我们遍历

13. 闭包

    1. 是一种函数，它会保留在定义函数时存在的自由变量的绑定，这样在调用函数时，虽然定义作用域不可用了，但是仍能使用那些绑定

14. 面向切面编程AOP和装饰器

    AOP：就是面向特定方法编程。作用：在程序运行期间在不修改源代码的基础上对已有方法进行增强。(无侵入性：解耦)

    装饰器：是可调用的对象，其参数是另外一个函数(被装饰的函数)。装饰器可能会处理被装饰的函数，然后将它返回，或者将其替换成另外一个函数或可调用对象。

    1. nonlocal关键词声明：内嵌函数中对于外部不可变类型比如数字，字符串，元组时，只能读取，不能修改，为了解决这个问题，引入nonlocal,  **将变量标记为自由变量**。

    2. functools.wraps，把被装饰函数的相关属性复制到装饰器中被替换的函数中

    3. functools.lru_cache,它实现了备忘功能。把耗时的函数的结果保存起来，避免传入相同的参数时重复计算。

    4. 叠放装饰器

       ​	把@d1 和@d2 两个装饰器按顺序应用到f 函数上，作用相当于f = d1(d2(f))。

       ~~~
           @d1
           @d2
           def f():
               print('f')
               
       等同于：
           def f():
               print('f')
           f = d1(d2(f))
       ~~~

    5. 参数化装饰器

       1. 解析源码中的装饰器时，python会把被装饰函数作为第一个参数传递给装饰器函数。那么，怎么让装饰器函数接受其他的参数尼？

          答：创建装饰器工厂函数，把参数传递给他，返回一个装饰器，然后再把它应用到要装饰的函数上。

          ~~~
          #现在是一个set 对象，这样添加和删除函数的速度更快。
          registry = set() ➊

          #registry接受一个可选的关键字参数
          def register(active=True): ➋

          	#decorate 这个内部函数是真正的装饰器；注意，它的参数是一个函数。
          	def decorate(func): ➌
          		print('running register(active=%s)->decorate(%s)'
          				% (active, func))
          		if active: 
          			registry.add(func)
          		else:
          			registry.discard(func) 
          			
          		#decorate是装饰器，必须返回一个函数
          		return func 
          		
          	#registry是工厂函数，因此返回decorate
          	return decorate 
          	
          @register(active=False) 
          def f1():
          	print('running f1()')
          	
          #即使不传入参数，register 也必须作为函数调用（@register()），
          #即要返回真正的装饰器decorate。	
          @register() 
          def f2():
          	print('running f2()')
          	
          def f3():
          	print('running f3()')
          ~~~

          这里的关键是，register() 要返回decorate，然后把它应用到被装饰的函数上。

          如果不使用@ 句法，那就要像常规函数那样使用register；若想把f 添加到registry
          中，则装饰f 函数的句法是register()(f)；不想添加（或把它删除）的话，句法是
          register(active=False)(f)。

       2. 参数装饰器通常会把被装饰函数替换掉，而且结构上需要多一次嵌套。（3层）

          举例：

          ~~~
          import time
          DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'
          ~~~


          #接受一个可选的关键字参数
          def clock(fmt=DEFAULT_FMT): ➊
          	def decorate(func): ➋
          		def clocked(*_args): ➌
          			t0 = time.time()
                      _result = func(*_args) ➍
                      elapsed = time.time() - t0
                      name = func.__name__
                      args = ', '.join(repr(arg) for arg in _args) ➎
                      result = repr(_result) ➏
                      print(fmt.format(**locals())) ➐
                   #返回被装饰函数的原结果
          		return _result ➑
          	
          	#返回被替换的函数
          	return clocked ➒
          	
          #返回真正的装饰器
          return decorate ➓
    
    
          if __name__ == '__main__':
              @clock()
              def snooze(seconds):
                  time.sleep(seconds)
    
              for i in range(3):
                  snooze(.123)
          ~~~
    
          以上参数化装饰器必须**作为函数调用**，提供参数或不提供参数也都必须要带上括号。
    
       3. 有什么办法省去那对括号？
    
          利用仅限关键词参数
    
    6. 类实现装饰器
    
       1. 函数替换（有参装饰器）---  **适合用来实现接受参数的装饰器**
    
          \__call\__()魔术方法：如果类实现了这个方法，则它的实例会变成可调用的对象。
    
          优点：相比三层嵌套的闭包函数，用类函数替换代码更清晰一些，里面的嵌套代码也少了一层
    
          本质：虽然装饰器是类实现的，但是用来替换原函数的对象，仍然是一个处\__call\__方法里的闭包函数
    
       2. 实例替换
    
          1. 实现无参装饰器
    
              被装饰函数func会作为唯一的初始化参数传递到类的实例化方法\__init\__()中。同时，类实例会作为包装对象替换原	 	   始函数。
    
          2. 实现有参装饰器
    
              先修改类的实例化⽅法，增加额外的参数，再定义⼀个新函数，由它来负责基于类创建新的可调⽤对象，这个新函数同时也是会被实际使⽤的装饰器。
    
    7. 装饰器实战--wrapt模块
    
       实现自动注入函数参数的装饰器。在装饰函数后，会在后者被调用时自动生成一个随机数，并将其注入为函数的第一个位置参数。
    
       发现问题：用来修饰类方法时，却输出了类实例self对象
    
       解决：wrapt
    
       ~~~ 
       import wrapt
    
       def provide_number(min_num, max_num):
    
           @wrapt.decorator
           def wrapper(wrapped, instance, args, kwargs):
               # 参数含义：
               #
               # - wrapped：被装饰的函数或类⽅法
               # - instance：
               # - 如果被装饰者为普通类⽅法，则该值为类实例
               # - 如果被装饰者为 classmethod 类⽅法，则该值为类
               # - 如果被装饰者为类/函数/静态⽅法，则该值为 None
               #
               # - args：调⽤时的位置参数（注意没有 * 符号）
               # - kwargs：调⽤时的关键字参数（注意没有 ** 符号）
               #
               num = random.randint(min_num, max_num)
               # ⽆须关注 wrapped 是类⽅法还是普通函数，直接在头部追加参数
               args = (num,) + args
               return wrapped(*args, **kwargs)
               
           return wrapper
           
           
           
       #可以完美兼容普通函数与类⽅法两种情况：    
       >>> print_random_number()
       22
       >>> Foo().print_random_number()
       93
       ~~~
    
       wrapt模块编写的人装饰器，处理解决类方法兼容问题以外，还使嵌套层级比普通装饰器少，变得更扁平，更易读。
    
       ​

15. 迭代器和生成器

    迭代是处理数据的基石。扫描内存中放不下的数据集时，我们要找到一种惰性获取数据项的方式，即按需一次获取一个数据项

    * 迭代器：一种帮你迭代其他对象的对象。最鲜明的特征是：不断对它执行next()函数会返回下一次迭代结果。

      * for循环工作的原理：先调用了iter()拿到它的迭代器，然后不断地用next()从迭代器中获取值。

      ~~~
      names = ['foo', 'bar', 'foobar']
      for name in names:
      	print(name)
      	
      	
      其实可以翻译成下⾯这样：
      iterator = iter(names)
      while True:
          try:
          	name = next(iterator)
          	print(name)
          except StopIteration:
          	break

      ~~~

      区分迭代器与可迭代对象

      一个合法的迭代器，必须同时实现\__iter\__(),\__next\__()两个魔术方法。

      可迭代对象只需要实现\__iter\__()方法，不一定得实现\__next\__方法

    * 生成器：是一种"懒惰的"可迭代对象。通常使用yield.

16. 类型注解

    是一种给函数参数，返回值以及任何变量增加类型描述的技术，大大提高代码的可读性。

    了解 typing库

17. 数据模型

    是一种定义对象行为和操作的规则。通过魔术方法实现。

    举例：当用print打印某个对象时，应该输出什么？

    答：默认行为：输出类名加上以一长串内存地址。

    ​	定义了\__str\__方法后：会返回对象的字符串化结果

18. 魔术方法

    \__str\__: 非正式的打印，注重可读性，格式应当对用户友好。比如用print()打印屏幕、用str()转化为字符串。

    \__repr\__:更为正式的打印，注重内容的完整性。比如在调试程序时。

    ~~~
    class Person:
    ...
    	def __str__(self):
    		return self.name
    		
    	def __repr__(self):
    		return '{cls_name}(name={name!r}, age={age!r},
                favorite_color={color!r})'.format( ➊
                cls_name=self.__class__.__name__, ➋
                name=self.name,
                age=self.age,
                color=self.favorite_color,
                )
                
    #结果：
    >>> p = Person('piglei', 18, 'black')
    >>> print(p)
    piglei
    >>> p
    Person(name='piglei', age=18, favorite_color='black')
    ~~~

    ​

19. 属性装饰器

    @property装饰器模糊了属性和方法间的界限，使用它，可以把方法通过属性的方式暴露出来。

    ​


        class Score:
        # 区
        __district = None
        
        #设置区值
        @property
        def distinct(self):
            return self.__district
        
        @distinct.setter
        def distinct(self,value):
            self.__district = '设置' + value
            
        @distinct.deleter
        def distinct(self):
            raise '不能删除'
    
    if __name__ == '__main__':
        a = Score()
        a.distinct  = '静安区'
        print(a.distinct)
        del a.distinct

使用@property装饰器，可以把distinct()方法变成一个虚拟属性，然后**像使用普通属性一样使用它**。

它让我们可以基于方法定义类属性，精确地控制属性的读取、赋值和删除行为，灵活地实现动态属性等功能。

20. isinstance(object,classinfo)            :用来判断一个函数是否是已知类型，类似于type()

    参数：object : 实例对象。
                 classinfo : 可以是直接或者间接类名、基本类型或者由它们组成的元组。

    ​

    ~~~
    a = 2
    isinstance(a,int)      # 结果返回 True
    isinstance(a,str)      # 结果返回 False
    isinstance(a,(str,int,list))      # 是元组中的一个，结果返回 True
    ~~~


    class Duck:
        a = 1
        def __init__(self):
            pass
    
    class D_son(Duck):
        def __init__(self):
            pass
        pass
    
    
    print(isinstance(D_son(),Duck))   #结果返回True
    
    ​~~~
    
    ​
    
    isinstance()与type()的区别？
    
    例如在继承上的区别：
    
    - isinstance() 会认为子类是一种父类类型，考虑继承关系。
    - type() 不会认为子类是一种父类类型，不考虑继承关系。

21. python的鸭子类型不关注类型，而关注行对象是否支持某些操作。而isinstance()是用来检测是否是相同类型的，这个函数是否在python中无用武之地了？

    答：不是。自从python2.6推出抽象类后，改变了一些。

    ​	1.抽象类中用@classmethod修饰__subclasshook(cls,C),我们可以定制抽象类的子类判断逻辑。这种子类形式只关心结构，不关注真正的继承关系。

     	2. .register()方法：给抽象类注册子类。

    1,2实现了一种比继承更灵活、更松散的子类机制，以此改变了isinstance(object,classinfo)的行为。只要待匹配类型classinfo是抽象类。**只检验行为，不检验类型**。

22. 抽象类

    1. @abstractmethod装饰器

       将某个方法标记为抽象方法。假如抽象类的⼦类在继承时，没有重写所有抽象⽅法，那么它就⽆法被正常实例化。

    2. 除了抽象方法外，抽象类也可以实现普通的基础方法，供子类继承使用

23. 在复杂的继承关系下，如何确认子类的某个方法会用到哪个父类？

    1. 在解决多重继承的⽅法优先级问题时，Python 使⽤了⼀种名为MRO（method resolution order）的算法。该算法会遍历类的所有基类，并将它们按优先级从⾼到低排好序。

       ~~~
       class A:
           def say(self):
           print("I'm A")
           
       class B(A):
           pass
           
       class C(A):
           def say(self):
           print("I'm C")
           
       class D(B, C):
       	pass
       	

       >>> D().say()
       I'm C
       ~~~

       调用mro()方法：，Python 会按照上⾯的 MRO 列表从前往后寻找这个⽅法，假如某个类实现了这个⽅法，就直接返回。

       ~~~
       >>> D.mro()
       [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,<class '__main__.A'>, <class 'object'>]
       ~~~

       ![70943787080](C:\Users\19125\AppData\Local\Temp\1709437870809.png)

    2. MRO与super()

       super() 是⼀个⽤来调⽤⽗类⽅法的⼯具函数。但这么说并不准确，super() 使⽤的其实不是当前类的⽗类，⽽是它在 MRO 链条⾥的上⼀个类。

       ~~~
       class A:
           def __init__(self):
               print("I'm A")
               super().__init__()

       class B(A):
           def __init__(self):
               print("I'm B")
               super().__init__()

       class C(A):
           def __init__(self):
               print("I'm C")
               super().__init__()

       class D2(B, C): ➊
       	pass
       	
       	
       >>> D2()
       I'm B
       I'm C 
       I'm A
       ~~~

       C类的\__init\__方法调用插在了B与A之间

24. namedtuple 具名元组

    1. 和元组tuple一样,NamedTuple也是不可变数据类型，创建后就不能改变内容。
    2. NamedTuple使用**.**来读写，也可以用下标索引。

    ~~~

    Point = namedtuple('Point', ['x', 'y'])
    Point = namedtuple('Point', ['x y'])
    Point = namedtuple('Point', ['x，y'])

    p = Point(11, y=22)  
    ~~~

    namedtuple()函数创建了名为Point,2个属性字段x和y的子类，将这个子类赋值给变量Point。最后一句就是普通的new的语法

25. 日志

    ~~~
    # 命名记录器： 
    logger = logging.getLogger(__name__)  #模块级记录器
    ~~~




26.类的内置属性

~~~
cls.__class__

cls.__name__

cls.__mro__

cls.__bases__

cls.__qualname__

cls.__subclasses__()

cls.mro()
~~~







s