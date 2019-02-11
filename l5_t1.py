"""

Create a new class called Point. This class will have a “x” and “y” attribute.
write a function called distance_between_points that takes two Points as arguments and returns the distance between them.
Test you function by instantiating two instances and assigning them x and y attributes of type Int


"""

from math import sqrt

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def distance(p,q):
    distance = sqrt((p.x-q.x)**2+(p.y-q.y)**2)
    return(f"distance between given two points is {distance}.")                     # use of f strings


x = int(input("Enter x coordinate of point a: "))
y = int(input("Enter y coordinate of point a: "))
a = Point(x,y)

x = int(input("Enter x coordinarte of point b: "))
y = int(input("Enter y coordinarte of point b: "))
b = Point(x,y)

print(distance(a,b))



