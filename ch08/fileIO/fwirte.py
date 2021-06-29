# 파일 열기(open()) -> 파일 쓰기(write()) -> 파일 닫기(close())

f = open("C:/pyfile/hello.txt", "w")
f.write("Hello~ p y t h o n!\n")
# f.write(1000) 오류-숫자는 입력불가 포맷형식 사용
f.write("%d\n" % 100) # 방법1
f.write("%.1f\n" %4.5)
num = "%d\n" % 12345
f.write(num) # 방법2 : 변수 사용
f.write("안녕 파이썬~!")

f.close()