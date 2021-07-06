# {m} m은 반복 횟수
import re

str = "123?45dd7890 hi 233334 hello"
m1 = re.findall("\d{1,3}", str)
print(m1)

m2 = re.findall("[A-z]+", str)
print(m2)

m3 = re.findall("[1-5]{1-2}", str)
print(m3)