import re


string = '**//Python Exercises// - 12. '
pattern = re.compile('[\W_]+')
print(pattern.sub('', string))