# 이차원 리스트의 생성과 출력

li = [
        [10,20],
        [30,40],
        [50,60]
    ]

print('li[0][0] =',li[0][0])
print('li[0][1] =',li[0][1])
print('li[1][0] =',li[1][0])
print('li[1][1] =',li[1][1])
print('li[2][0] =',li[2][0])
print('li[2][1] =',li[2][1])

print("리스트의 크기(행) =", len(li))
'''
for x,y in li:
    print(x,y) #파이썬 예시
'''

for i in range(len(li)):
    # print(len(li[i]))
    for j in range(len(li[i])):
        print(li[i][j], end = " ")
    print()
#일반적인 코드 예시 
