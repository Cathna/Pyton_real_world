#lists
#dir() with a data type in the brackets shows all attributes
#help() adding data type and attribute will tel you what it does.
#Use these in the shell command line
#dir(__builtins__)

#student_grades = [9.1, 8.8, 7.5]
student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}

#mysum = sum(student_grades)
mysum = sum(student_grades.values())
length = len(student_grades)

mean = mysum / length

print(mean)
