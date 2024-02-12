class student:
    def __init__(self, name, number, grades):
        self.__name__ = name
        self.__number__ = number
        self.__grades__ = grades
    def __str__(self): 
        return f"student {self.__name__} number {self.__number__} is with {self.__grades__} grades"
    def is_student_with_6(self):
        avg_grade = (self.__grades__[0]+self.__grades__[1])/len(self.__grades__)
        return avg_grade>=5.50
           
    def is_student_with_4(self):
        avg_grade = (self.__grades__[0]+self.__grades__[1])/len(self.__grades__)
        return avg_grade >=3.50 and avg_grade < 4.50

        
    
def is_student(filename):
    students = []
    with open(filename, "r", encoding="utf-8") as reader:
        lines = reader.readlines() 
    
    for line in lines:
        words = line.split()
        name = " ".join(words[1:-2])
        grades = [float(words[-2]),float(words[-1])]
        students.append(student(name,words[0],grades))
    students_with_4 = 0     
    avg = 0
    for element in students:
        avg =avg+element.__grades__[0]+element.__grades__[1]
        if element.is_student_with_6():
            print(element)
        elif element.is_student_with_4():
            students_with_4+=1    
    print("students with 4 ",students_with_4)
    print(avg)
    avg=avg/(len(students)*2)
    avg = round(avg,2)
    print("average of the class is" ,avg)
    if avg<4.5:
        print("The test was hard")
    else:
        print("the test wasnt hard")    
if __name__ == "__main__":
    input_filename = "9a_class.txt"
    output_filename = "results.txt"
    is_student(input_filename,output_filename)  