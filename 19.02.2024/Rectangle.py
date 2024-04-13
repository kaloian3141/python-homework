from Shape import Shape
import turtle
import math
class Rectangle(Shape):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        self.__color = color
   
    def draw(self):
        x = self.get_coordinates_X()
        y = self.get_coordinates_Y()
        
        t = turtle.Turtle()
        t.penup()
        t.goto(x,y)
        t.fillcolor(self.__color)
        t.pendown()
        t.begin_fill()
        t.forward(self.__width)
        t.left(90)
        t.forward(self.__height)
        t.left(90)
        t.forward(self.__width)
        t.left(90)
        t.forward(self.__height)
        t.left(90)
        t.end_fill()
        t.penup()
        t.goto(x+self.__width/2,y+self.__height/2)
        area = self.__width * self.__height
        t.write(f"Area: {area}", align="center")