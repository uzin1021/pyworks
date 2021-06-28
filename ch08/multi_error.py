try:
    a = [1,2]
    print(a[2]) #첫번째 에러

    4/0 #두번째 에러

except IndexError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)