# 인치 클래스 만들기
# inch -> mm로 바꾸는 클래스(1inch - 2.54cm)

class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def convert(self, value): # self.factor : 25
        return self.factor * value

if __name__=="__main__":
    c1 = ScaleConverter("inches","mm", 25)
    print("converting 2 inches")
    print(str(c1.convert(2))+c1.units_to) #str이 형변환에서 용량이 크므로 int 보다 str로 변형해준다.