#리스트의 연산

score = [80,50,70,65,40,90]
sum = 0 # 변수 선언
count = len(score)
avg = 0

#합계
for i in score:
    sum += i
    print("i = %d, sum=%d" % (i, sum))

#평균
avg = sum / count

    
#print("개수 : %d개" % count)
print("개수 : {}개" .format(count))
print("합계 : %d점" % sum)
print("평균 : %.1f점" % avg) 
