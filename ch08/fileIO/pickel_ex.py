import pickle
# 객체의 형태를 그대로 저장하고 불러오는 모듈
# 바이너리 모드 사용
with open('datas.txt','wb') as f:
    li = ['강아지','고양이','닭']
    dic = {1:'감자', 2:'딸기', 3:'키위'}
    pickle.dump(li, f)
    pickle.dump(dic, f)


with open('datas.txt','rb') as f:
    li = pickle.load(f)
    dic = pickle.load(f)
    print(li)
    print(dic)