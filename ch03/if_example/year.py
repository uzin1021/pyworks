#조건 : 4년마다 오며 100년 단위는 윤년이 아니나, 400년 단위로 윤년이다.

year = int(input("연도를 입력하세요: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("%d년은 윤년입니다." %year)    
else:
    print("%d년은 윤년이 아닙니다." %year)

# year % 100 != 0 or year % 400 == 0:
# year % 4 != 100) or (year % 4 == 0 and year % 4 == 400):

