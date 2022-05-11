#def area(a, b):
#    return a * b

#def area( a, b=6) this hasa default arg for b, non default args cannot come after a default arg

#print(area(4, 5))non keyword arg
#print(area(a=4, b=5))keyword args

#below is for non key word args
def mean(*args): #unlimited args can be entered(any word can be used inplace of args)
    return sum(args) / len(args)

print(mean(1, 5, 20, 90))# only numbers can be entered

#below is the same funtion for keyword args
def mean(**kwargs):
    return kwargs

print(mean(a=1, b=2, c=3))


In this section you learned that:

Functions can have more than one parameter:
def volume(a, b, c):
    return a * b * c
Functions can have defaultparameters (e.g. coefficient):
def converter(feet, coefficient = 3.2808):
    meters = feet / coefficient
    return meters

print(converter(10))
Output: 32.808

Arguments can be passed as non-keyword(positional) arguments (e.g. a) or keywordarguments (e.g. b=2and c=10):

def volume(a, b, c):
    return a * b * c

print(volume(1, b=2, c=10))
An *args parameter allows the function to be called with an arbitrary number of non-keyword arguments:
def find_max(*args):
    return max(args)
print(find_max(3, 99, 1001, 2, 8))
Output: 1001

An **kwargsparameter allows the function to be called with an arbitrary number of keyword arguments:
def find_winner(**kwargs):
    return max(kwargs)
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
Output: Sim

Here's a summary of function elements:
