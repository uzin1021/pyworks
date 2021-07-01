# 특정한 자료 삭제

from libs.db.dbconn import getconn

def delect_data():
    conn = getconn()
    cur = conn.cursor()
    sql = "delete from member where name = '최영'"
    cur.execute(sql)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    delect_data()