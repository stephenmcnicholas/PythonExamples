import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.one = vertice1
        self.two = vertice2
        self.three = vertice3
        self.threePoints = [self.one, self.two, self.three]
        
    def perimeter(self):
        __side1 = math.hypot(self.threePoints[0].getx() - self.threePoints[1].getx(), self.threePoints[0].gety() - self.threePoints[1].gety())
        __side2 = math.hypot(self.threePoints[1].getx() - self.threePoints[2].getx(), self.threePoints[1].gety() - self.threePoints[2].gety())
        __side3 = math.hypot(self.threePoints[2].getx() - self.threePoints[0].getx(), self.threePoints[2].gety() - self.threePoints[0].gety())
        return(__side1 + __side2 + __side3)
        
triangle = Triangle(Point(0, 0), Point(3, 0), Point(0, 4))
print(triangle.perimeter())
