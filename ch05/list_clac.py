# 리스트를 매개변수로 전달하기
# 점수의 평균 계산하기

def avg(a):
    sum = 0
    c = len(a)
    for i in a:
        sum += i
    return int(sum/len(a))


avg = avg([50,70,90,80,60])
print("평균 점수: ",avg)
