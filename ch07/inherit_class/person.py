# Person 클래스 - 멤버 변수(name, age)
# Employee 클래스는 Person을 상속 받음

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
        pass

if __name__ == "__main__":
    p1 = Person("한강" , 25)
    print(p1.name,p1.age)

    e1 = Person("이이", 32)
    print(e1.name,e1.age)

    e2 = Person("이황", 33)
    print(e2.name,e2.age)