# 리스트의 최대값, 최소값, 정렬

score = [70,80,50,50,90,20]

max = score[0]
len(score)
n = len(score)

for i in range(1, n):
    if max < score[i]:
        max = score[i]
    
print(max)

#오름차순 정렬

for i in range(0, n):
    for j in range(0, n-1):
        if score[j] > score[j+1]:
            score[j], score[j+1] = score[j+1], score[j]
        '''
            # 1행
            70 50 60 80 20 90
            2행
            50 60 70 20 80 90
            3행
            50 60 20 70 80 90
            4행
            50 20 60 70 80 90
            5행
            20 50 60 70 80 90
        '''    
'''
for i in score:
    print(i, end = " ")
'''
