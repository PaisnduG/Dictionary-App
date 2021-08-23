import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), n=5, cutoff=0.7)) > 0:
        yn = input("Did you mean {} instead? Enter Y if is yes, or N if no: ".format(get_close_matches(word, data.keys(), n=5, cutoff=0.7)[0]))
        if yn == "Y":
            return data[get_close_matches(word, data.keys(), n=5, cutoff=0.7)[0]]
        elif yn == "N":
            return "The word does not exist."
        else:
            return "We didn't understand your query."
    else:
        return "The word does not exist."

word = input("Enter Word: ")

output = translate(word)

if isinstance(output, list):
    for item in output:
        print(item)
else:
    print(output)