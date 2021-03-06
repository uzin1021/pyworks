
with open("scorelist.txt","r") as f:
    d2 = [] # 이차원 리스트 준비
    for i in range(3):
        d2.append(f.readline().split())
    print(d2)
    """
    [
        ['홍길동', '80', '70'],
        ['이순신', '70', '60'], 
        ['황진이', '40', '50']
     ]
    """
    for i in range(3):
        d2[i][1] = int(d2[i][1]) # 국어(숫자형 변경: 문자 -> 숫자) - 2열
        d2[i][2] = int(d2[i][2]) # 수학(숫자형 변경) - 3열
        d2[i].append(d2[i][1] + d2[i][2]) # 총점 - 4열
        d2[i].append(d2[i][3]/2) # 평균 - 5열
    # print(d2)
    print("   ************* 성적표 ***********   ")
    print(" ====================================")
    print("    이름   국어   수학   총점   평균")
    print(" ====================================")
    for i in range(3):
        print("    {}   {}   {}   {}   {}  ".format(d2[i][0],d2[i][1],d2[i][2],d2[i][3],d2[i][4]))
    print(" ====================================")
    print("    ********과목별 평균***********   ")
    kor_sum = 0
    math_sum = 0
    for i in range(3):
        kor_sum += d2[i][1] # 국어 총점
        math_sum += d2[i][2] # 수학 총점
    print(" 국어  :  %.2f점  , 수학  :  %.1f점" % (kor_sum/3, math_sum/3))