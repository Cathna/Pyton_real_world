import json
from difflib import get_close_matches
data = json.load(open("data.json"))

#the defined function will check the entered word agains the data
def translate(w):
    w = w.lower()#changes uppercase to lowercase
    if w in data:#entry is checked against user entry
        return data[w]#returns w if in data
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0: #if not in data checks for nearest safe word
    #displays nearest words to the entered word
        yn = input ("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        yn = yn.upper()#changes inoput to uppercase
        if yn == "Y":#runs through options and returns correct response
            return data[get_close_matches(w, data.keys())[0]]
        elif yn =="N":
            return "The word does not exist. Please check the word"
        else:
            return "We didn't understand your entry"
    else:
        return "The word does not exist. Please check the word"
#Takes output checks it and then displays correctly
word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
