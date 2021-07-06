# 1

def gugudan(dan):
    lst = []
    for i in range(2,10):
        lst.append(("{} x {} = {}").format(dan,i,dan *i))

    return lst

dan2 = gugudan(2)
print(dan2)

# 2
'''
3과 5의 배수의 합
계산범위 : 1부터 10까지 자연수
결과 값 : 33
'''
