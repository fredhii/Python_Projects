import json
from difflib import get_close_matches
data = json.load(open("original.json"))

def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("\nDid you mean \033[96m%s\033[0m insted?" %get_close_matches(word, data.keys())[0])
        decide = input("Press Y to confirm otherwise press any other key: ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        return "Pugger your paw steps on wrong key c:"

    return "Pugger your paw steps on wrong key c:"

print("Insert word to search for: ")
word = input()
word = word.lower()
out = translate(word)

if type(out) == list:
    for item in out:
        print("\n\033[96m", item)
        print("\n")
else:
    print("\n\033[96m", out)
    print("\n")