# member 테이블 전체 검색

from libs.db.dbconn import getconn

def select_data():
    conn = getconn()
    cur = conn.cursor()
    # 자료 조희 - SQL DML (select)
    sql = "select * from member" # * : name,age포함
    cur.execute(sql) # 데이터 불러오기
    print("데이터 전체 조회")
    rs = cur.fetchall() # 꺼내온 자료 객체
    for i in rs:
        print(i)

    conn.close()

if __name__ == "__main__":
    select_data()