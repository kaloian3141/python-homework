with open('text.txt', 'w') as writer:
    writer.write('hello there')
    writer.close()  
reader = open("text.txt", "r")
print(reader.read())
    