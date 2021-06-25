#장바구니 클래스 - 인스턴스 리스트

class Cart:
    def __init__(self, goods):
        self.li = []
        self.li.append(goods)

    def showinfo(self):
        print(self.li)


c = Cart("커피")
c.showinfo()
c1 = Cart("계란")
c1.showinfo()
c2 = Cart("우유")
c2.showinfo()