import math
from Shape import Shape
import turtle
class Triangle(Shape):
    def __init__(self, x, y, side1, side2, angle1):
        super().__init__(x, y)
        self.__side1 = side1
        self.__side2 = side2
        self.__angle1 = angle1
       
    def calculate_center(self,x1,x2,x3,y1,y2,y3):
        center_x = (x1 + x2 + x3) / 3   
        center_y = (y1 + y2 + y3) / 3
        return center_x, center_y
    def draw(self):
        x = self.get_coordinates_X()
        y = self.get_coordinates_Y()
        side3 = math.sqrt(self.__side1**2 + self.__side2**2 - 2 * self.__side1 * self.__side2 * math.cos(math.radians(self.__angle1)))
        perimeter = self.__side1 + self.__side2 + side3
        semiperimeter = perimeter / 2
        area = math.sqrt(semiperimeter * (semiperimeter-self.__side1) * (semiperimeter-self.__side2) * (semiperimeter-side3))
        t = turtle.Turtle()
        color = "red"
        if area > perimeter:
            color = "blue"
        elif area < perimeter:
            color = "green"
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        t.forward(self.__side1)
        angle2_cordinates = t.position()
        t.penup()
        t.goto(x, y)
        t.left(self.__angle1)
        t.pendown()
        t.forward(self.__side2)
        angle3_cordinates = t.position()
        t.goto(angle2_cordinates)
        t.end_fill()
        t.penup()
        x2, y2 = angle2_cordinates
        x3, y3 = angle3_cordinates
        center_x, center_y = self.calculate_center(x,x2,x3,y,y2,y3)
        t.goto(center_x, center_y)
        t.pendown()
        if area > perimeter:
            result = round(area, 2)
            t.write(f"Area: {result}", align="center")
        elif area < perimeter:
            t.write(f"Circumference: {perimeter}", align="center")
        
    
        

        
        

        