class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("강하늘", 30)
p1 = Person("이산", 50)

print(p.name)
print(p.age)

print(p.name, p.age)
print(p1.name, p1.age)