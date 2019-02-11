"""
Create a new class called Rectangle, this class will have width, height and corner attributes. The corner attribute is an instance of the Point class created in Q1.

•	Write a function called “find_center” that takes a Rectangle has an argument and returns a Point that returns a Point that contains the coordinates of the center of the Rectangle. (Assuming the corner of the rectangle is on the origin)
•	Write a function named move_rectangle that takes a Rectangle and two numbers named dx and dy. It should change the location of the rectangle by adding dx to the x coordinate of corner and adding dy to the y coordinate of corner.
•	Write a version of move_rectangle that creates and returns a new Rectangle instead of modifying the old one.

"""

class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

class Rectangle():
    def __init__(self,width,height,corner = Point(0,0),center= Point(0,0)):
        self.height = height
        self.width = width
        self.corner = corner
        self.center = center

def find_center(rect):
    c = Point()
    c.x = rect.corner.x + rect.width/2
    c.y = rect.corner.y + rect.height/2
    rect.center = Point(c.x,c.y)
    return (rect)

def move_rectangle(rect,dx,dy):
    rect.corner.x += dx
    rect.corner.y += dy
    rect.center.x += dx
    rect.center.y += dy
    return (rect)


box = Rectangle(100,200)
find_center(box)
print(f"x of center= {box.center.x}, y of center= {box.center.y}")
move_rectangle(box,10,10)
print(f"x of corner = {box.corner.x}, y of corner = {box.corner.y}, x of center = {box.center.x}, y of center ={box.center.y}")