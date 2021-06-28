#숫자를 추측해서 맞히는프로그램

import random

com = random.randint(1,30)
while True:
    try:
        guess = int(input("맞혀보세요(1~30): "))
        if guess > 30 or guess < 1:
            print("입력 숫자를 초과하였습니다.")
        elif com < guess:
            print("너무 커요")
        elif com > guess:
            print("너무 작아요")
        else:
            print("정답!")
            break
    except ValueError:
        print("숫자가 아닙니다. 다시 입력해주세요:")
