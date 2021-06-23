# 리스트의 최대값, 최소값, 정렬

score = [70,80,40,50,60,20]

max = score[0]
len(score)
n = len(score)

for i in range(1, n):
    if max < score[i]:
        max = score[i]
    
print(max)
