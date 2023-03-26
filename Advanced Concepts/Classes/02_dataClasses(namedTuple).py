# class Point:
#     def __init__(self, x, y) -> None:
#         self.x =x
#         self.y = y
    
#     def __eq__(self, __o: object) -> bool:
#         return self.x==__o.x and self.y==__o.y
    
# p1=Point(1,2)
# p2=Point(1,2)
# print(p1==p2)
# this can also be achieved by namedTuple
from collections import namedtuple
# these are immutabe

point = namedtuple("Point",["x", "y"])

p1 = point(x=1, y=2)
# p1.x=10 will result in an error
p2 = point(x=1, y=2)
print(p1==p2)