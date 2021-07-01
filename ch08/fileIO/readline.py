
with open('c:/pyfile/2021kbo.txt', 'w') as f:
    team = ['삼성','LG','롯데','기아']
    for i in team:
        f.write(i + "\n")

with open('c:/pyfile/2021kbo.txt', 'r') as f:
    # data = f.readlines() # readlines : 파일읽기를 하면 리스트로 반환 , readline : 줄 단위로 그대로 읽어와 붙여서 출력한다.
    # print(data)
    '''
    # 이차원 리스트 만들기
    d2 = []
    for i in range(4):
        data = f.readline().split()
        print(data)
    '''
    d2 = [] # 새리스트 준비
    for i in range(4):
        d2.append(f.readline().split())
    print(d2)

f.close()
