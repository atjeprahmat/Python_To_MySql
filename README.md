# Cara Menghubungkan Python ke MySQL menggunakan pymysql

Cara Menghubungkan Python ke MySQL menggunakan pymysql

Perlu menghubungkan Python ke MySQL?

Jika demikian, saya akan menunjukkan kepada Anda cara membuat koneksi seperti itu dari awal!

Tetapi sebelum kita mulai, ini adalah sintaksis generik yang dapat Anda gunakan untuk menghubungkan Python ke MySQL:

    import pymysql
    db = pymysql.connect(host='localhost', user='root', password='', database='TestDB_Python')
    cur = db.cursor()
    cur.execute('SELECT * FROM person')
    for row in cur.fetchall():
    print(row)
    db.close()
  

Membuat Database:
CREATE DATABASE TestDB_Python;

    USE TestDB_Python;

    CREATE TABLE Person (Name VARCHAR(100), Age INT, City VARCHAR(100));

    SELECT * FROM Person;


    INSERT INTO Person VALUES('Jade','20','London'),
    ('Marry','119','NY'),
    ('Martin','25','London'),
    ('Rob','35','Geneva'),
    ('Maria','42','Paris'),
    ('Jon','28','Toronto')
