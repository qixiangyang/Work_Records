"""
Description:
Author:qxy
Date: 2019-07-05 13:38
File: class_method 
"""

import uuid


class Person(object):
    nationality = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__id = str(uuid.uuid1())

    # 成员方法/实例方法
    def sayHello(self):
        print('Hello, i am %s from %s, i am %d years old.' % (self.name, self.nationality, self.age))

    # 私有方法
    def __func0(self):
        print('private method: func0')
        print(self.name, self.age, self.__id, self.nationality)

    # 类方法
    @classmethod
    def func1(cls):
        print(cls.nationality)

    # 静态方法
    @staticmethod
    def func2(a, b):
        print(a + b)
        return a + b

    @property
    def func3(self):
        return '%s: %d' % (self.name, self.age)


p = Person('tom', 18)
p.sayHello()
Person.sayHello(p)

Person.func1()
Person.func2(1, 2)
b = Person.func3
print(b)

"""
总结：

成员方法也可以通过类名去访问，但是有点多此一举的感觉；

类方法和静态方法也可以通过实例对象去访问，但是通常情况下都是通过类名直接访问的；

最重要的一条总结：类的各种方法，能访问哪些属性实际上是跟方法的参数有关的：
比如成员方法要求第一个参数必须是一个该类的实例对象，那么实例对象能访问的属性，成员方法都能访问，而且还能访问私有属性；
再比如，类方法要求第一个参数必须是当前类，因此它只能访问到类属性/公有属性，而访问不到成员属性 和 私有属性；

再比如，静态方法对参数没有要求，也就意味着我们可以任意给静态方法定义参数；

假如我们给静态方法定义了表示当前类的参数，那么就可以访问类属性/公有属性；
假如我们给静态方法定义了表示当前类的实例对象的参数，那么就可以访问成员属性；
假如我们没有给静态方法定义这两个参数，那么就不能访问该类或实例对象的任何属性。
"""