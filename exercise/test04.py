# 1
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

print(is_odd(6))

# 2 가변 매개 변수
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result /len(args)

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))

# 3
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1)+int(input2)
print("두 수의 합은 %d 입니다" % total)

# 4
print("you""need""python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python"]))

# 5
