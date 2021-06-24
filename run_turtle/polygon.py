# 다른곳에 도형 그리기
import turtle as t

t.shape('circle')

def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)

def polygon2(n ,d):
    for x in range(n):
        t.forward(d)
        t.left(360/n)
polygon(3)
polygon(5)


t.up() # 선 올리기
t.forward(100) 
# t.back(100) #100px 뒤로 이동
t.down() # 선 내리

polygon2(4, 90)
polygon2(5,120)

