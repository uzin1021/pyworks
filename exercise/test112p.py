# 1번

a = 80
b = 75
c = 55

sum = a+b+c
avg = sum/3

print("평균 점수 : ", avg ,"점")
# print("평균 점수 : %d점 " , % avg) ??

# 2번

print( 13 % 2 ) 
print( 13 % 2 == 0 )

n = 13
if n % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")

# 3번~4번 (인덱싱,슬라이싱)

pin = "881120-1068234"
yyyymmdd = pin[0:6]
print(yyyymmdd)
num = pin[7:14]
print(num)
gen = pin[7]
# print(gen)
if gen == "1":
    print("남자입니다")
else:
    print("여자입니다")
