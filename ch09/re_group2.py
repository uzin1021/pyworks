import re

# 그룹핑된 문자열에 이름 붙이기
# ?P<그룹이름>
p = re.compile("(?P<name>\w+)\s(?P<phone>\d+[-]\d+[-]\d+)")
m = p.search("jang 010-1234-1234")
print(m.group())
print(m.group("name"))
print(m.group("phone"))


