# 여러개의 원 만들기

import turtle as t

t.speed(0)
t.pensize(2)
t.bgcolor("black")
t.color("pink")

n = 40
for x in range(n):
    t.circle(80)
    t.left(360/n)
