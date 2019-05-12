import pymysql

db = pymysql.connect(host='localhost', user='root', password='', database='TestDB_Python')

cur = db.cursor()

cur.execute('SELECT * FROM person')

for row in cur.fetchall():
    print(row)

db.close()