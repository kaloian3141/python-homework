import turtle
from triangle import Triangle
from Circle import Circle
from Rectangle import Rectangle
from Comparator import Comparator
from Mylist import MyList
triangle1 = Triangle(0,0,30,40,90)
triangle1.draw()
circle1 = Circle(40,20,100,"red")
circle1.draw()
rectangle1 = Rectangle(100,20,200,200,"green")
rectangle1.draw()
comparator1 = Comparator(-100,-300,200,400,60,"yellow")
comparator1.draw()
turtle.done()
list1 = MyList()
list1.append(triangle1)
list1.append(circle1)
list1.append(rectangle1)
list1.append(comparator1)
list1[2].draw()