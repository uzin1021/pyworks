# list 자료형

f = open("c:/pyfile/2021kbo.txt", "w")
team = ['기아', '삼성', '한화', 'LG', '두산', "kT", "SSG", "롯데"]
'''
for i in team:
    f.write(i+" ")
f.close()
'''
# range()함수
n = len(team)
for i in range(n):
    f.write(team[i] + " ")
f.close()

f = open("c:/pyfile/2021kbo.txt", "r")
data = f.read()
print(data)
f.close()