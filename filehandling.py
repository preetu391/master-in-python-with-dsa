file_object = open("test.txt","w+") #opening a file

file_object.write("Let's learn file handling")

read_file = file_object.read()

print(read_file)

file_object.close()