﻿import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        distx = x - self.getx()
        disty = y - self.gety()
        return math.hypot(distx,disty)

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(0, 2))
