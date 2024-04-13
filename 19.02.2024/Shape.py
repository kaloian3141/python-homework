class Shape:
    def __init__(self,x,y):
        self.__x = x   
        self.__y = y 
        
    def draw(self):
        pass
    def get_coordinates_X(self):
        return self.__x
    def get_coordinates_Y(self):
        return self.__y
    
