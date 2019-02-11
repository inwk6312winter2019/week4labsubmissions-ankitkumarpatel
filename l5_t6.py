"""

Write an add method for Points that works with either a Point object or a tuple:
•	If the second operand is a Point, the method should return a new Point whose x coordinate is the sum of the x coordinates of the operands, and likewise for the y coordinates.
•	If the second operand is a tuple, the method should add the first element of the tuple to the x coordinate and the second element to the y coordinate, and return a new Point with the result.


"""
class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return (f"{self.x},{self.y}")

    def __add__(self, other):
        return (self.x+other.x,self.y+other.y)


    def add(self, other):
        if isinstance(other, tuple):
            return (self.x + other[0], self.y + other[1])
        else:
            return self + other

center = Point(5,10)
corner = Point(10,8)
tup=(10,8)

print("sum of two point objects is:",center.add(corner))
print("sum of point object and tuple is:",center.add(tup))