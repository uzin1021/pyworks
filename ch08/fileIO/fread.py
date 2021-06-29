
try:
    f = open("c:/pyfile/hello.txt", "r")
    data = f.read()
    print(data)  # 파일 읽기 - 콘솔창에서 확인
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")  # try-except 사용 : 파일 입력 잘못했을때 메세지 출력
