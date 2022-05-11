#myfile = open("fruits.txt")#path can go here to file
#print(myfile.read())
#cursor will start at first char of file, once read function is executed the cursor is at the end so repeating the read function will only print once.

#content = myfile.read()

#myfile.close #closes the file, to read again, you will need to open again

#print(content)
#print(content)

#the above reads the file into a variable so that you can print out multiple times

#using with statement, no need to close after using
#with open("fruits.txt") as myfile
#    content = myfile.read()

#print(content)


#with open("text/fruits.txt") as myfile:
#    content = myfile.read()

#print(content)
#with open("text/vegitable.txt", "w") as myfile:
#     myfile.write("Tomato\nCucumber\nOnion")#\n creates new lines. will overwrite contant of file
#     myfile.write("Garlic")#this will append to the end of the last entry with out the line break


with open("text/vegitable.txt", "a+") as myfile:#options here are r= read, w = write, x = newfile open to write, a= open to write to end of file, + = open file to read and write
    myfile.write("\nOkra")
    myfile.seek(0)#find begining of file
    content = myfile.read()

print(content)

 Summary: File Processing
In this section you learned that:

You can readan existing file with Python:
with open("file.txt") as file:
    content = file.read()
You can createa new file with Python and writesome text on it:
with open("file.txt", "w") as file:
    content = file.write("Sample text")
You can appendtext to an existing file without overwriting it:
with open("file.txt", "a") as file:
    content = file.write("More sample text")
You can both append and reada file with:
with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()
