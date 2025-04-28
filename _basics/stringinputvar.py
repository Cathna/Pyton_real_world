name = input("Enter your name: ")
surname = input("enter your surname: ")

message1 = "Hello %s %s!" % (name, surname)
message2 = "Hello {} {}!".format(name, surname)

print(message1)
print(message2)

#experience_months = input("Enter your experience in months: ")
#experience_years = int(experience_months) / 12)
#name = "Sim"
#experience_years = 1.5
#print("Hi %s, you have %s years of experience." % (name, experience_years))
#name = "Sim"
#experience_years = 1.5
#print("Hi {}, you have {} years of experience".format(name, experience_years))
