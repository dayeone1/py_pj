import pymysql

# 데이터베이스 연결
conn = pymysql.connect(
    host='127.0.0.1:3306',
    user='root',
    password='1234',
    db='test',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    curs = conn.cursor()
    
    # SQL 쿼리 실행
    sql = "SELECT * FROM test"
    curs.execute(sql)
    
    # 결과 가져오기
    rows = curs.fetchall()
    for row in rows:
        print(row)

finally:
    # 연결 종료
    conn.close()
