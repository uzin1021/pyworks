import re
p = re.compile('[a-z]+')
str = "hello"
m = p.match("hello")

print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())

print("=======search=========")
# search
p2 = re.compile('[a-z]+')
m2 = p2.search("2021 incheon")
print(m2)
print(m2.group())
print(m2.start())
print(m2.end())
print(m2.span())
