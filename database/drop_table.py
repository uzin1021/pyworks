# delect는 자료만 지움
# table 자체 지우기
from  libs.db.dbconn import getconn

def drop_table():
    conn = getconn() # 네트워크(db) 연결 객체
    cur = conn.cursor()

    # 테이블 삭제 - SQL DDL(데이터 정의어)
    sql = "drop table member"
    cur.execute(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    drop_table()