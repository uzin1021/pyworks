import re

# '*'와 '+'의 차이 비교
# '*'는 앞 문자가 0개이상 반복 (없어도 가능)

pat = re.compile("ca*t")
m1 = re.findall(pat,"caat")

pat = re.compile("ca*t")
m2 = re.findall(pat,"ct")

print(m1)
print(m2)

# '+'는 앞 문자가 1개 이상 반복
pat2 = re.compile("ca+t")
m3 = re.findall(pat2,"caat")
print(m3)
m4 = re.findall(pat2,"ct")
print(m4)

