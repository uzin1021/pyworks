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

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()
def message(m1,m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("",20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("",15))
    t.home()

def play():
    global score
    global playing

    t.forward(10)

    #적거북이의 속도는 점수가 올라가면 1씩 증가함.
    if random.randint(1, 5) == 3:  # 3을 뽑을 확률이 적음 , 20퍼의 확률로 따라옴
        ang = te.towards(t.pos())
        te.setheading(ang)
    speed = score + 4
    if speed >15:
        spee = 15
    te.forward(speed)
    #주인공이 먹이를 먹으면 점수가 1 올라감.
    if t.distance(tf) < 12:
        score += 1
        t.write(score)
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        tf.goto(x,y)
    #주인공 거북이가 적에게 잡히면 게임 종료
    if t.distance(te) <12:
        text = "Score : " +str(score)
        message("Game over: " , text)
        playing = False
        score = 0

    if playing:
        t.ontimer(play, 100)

# 점수 변수와 플레이 스위치(bool) 변수 선언
score = 0
playing = False


#main 메인영역
t.shape("turtle")
t.bgcolor("lightyellow")
t.speed(0)
t.up()
t.setup(500,500) #너비,높이
t.title("달려라 거북이")
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
t.onkeypress(start, "space")

t.listen()
message("Turtle Run", "[Space]")

t.mainloop()