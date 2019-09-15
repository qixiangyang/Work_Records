"""
Description:
Author:qxy
Date: 2019-07-05 13:15
File: class_inheritance 
"""


# 父类/基类/超类--Person
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print("%s is walking" % self.name)

    def talk(self):
        print("%s is talking" % self.name)


# 子类--Teacher
class Teacher(Person):
    def __init__(self, name, age, level, salary):
        super(Teacher, self).__init__(name, age)
        self.level = level
        self.salary = salary

    def teach(self):
        print("%s is teaching" % self.name)


# 子类--Student
class Student(Person):
    def __init__(self, name, age, class_):
        Person.__init__(self, name, age)
        self.clase_ = class_

    def study(self):
        print("%s is studying" % self.name)


# 子类实例化
t1 = Teacher('张老师', 33, '高级教师', 20000)
s1 = Student('小明', 13, '初一3班')

t1.talk()
t1.teach()
t1.walk()

s1.talk()
s1.talk()
s1.study()

"""
继承说明
Teacher类 和 Student类 都继承 Person类，因此Teacher和Student是Person的子类/派生类，而Person是Teacher和Student的父类/基类/超类；
Teacher和Student对Person的继承属于实现继承，且是单继承；
Teacher类继承了Person的name和age属性，及talk()和walk()方法，并扩展了自己的level和salary属性，及teach()方法；
Student类继承了Person的name和age属性，及talk()和walk()方法，并扩展了自己的class属性，及study()方法；
Teacher和Student对Person类属性和方法继承体现了 “代码的重用性”， 而Teacher和Student扩展的属性和方法体现了 “灵活的扩展性”；
子类需要在自己的__init__方法中的第一行位置调用父类的构造方法，上面给出了两种方法：
super(子类名, self).__init__(父类构造参数)，如super.(Teacher, self).__init__(name, age)
父类名.__init__(self, 父类构造参数)，如Person.__init__(self, name, age)，这是老式的用法。
子类 Teacher 和 Student 也可以在自己的类定义中 重新定义 父类中的talk()和walk()方法，改变其实现代码，这叫做方法重写。
"""

"""
https://www.cnblogs.com/yyds/p/7591804.html
"""