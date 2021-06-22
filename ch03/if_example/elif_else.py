#조건문
#놀이 공원 입장료 계산

age = int(input("나이 입력: "))
charge = 0 # 없어도 결과값에 영향 x, 전역변수

if age < 8:
    print("취학 전 아동입니다")
    charge = 1000
    #print("입장료는 %d원 입니다. " %charge) 중복(공통부분) 바깥으로 빼기
elif age < 14: # age <14앞에 age >= 8 and 생략  
    print("초등학생 입니다.")
    charge = 2000
elif age >= 14 and age < 20: #마찬가지로 age >= 14 and 생략 가능
    print("중,고등학생 입니다.")
    charge = 3000
else:
    print("성인 입니다.")
    charge = 4000

print("입장료는 %d원 입니다. " %charge) 
