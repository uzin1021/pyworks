import turtle as t
import random

def turn_right(): #오른쪽 화살표 키
    t.setheading(0)

def turn_up(): #위쪽 화살표키
    t.setheading(90)

def turn_left(): #왼쪽
    t.setheading(180)

def turn_down(): #아래쪽
    t.setheading(270)


def play():
    t.forward(10)
    te.forward(9)
    # 적거북이가 주인공거북이 쫓아옴
    ang = te.towards(t.pos())
    te.setheading(ang)
    # 주인공 거북이가 먹이에 닿으면 먹이 랜덤하게 이동
    if t.distance(tf) <12:
        x = random.randint(-230 , 230)
        y = random.randint(-230, 230)
        tf.goto(x,y)

    if t.distance(te) >= 12: #12보다 작으면 잡혀서 게임 종료
        t.ontimer(play, 100) # 0.1초 간격으로 작동

#main 메인영역
t.shape("turtle")
t.bgcolor("lightyellow")
t.speed(0)
t.up()
t.color("darkgreen") #주인공 거북이

#적 거북이
te = t.Turtle() #t.Turtle() 클래스에서 te 인스턴스 생성

te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

#먹이
tf = t.Turtle()

tf.shape("circle")
tf.color("brown")
tf.speed(0)
tf.up()
tf.goto(0, -200)

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left,  "Left")
t.onkeypress(turn_down, "Down")
# t.onkeypress(clear, "Escape")

t.listen()
play()

t.mainloop()