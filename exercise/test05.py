# 1번
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value #print(c.add(10)) none 없앨때

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return self.value
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
        return self.value
# 부모 클래스의 인스턴스
c = Calculator()
#c.add(10)
#print(c.value)
# print(c.add(10))
cal = UpgradeCalculator()
cal.add(10)
cal.minus(6)
print(cal.value)

cal2 = MaxLimitCalculator()
cal2.add(40)
cal2.add(90)
print(cal2.value)

# 2번
# 4번
li = [1, -2,3,5,-8,-3]
print(list(filter(lambda x : x >= 0, li)))

def one(x):
    a1=[]
    for i in x:
        if i >= 0:
            a1.append(i)
        return a1

li = [1, -2,3,5,-8,-3]
li2 = one(li)
print(li2)

# 6
def times(a):
    a2 = []
    for i in a:
        a2.append(i*3)
    return a2

li = [1,2,3,4]
li2 = times(li)
print(li2)
print(list(map(lambda x : x*3, li)))
