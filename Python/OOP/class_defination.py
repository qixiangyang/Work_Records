"""
Description:
Author:qxy
Date: 2019-07-05 12:00
File: class_defination 
"""

import uuid


class Person(object):
    nationality = 'China'

    def __init__(self, name):
        self.name = name
        self.__id = str(uuid.uuid1())

    def hello(self):
        print('Hi, i am %s, from %s， my id is %s' % (self.name, self.nationality, self.__id))

    def get_and_print_id(self):
        print(self.__id)
        return self.__id


"""实例化"""
tom = Person('tom')
jerry = Person('jerry')
jack = Person('jack')

"""公共属性"""
print(Person.nationality, tom.nationality, jerry.nationality, jack.nationality)
tom.nationality = 'India'
print(Person.nationality, tom.nationality, jerry.nationality, jack.nationality)
Person.nationality = 'USA'
print(Person.nationality, tom.nationality, jerry.nationality, jack.nationality)


"""成员属性"""
print(tom.name, jerry.name, jack.name)
jerry.name = 'jerry1'
print(tom.name, jerry.name, jack.name)

"""直接访问成员属性"""
# Person.name

"""私有属性访问"""
# print(tom.__id)
# print(Person.__id)

"""通过类方法访问私有属性"""

tom.hello()
jerry.hello()
jack.hello()
"""
- 私有变量不能通过类直接访问；
- 私有变量也不能通过实例对象直接访问；
- 私有变量可以通过成员方法进行访问。
"""

"""访问私有变量"""
tom_id = tom.get_and_print_id()
jerry_id = jerry.get_and_print_id()
jack_id = jack.get_and_print_id()

print(tom._Person__id, jerry._Person__id, jack._Person__id)

"""
总结
公有属性、成员属性 和 私有属性 的受保护等级是依次递增的；
私有属性 和 成员属性 是存放在已实例化的对象中的，每个对象都会保存一份；
公有属性是保存在类中的，只保存一份；
哪些属性应该是公有属性的，哪些属性应该是私有属性 需要根据具体业务需求来确定。
"""


"""类的继承 / class inheritance"""



