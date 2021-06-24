# 학생 클래스 생성과 사용

class Student:
    def __init__(self, sid, name):
        self.sid = sid #학번
        self.name = name
    def showinfo(self): #정보 출력 메서드
        print(self.sid , self.name)

if __name__ == "__main__": #student_test만 출력되게함.
    s1 = Student(1001, "박대양")
    s1.showinfo()
    #print(s1.sid , s1.name)
    s2 = Student(1002, "mmm")
    s2.showinfo()