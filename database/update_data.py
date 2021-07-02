# 자료 수정(자료 내용 변경)하기

from libs.db.dbconn import getconn

def update_data():
    conn = getconn()
    cur = conn.cursor()
    sql = "update member set name='성춘향' mem_num = 105"
    # sql = "update member set age=55 where name= '최영'"
    cur.execute(sql)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    update_data()