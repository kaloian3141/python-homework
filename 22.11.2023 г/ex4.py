def write_arr_to_file(file_name, arr):
 
        with open(file_name, 'a') as writer:
            for element in arr:
                writer.write(str(element))
                writer.write("\n")
if __name__ == '__main__':
   file_name = "output1.txt"
   my_array = [1, 24, 13, 41, 51]
   write_arr_to_file(file_name, my_array)
        