"""
Description:
Author:qxy
Date: 2019-07-05 13:31
File: class_polymorphism 
"""

"""
多态是指，相同的成员方法名称，但是成员方法的行为（代码实现）却各不相同。
这里所说的多态是通过 继承接口的方式实现的。Java中有interface，但是Python中没有。
Python中可以通过在一个成员方法体中抛出一个NotImplementedError异常来强制继承该接口的子类在调用该方法前必须先实现该方法的功能代码。
"""


class Animal(object):

    def __init__(self, name):
        self.name = name

    def walk(self):
        raise NotImplemented('Subclass must implement the abstract method by self')

    def talk(self):
        raise NotImplemented('Subclass must implement the abstract method by self')


# a = Animal('bb')
# print(a.talk())

class Dog(Animal):
    def talk(self):
        print('%s is talking：旺旺...' % self.name)

    def walk(self):
        print('%s 是一条小狗，用4条腿走路' % self.name)


class Duck(Animal):
    def talk(self):
        print('%s is talking: 嘎嘎...' % self.name)

    def walk(self):
        print( '%s 是一只鸭子，用两条腿走路' % self.name)


a = Dog('bb')
a.talk()
a.walk()

b = Duck('cc')
b.walk()
b.talk()


