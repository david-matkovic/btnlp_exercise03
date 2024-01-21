import re


def start(string):
    check = re.compile(r"^5")
    if check.match(string):
        return True
    else:
        return False