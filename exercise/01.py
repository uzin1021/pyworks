
class Calcultor:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calcultor):
    def minus(self, val):
        self.value = self.value -val # self.value -= val

class MaxLimitCalculator(Calcultor):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

c = Calcultor()
cal = UpgradeCalculator()
cal.add(30)
cal.minus(10)
print(cal.value)

c2 = MaxLimitCalculator()
c2.add(40)
c2.add(80)
print(c2.value)




a = [30,40,50,60,70]
sum = 0
for i in a:
    sum += i
avg = sum/len(a)
print("%d점 입니다." %avg)
print("{}점 입니다".format(avg))