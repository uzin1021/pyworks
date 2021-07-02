import re

p = re.compile("(\w+)\s(\d+[-]\d+[-]\d+)")
m = p.search("jang 010-1234-1234")
print(m)
print(m.group())
print(m.group(1))
print(m.group(2))

