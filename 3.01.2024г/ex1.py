import datetime
def is_student_with_6(filename,output_filename):
    students_with_6 = []
    with open(filename, "r", encoding="utf-8") as reader:
        lines = reader.readlines()
    print("Учениците които имат оценка 6 са:")  
    with open(output_filename, "a", encoding="utf-8") as appender:   
       appender.write("Учениците които имат оценка 6 са:\n")  
       for line in lines:
        words = line.split()
        name = " ".join(words[1:-1])
        if float(words[-1])>=5.50:
            students_with_6.append(name)
            print(name)
            appender.write(name+"\n")
def is_student_with_4(filename,output_filename):
    students_with_4 = 0
    with open(filename, "r", encoding="utf-8") as reader:
        lines = reader.readlines()
    for line in lines:
        words = line.split()
        if float(words[-1])>=3.50 and float(words[-1])<4.50:
            students_with_4+=1
    print(f"\nУчениците които имат оценка 4 са {students_with_4} на брой")
    with open(output_filename, "a", encoding="utf-8") as appender: 
        appender.write(f"\nУчениците които имат оценка 4 са {students_with_4} на брой")   
def avg_of_class(filename,output_filename):   
    avg = 0
    with open(filename, "r", encoding="utf-8") as reader:
        lines = reader.readlines()
    for line in lines:
        words = line.split()
        avg+=float(words[-1])
    avg/=26
    with open(output_filename, "a", encoding="utf-8") as appender: 
        print("\nСредно аритметичната оценка е:"+"{:.2f}".format(avg))
        appender.write("\nСредно аритметичната оценка е:"+"{:.2f}".format(avg))
        if avg<4.50:
           print("\nКонтролното беше трудно!")
           appender.write("\nКонтролното беше трудно!")
        else:
           print("\nКонтролното беше лесно!")  
           appender.write("\nКонтролното беше лесно!")  
if __name__ == "__main__":
    input_filename = "9a_class.txt"
    output_filename = "results.txt"
    is_student_with_6(input_filename,output_filename)
    is_student_with_4(input_filename,output_filename)
    avg_of_class(input_filename,output_filename)
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(output_filename, "a", encoding="utf-8") as appender:
        appender.write("\n"+current_datetime)
    