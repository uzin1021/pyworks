# 멤버 매개변수가 있는 상속
from person import Person
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

'''
class Employee(Person):
    def __init__(self, name, age, empid):
        super().__init__(name, age) # 부모멤버는 super()를 사용
        self.empid = empid

    def getname(self):
        return self.name
    def getage(self):
        return self.age  #캡슐화(정보 은닉) - get() 매서드 사용
    def getempid(self):
        return  self.empid

e1 = Employee("북한산", 20, 300)
print(e1.name,e1.age,e1.empid)
print("이름 : ", e1.getname())
print("나이 : ", e1.getage())
print("ㅇㅇ : ", e1.getempid())
e2 = Employee("이산" ,23, 130)
print(e2.name,e2.age,e2.empid)