# 정규 표현식 예제
import re

p = re.compile('[a-z]+')  # +는 반복을 의미하는 문자
m = p.match('afternoon')

print(m)


'''
match() : 처음부터 문자를 검색 - find()와 같음
'''