# 특정한 회원 검색하기
from libs.db.dbconn import getconn

def selcet_one():
    conn = getconn()
    cur = conn.cursor()

    # 1명 검색 SQL
    sql = "select * from member where mem_num = 104" # primary key로 거의 고정
    cur.execute(sql)
    print("이황 검색")
    # rs = cur.fetchmany(num)
    rs = cur.fetchone()
    '''
    for i in rs:
        print(i)
    '''
    print(rs)
    conn.close()

if __name__ == "__main__":
    selcet_one()