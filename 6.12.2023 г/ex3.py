def file_reading_function(filename,string):
    dict_of_lines = {}
    with open(filename,'r') as reader:
        lines = reader.readline()
    for line in lines: 
      current_line_number=1
      for word in line.split():
        if word==string:
          dict_of_lines[current_line_number] += 1
      current_line_number += 1
    with open("new_text.txt",'w') as writer:
       for elements in dict_of_lines:
          max_element=elements
          
          for second_element in dict_of_lines:
             if second_element>max_element:
               max_element=second_element

          writer.write(max_element,"\n")
          dict_of_lines.pop(max_element)
                

if __name__ == '__main__':
    input_filename = "text.txt"
    input_string = "of"
    file_reading_function(input_filename,input_string)
