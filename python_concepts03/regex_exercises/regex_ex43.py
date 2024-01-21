import re


text = "ThisIsARandomString"
print(re.findall('[A-Z][^A-Z]*', text))
