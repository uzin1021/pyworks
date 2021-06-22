# set() 집합 자료구조의 특징
# 순서가 없고, 중복이 허용되지 않음

s = set() #빈 집합 자료형 선언
s.add(1)
s.add(2)
print(s)

# 중복 저장 안되고, 순서도 자유로움
s2 = set(['cow', 'dog', 'cat', 'dog', 'cat'])
print(s2)

# 리스트와 비교 (순서대로 나열)
ani = (['cow', 'dog', 'cat', 'dog', 'cat'])
print(ani)
