import time
import os
#builtin modules and python modules
#code checks for file and runs the if or else section

while True:
    if os.path.exists("text/vegetables.txt"):
        with open("text/vegetables.txt") as file:
            print(file.read())
    else:
        print("File does not exist.")
    time.sleep(10)

#to find the built ins of a function use dir(whateveer the function)
#sys.builtin_module_names
#import os
#to check modules os.sys.prefix

#In this section you learned that:

#Builtin objectsare all objects that are written inside the Python interpreter in C language.
#Builtin modulescontain builtins objects.
#Some builtin objects are not immediately available in the global namespace. They are parts of a builtin module. To use those objects the module needs to be importedfirst. E.g.:
#import time
#time.sleep(5)
#A list of all builtin modulescan be printed out with:
#import sys
#sys.builtin_module_names
#Standard librariesis a jargon that includes both builtin modules written in C and also modules written in Python.
#Standard librarieswritten in Python reside in the Python installation directory as .pyfiles. You can find their directory path with sys.prefix.
#Packagesare a collection of .pymodules.
#Third-party librariesare packages or modules written by third-party persons (not the Python core development team).
#Third-party libraries can be installedfrom the terminal/command line:
#Windows:
#pip install pandas
#Mac and Linux:
#pip3 install pandas
