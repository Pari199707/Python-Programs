import collections

Point=collections.namedtuple("Point","x y")
p1=Point(10,20)
p2=Point(30,40)

print(p1,p2)
print("Point 1:",p1.x,p1.y,", Point 2:",p2.x,p2.y)
print("x diff:",p2.x-p1.x)
print("y diff:",p2.y-p1.y)
p1=p1._replace(x=100)
print("Point 1:",p1.x,p1.y)