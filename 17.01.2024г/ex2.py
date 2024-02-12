class Rectangle:
    def __init__(self,name,lengh,weight):
        self.__name__=name
        self.__lengh__=lengh
        self.__weight__=weight
      
       
    def Finding_area(self):
        area=0
        area = self.__lengh__*self.__weight__ 
        return area  
    def Finding_perimeter(self):    
        perimeter=0
        perimeter=2*(self.__lengh__+self.__weight__)
        return perimeter
    def Finding_diagonals(self):
        diagonals =0 
        squere_of_sides=self.__lengh__**2+self.__weight__**2
        diagonals = squere_of_sides**0.5
        return diagonals
    def are_they_same(self,other):
        return self.__lengh__==other.__lengh__ and self.__weight__==other.__weight__
    def is_squere(self):
        return self.__lengh__==self.__weight__
def print_(rectangle):
    area = rectangle.Finding_area()
    perimeter = rectangle.Finding_perimeter()
    diagonals = rectangle.Finding_diagonals()
    print(f"The area of the rectangle is: {area}, The perimeter of the rectangle is {perimeter}, the diagonal of the rectangle is {diagonals}.")
if __name__ == "__main__":
    ABCD = Rectangle("ABCD",3,4) 
    MNCH = Rectangle("MNCH",1,1)
    print_(ABCD)
    if ABCD.are_they_same(MNCH):
        print("they are same")
    if MNCH.is_squere():
        print("MNCH is squere")
            
   

    