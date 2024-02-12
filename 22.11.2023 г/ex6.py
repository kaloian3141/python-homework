import os
def change_name(old_name, new_name):
    with open(old_name, 'r') as reader:
        lines = reader.readlines()
        
    with open(new_name, 'w') as writer:   
        writer.writelines(lines)
    os.remove(old_name)

if __name__ == '__main__':
    old_file_name = "text_backup.txt"
    new_file_name = "text.txt"
    change_name(old_file_name, new_file_name)