import re


def search_numbers(string):
    pattern = r"\b\d{1,3}\b"
    matches = re.findall(pattern, string)
    if matches:
        for match in matches:
            print(match)
    else:
        print("Nothing to be found")


print(search_numbers("Exercises number 1, 12, 13, and 345 are important"))