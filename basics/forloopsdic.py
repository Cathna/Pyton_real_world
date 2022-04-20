students_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

for grades in students_grades.items():
    #students_grades.keys will give just the keys
    #students_grades.values will give just the values
    Print(grades)

#You can combine a dictionary for loop with string formatting to create text containing information from the dictionary:

#phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

#for pair in phone_numbers.items():
#    print("{} has as phone number {}".format(pair[0], pair[1]))


#Another (better) way to do it::

#phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

#for key, value in phone_numbers.items():
#    print("{} has as phone number {}".format(key, value))
#In both cases the output is:

#Output:

#John Smith has as phone number +37682929928

#Marry Simpons has as phone number +423998200919
