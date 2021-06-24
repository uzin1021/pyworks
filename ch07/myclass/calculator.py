# 계산기 클래스 만들기
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    def sub(self):
        return self.x - self.y
    def mul(self):
        return self.x * self.y
    def div(self):
        return self.x / self.y

# print(Calculator(3,4).add())

if __name__ == "__main__": #clac_test 만 출력되게함.
    c = Calculator(5, 9)
    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())