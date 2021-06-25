# Person 클래스 생성과 사용

class Person:
    def __init__(self): # init - 초기자(생성자) 함수
        self.__name = "강하늘"
        self.__age = 30

    def getname(self): #멤버 변수에 직접 접근하지 않도록 get()을 사용
        return self.__name

    def getage(self):
        return self.__age


p = Person() # 객체 변수 - 인스턴스(instance)
#print(p.name)
#print(p.age)

print(p.getname())
print(p.getage())