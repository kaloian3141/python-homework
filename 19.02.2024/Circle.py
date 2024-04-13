from Shape import Shape
import turtle

class Circle(Shape):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y)
        self.__radius = radius
        self.__color = color
    
    def draw(self):
        x = self.get_coordinates_X()
        y = self.get_coordinates_Y()
        
        t = turtle.Turtle()
        t.penup()
        t.goto(x,y - self.__radius)
        t.speed(10)
        t.pencolor(self.__color)
        t.pendown()
        t.circle(self.__radius)
        
        perimeter = 2 * 3.14 * self.__radius
        t.penup()
        t.goto(x,y)
        t.pencolor("black")
        t.pendown()
        t.write(f"Circumference: {perimeter}", align="center")
        t.penup()
        


