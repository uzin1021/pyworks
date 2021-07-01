# 1차원 구조 리스트
d1 = [1,2,3]

print(d1[1])
d1.append(10)
print(d1)

# 2차원 구조 리스트
d2 = [[11,22],[33,44],[55,66]] # 3행 2열
print(d2[0][0])
print(d2[0][1])
d2.append([77,88]) # 리스트로 값추가할경우 []사용
print(d2)

for i in d2:
    print([i][0])

# d2 리스트 합계 , 평균
d2.append([d2[0][0] + d2[1][0] + d2[2][0] + d2[3][0]]) # []주의
print(d2)
avg = (d2[0][0] + d2[1][0] + d2[2][0] + d2[3][0]) / 4
d2.append([avg])
print(d2)