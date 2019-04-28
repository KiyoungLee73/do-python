class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
 
rect = Rectangle(x1=20, y1=20, x2=40, y2=30)

x = abs(rect.x1 - rect.x2)
y = abs(rect.y1 - rect.y2)
area = x*y

print(area)


import math
 
class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
 
length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())

x1 = abs(p[0].x - p[1].x)
x2 = abs(p[1].x - p[2].x)
x3 = abs(p[2].x - p[3].x)
y1 = abs(p[0].y - p[1].y)
y2 = abs(p[1].y - p[2].y)
y3 = abs(p[2].y - p[3].y)

length = math.sqrt(x1**2 + y1**2) + math.sqrt(x2**2 + y2**2) + math.sqrt(x3**2 + y3**2)



print(length)