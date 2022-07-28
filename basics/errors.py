#Syntax errors

print(1)
int(9)
int 9 #syntax error, no brackets
print(2)
print 3 #syntax error, no brackets

#print and int are functions and functions must have brackets


#Exceptions : Logic errors

a = 1
b = "2"

print(int(2.5) #print function braket missing
print(a + b) #type error, adding int to string
print(c) #name error : c is not defined
print(c/0)#ZeroDivision error

#if you cant find the answer, google it

#Error handling

def divide(a,b):
    return a/b

print(divide(1,0))# error due to 0, erro message will show 2 points

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:#name error as open except will accept all errors
        return "Zero Divison not accepted"

#you should have exceptions for all expected errors

print(divide(1,0))#will return message
#try and except allow code to run with errors
