# 로또 번호 생성

import random as r

lotto =  []
'''
n = r.randint(1, 45)
lotto.append(n)
print(lotto)
'''
#1 - 문제는 숫자가 중복됨.좋지않은 방법 
for i in range(6):
    n = r.randint(1,45)
    if n not in lotto:
        lotto.append(n)
    #if len(lotto) == 6:
       #break
print(lotto)

#2
lotto2= []
while len(lotto2) < 6:
    n = r.randint(1,45)
    if n not in lotto2:
        lotto2.append(n)

print(lotto2)
