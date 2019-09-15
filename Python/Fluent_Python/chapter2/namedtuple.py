"""
Description:
Author:qxy
Date: 2019-06-22 11:32
File: namedtuple 
"""

from collections import namedtuple

City = namedtuple("City", "name country population coordinates")
tokyo = City("Tokyo", "JP", 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.coordinates)

print(tokyo._fields)
print(tokyo._asdict())
# print(tokyo._make(iterable=True))


"""
切片命名
"""

