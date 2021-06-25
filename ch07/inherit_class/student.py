from person import Person
# Student 클래스 - 학번(stuid)

class Student(Person):
    def __init__(self, name, age, stuid):
        self.stuid = stuid
        super().__init__(name, age)

    def showinfo(self):
        print(self.name, self.age, self.stuid)

s1 = Student("이강", 19, 102)
s1.showinfo()
s2 = Student("이밤", 18, 101)
s2.showinfo()