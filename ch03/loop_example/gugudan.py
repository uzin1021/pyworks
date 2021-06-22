#구구단 4단 출력하기
'''
for i in range(1, 10):
    print("4 x %d = %d" % (i, 4*i))
'''
#구구단 출력하기
dan = int(input("단 :"))
for i in range(1, 10):
    print("%d x %d = %d" % (dan, i, i*dan)) #%d만큼 항의 개수 추가
    
