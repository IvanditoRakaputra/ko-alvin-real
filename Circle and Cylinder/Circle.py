import math
class Circle():
    def __init__(self, radius = 1.0, color = 'red'):
        self.radius = radius
        self.color = color
    def getRadius(self):
        return self.radius
    def getColor(self):
        return self.color
    def setRadius(self, radius):
        self.radius = radius
    def setColor(self,color):
        self.color = color
    def getArea(self):
        return math.pi*self.getRadius()**2
    