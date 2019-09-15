"""
Description:
Author:qxy
Date: 2019-07-02 16:10
File: property_usage 
"""
import math


class Circle:
    def __init__(self, radius):  # 圆的半径radius
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2  # 计算面积

    def perimeter(self):
        return 2 * math.pi * self.radius  # 计算周长


c = Circle(10)
print(c.radius)
print(c.area())
print(c.perimeter)