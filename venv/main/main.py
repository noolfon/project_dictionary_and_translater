import json
from difflib import get_close_matches
import translators as ts

data = json.load(open("data.json"))

def retrive_definition(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
        if (action == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action == "n"):
            return ("The word doesn't exist, yet.")
        else:
            return ("We don't understand your entry. Apologies.")



def run():
    while True:
        word_user = input('Enter a word("exit to theand"): ')

        if word_user == 'exit':
            break

        output = retrive_definition(word_user)

        if type(output) == list:
            tr = ts.google(word_user, to_language='ru')
            print(word_user,'>>', tr)

            for ind,item in enumerate(output):
                print(f'Numder discription: {ind+1}')
                print("-",item)
                print("-", ts.google(item, to_language='ru'))
                print()
        else:
            print("-",output, ts.google(output, to_language='ru'))


if __name__ == '__main__':
    run()