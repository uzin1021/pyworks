import random

dice = []
for i in range(10):
    n = random.randint(1,6)
    dice.append(n)

# print(dice)
'''
# 로또 번호 생성기
lotto = []
for i in range(6):
    n = random.randint(1,45)
    lotto.append(n)

print(lotto)
'''
lotto = []
while len(lotto) < 6:
    num = random.randint(1,45)
    if i not in lotto:
        lotto.append(num)
print(lotto)