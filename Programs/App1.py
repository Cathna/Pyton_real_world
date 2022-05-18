import json
from difflib import get_close_matches
data = json.load(open("data.json"))

#the defined function will check the entered word agains the data
def translate(w):
    w = w.lower()#changes uppercase to lowercase
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(w, data.keys())[0]
    else:
        return "The word does not exist. Please check the word"

word = input("Enter word: ")

print(translate(word))
