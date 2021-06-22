# 함수의 정의와 사용

# return 이없고 매개변수가 없는 함수

def say_hello():
    print("Hi~")

# return 이 없고  매개변수가 있는 함수

def say_hello2(name):
    print("{}님 반갑습니다.".format(name))
    print(name,"님 반갑습니다.")


say_hello()
say_hello()

say_hello2('uzin')

