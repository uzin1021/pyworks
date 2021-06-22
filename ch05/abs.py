# abs() 직접 정의
# 절대값 알고리즘 1
'''
def abs_sign(x):
    if x < 0: x * x
    return -x
'''
# 절대값 알고리즘 2
def abs_sign(x):
    if x < 0:
        return -x
    else:
        return x
# 절대값 알고리즘 3
def abs_square(x):
    y = x * x
    return math.sqrt(y)

#n1 = abs_square(x)
abs_sign(-3)
print(abs_sign(-3))
#print(n1)

n2 = abs_square(-4)
print(n2)
