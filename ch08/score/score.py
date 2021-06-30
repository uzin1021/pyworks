# 성적 입력 프로그램 만들기
#
with open('scorelist.txt', 'a') as f:
    x= ' '
    while True:
        try:
            x = input("성적을 저장할까요?(y/n)")
            if x == "y":
                with open('scorelist.txt','a') as f:
                    name = input("이름 입력 : ")
                    kor = int(input("국어 점수 : "))
                    math= int(input("수학 점수 : "))
                    avg = (kor + math) /2

                    f.write(name + " ")
                    f.write(str(kor) + " ")
                    f.write(str(math) + " ")
                    f.write(str(avg) + "\n")

                    x = input("성적을 저장할까요?(y/n)")
                    if x == "n" or x == "N":
                        break
        except ValueError:
            print("잘못된 입력입니다. 다시 입력해주세요:")
