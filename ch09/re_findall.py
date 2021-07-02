import re

str = 'Two is too'
f1 = re.findall('T[ow]o', str) # findall 대소문자 구분
print(f1)

f2 = re.findall('T[ow]o', str, re.IGNORECASE)
print(f2)

f3 = re.findall('t[^w]o', str, re.IGNORECASE)
print(f3)