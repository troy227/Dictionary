import json
import difflib

data=json.load(open("data.json",'r'))
word=input("")
word=word.lower()
def translate(word):
    if word in data:
        
        return data[word]
    elif word.title() in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif difflib.get_close_matches(word,data.keys(),1,cutoff=0.8):
        cword=difflib.get_close_matches(word,data.keys(),1)
        choice=input("You mean %s ? Enter Y if Yes or N if No-"% cword[0])
        if choice.upper()=='Y':
            mean=data[cword[0]]
            return mean
        elif choice.upper()=='N':
            return("The Word Doesn't Exist")
        else:
            return("We didnt Understand your query")
        
        
    else:
        return("No such word Exists. Please Try again")
output=(translate(word))
for i in output:
    print(i)
