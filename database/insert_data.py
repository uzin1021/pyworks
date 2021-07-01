# 자료를 삽입하는 코드

from libs.db.dbconn import getconn

def insert_data():
    conn = getconn()
    cur = conn.cursor()

    # 자료를 추가하는 - SQL
    cur.execute("insert into member values ('최영',50)")
    cur.execute("insert into member values ('이황',50)")
    cur.execute("insert into member values ('이순신', 60)") # 이 줄은 지우고 다시 작성,
                                                           # 똑같이 입력할시 중복데이터 생성됨

    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_data()