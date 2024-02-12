import os
def reverse_and_rewrite(input_file, output_file):
    with open(input_file, 'r') as reader:
        lines = reader.readlines()

    with open(output_file, 'w') as writer:
        writer.writelines(reversed(lines))

    with open(input_file, 'w') as writer:
        writer.write("")
    os.remove(input_file)    

if __name__ == '__main__':
    input_filename = "text.txt"
    backup_filename = "text_backup.txt"
    output_filename = "reversed_test.txt"
    
    with open(input_filename, 'r') as reader:
        with open(backup_filename, 'w') as writer:
            writer.write(reader.read())

    reverse_and_rewrite(input_filename, output_filename)
