# 도형 그리기

import turtle as t

t.shape("turtle")

# 사각형 그리기
n = 4
t.color("pink")
t.pensize(3)
for i in range(n):
    t.forward(100)
    t.right(360/n)

# 삼각형 그리기
t.color("red")
t.pensize(2)
n = 3
for i in range(n):
    t.forward(100)
    t.left(360/n)

# 원
n = 40
for i in range(n):
    t.color("yellow")
    t.left(360/n)
    t.circle(60)
