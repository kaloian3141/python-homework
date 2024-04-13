import turtle
from Shape import Shape
import math
class Comparator(Shape):
    def __init__(self, x, y,side1,side2,angle,color):
        super().__init__(x, y)
        self.__side1 = side1
        self.__side2 = side2
        self.__angle = angle
        self.__color = color
    def calculate_center(self,x1,x2,x3,x4,y1,y2,y3,y4):
        center_x = (x1 + x2 + x3 + x4) / 4   
        center_y = (y1 + y2 + y3 + y4) / 4
        return center_x, center_y
    def draw(self):
        x = self.get_coordinates_X()
        y = self.get_coordinates_Y()
        t = turtle.Turtle()
        t.penup()
        t.goto(x,y)
        t.fillcolor(self.__color)
        t.pendown()
        t.begin_fill()
        t.forward(self.__side1)
        cordinates_of_angle2 = t.position()
        t.left(self.__angle)
        t.forward(self.__side2)
        cordinates_of_angle3 = t.position()
        t.left(180-self.__angle)
        t.forward(self.__side1)
        cordinates_of_angle4 = t.position()
        t.left(self.__angle)
        t.forward(self.__side2)
        t.end_fill()
        t.penup()
        t.goto(x,y)
        x2,y2 = cordinates_of_angle2
        x3,y3 = cordinates_of_angle3
        x4,y4 = cordinates_of_angle4
        center_x,center_y =self.calculate_center(x,x2,x3,x4,y,y2,y3,y4)
        t.goto(center_x,center_y)
        area = math.sin(math.radians(self.__angle))*self.__side1*self.__side2
        t.write(f"Area: {area}", align="center")
       
        

        
