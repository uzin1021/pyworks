#전역변수(정적변수) - 누적 공유되는 변수
#global 키워드 사용

def one_up():
    global x
    x = x+1
    return x
x = 0 # x가 지역변수 안에서 선언하지않을때 출력 하지않음 이때 global(전역변수)를 써준다.
print(one_up())


def one():
    #global x
    y = x + 1
    return y 
x = 0 #지역변수가 y로 다를때는 바깥에서 선언해도 출력 가능함. 
print(one())
