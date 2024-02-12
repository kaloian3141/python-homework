def copy_nth_line(output_file, n):
    input_file = "text.txt"

    with open(input_file, 'r') as reader:

        lines = reader.readlines()
    with open(output_file, 'w') as writer:
        
        for i in range(0, len(lines), n):
            writer.write(lines[i])

if __name__=='__main__':
   output_filename = "output.txt"  
   n = 2  
   copy_nth_line(output_filename, n)