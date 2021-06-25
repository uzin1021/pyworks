#랜덤하게 거북이가 걸어가기
import turtle as t
import random as r

t.shape("circle")
t.speed(10)
t.pensize(2)
t.bgcolor("pink")
t.setup(500,500) #작업영역 크기

for x in range(500): # 거북이가 500번 움직임
    angle = r.randint(1, 360)
    t.setheading(angle) # 거북이의 방향
    t.forward(10)
t.mainloop()