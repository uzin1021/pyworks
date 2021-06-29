# kbo 구단을 1개씩 랜덤 추출하기
import random
try:
    f = open("c:/pyfile/2021kbo.txt" ,"r")
    data = f.read().split() # split - 리스트 배열
    team = random.choice(data)

    print(data)
    print(data[2]) # data에서 하나씩 추출
    print(team) # 랜덤으로 추출

    f.close()
except FileNotFoundError as e:
    print(e)