def write_arr_to_file(file_name, arr):
        with open(file_name, 'r') as reader:
            lines = reader.readlines()
        with open(file_name, 'w') as writer:
            for element in arr:
                writer.write(str(element))
                writer.write("\n")
            for line in lines:
                writer.write(line)   


if __name__ == '__main__':
    file_name = "output1.txt"
    my_array = [11, 24, 133, 33, 51]
    write_arr_to_file(file_name, my_array)