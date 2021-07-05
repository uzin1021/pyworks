import datetime
import time


# 7
def find_max(li):
    max = li[0]
    #n = len(li)
    '''
    for i in range(1,n):
        print(max)
        if max < li[i]:
            max = li[i]
    return max
    '''
d1 = [-8,2,7,5,-3,5,0,1]


max = max(d1)
min = min(d1)
print(max)
print(min)
print(max + min)

print("=============================================")
# 8
# 1. 내장으로 round
# 2. math 모듈 사용


# 12
now = datetime.datetime.now()
print(now.strftime("%Y/%m/%d/ %H:%M:%S"))

# 13
import random

lotto = []
n = len(lotto)
while n < 6:
    num = random.randint(1,45)
    if num not in lotto:
        lotto.append(num)

print(lotto)