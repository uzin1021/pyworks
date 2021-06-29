# 영어 타자 게임 만들기

f = open("words.txt", "a")
word = ["sky",'sea','candy','earth','tree','flower'
        ,'garlic','cat','dog','potato']
for i in word:
    f.write(i + " ")
f.close()