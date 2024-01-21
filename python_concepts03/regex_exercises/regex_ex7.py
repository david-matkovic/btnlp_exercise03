import re

def find_sequences(string):
    pattern = ("^[a-z]+_[a-z]+$".re.IGNORECASE)
    if re.search(pattern, string):
        return "Yes"
    else:
        return "NO"