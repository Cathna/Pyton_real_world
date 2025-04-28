temps = [221, 234, 340, -9999, 230]


#new_temps = []
#for temp in temps:
#    new_temps.append(temp /10)
#new_temps =[temp /10 for temp in temps]
#new_temps = [temp / 10 for temp in temps if temp != -9999]
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps)

#In this section you learned that:

#A list comprehension is an expression that creates a list by iterating over another container.
#A basic list comprehension:
#[i*2 for i in [1, 5, 10]]
#Output: [2, 10, 20]
#List comprehension with ifcondition:
#[i*2 for i in [1, -2, 10] if i>0]
#Output: [2, 20]
#List comprehension with an ifandelsecondition:
#[i*2 if i>0 else 0 for i in [1, -2, 10]]
#Output: [2, 0, 20]
