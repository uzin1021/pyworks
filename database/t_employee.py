from libs.db.dbconn import getconn

def select_emp():
    conn = getconn()
    cur = conn.cursor()
    # sql - select
    sql = "select * from employee"
    cur.execute(sql)
    rs = cur.fetchall() #데이터 목록 리스트형 반환
    for i in rs:
        print(i)


def select_one():
    conn = getconn()
    cur = conn.cursor()
    sql = "select * from employee where emp_id='e102'"
    cur.execute(sql)
    rs = cur.fetchall()
    print(rs)
    conn.close()

def insert_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "insert into employee(emp_id, name, age, salary) values (?,?,?,?)"
    cur.execute(sql, ('e104','손흥민',35, 15000))
    conn.commit()
    conn.close()

def update_emp():
    conn = getconn()
    cur = conn.cursor()
    # 박인비의 급여를 20000 -> 25000으로 변경
    sql = "update employee set salary = 25000 where emp_id ='e102'"
    cur.execute(sql)
    conn.commit()
    conn.close()

def delect_data():
    conn = getconn()
    cur = conn.cursor()
    sql = " delete from employee where emp_id =?"
    cur.execute(sql,('e102', ))
    conn.commit()
    conn.close()

#update_emp()
#insert_emp()
#select_one()
delect_data()
select_emp()