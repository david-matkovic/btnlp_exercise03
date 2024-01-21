import re

match = re.search("a*", "aaaaab")

if match:
    print("I've got:", match.group())



def character_match(text):
    matching = "^a(b*)$"
    if re.search(matching, text):
        return "We've got something here"
    else:
        return "No such luck"

