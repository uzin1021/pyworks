
def vartest(a):
    a = a + 1 # a : 전역변수
    return a

a = 1 # a : 지역변수 
print(a)
print(vartest(a))

