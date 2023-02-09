import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        print('(' + str(self.x) + ', '+ str(self.y)  + ')'  )

    
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
        
    def dist(self, pt):
        dx = pt.x - self.x
        dy = pt.y - self.y
        print(math.sqrt(dx ** 2 + dy ** 2))
        
p1 = Point(2,3)
p2 = Point(1,4)

p1.move(1, 1)
p1.show()
p1.dist(p2)