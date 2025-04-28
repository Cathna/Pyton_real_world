#Allows both lists and dictionaries to be run through this function
def mean(value):
#if isinstance(value, dict): can be used instead,
    if type(value) == dict:

        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean #if the return is missing there will be no output

print(mean([1, 4, 5]))

#x = 3
#y = 1
#if x > y:
#    print("x is greater than y")
#elif x == y:
#    print("x is equal to y")
#else:
#    print("x is less than y")
