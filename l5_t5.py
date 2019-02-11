"""

Write an init method for the Point class that takes x and y as optional parameters and assigns them to the corresponding attributes.
•	Write a str method for the Point class. Create a Point object and print it.
•	Write an add method for the Point class.


"""

class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return print(f"{self.x},{self.y}")

    def __add__(self, other):
        return (self.x+other.x,self.y+other.y)



center = Point(5,10)
corner = Point(10,8)

print(center.__add__(corner))