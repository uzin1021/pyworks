# try ~ except ~ finally

def divide(x , y):
    try:
        div = x / y
    except ZeroDivisionError:
        print("0으로 나눌수 없습니다.")
    else:
        print(div)
    finally:
        print("여기는 꼭 수행하는 구간입니다.")

divide(3,0)

divide(3,50)