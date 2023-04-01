import pymysql

db = pymysql.connect('localhost', 'root', 'root', 'lianjia')
cursor = db.cursor()
sql = """CREATE TABLE spider (
         title VARCHAR(200),
         link VARCHAR(200),
         location VARCHAR(200),
         rent INT,
         apartment_layout VARCHAR(200),
         area FLOAT,
         orientation VARCHAR(200),
         publish_time VARCHAR(200),
         unit_price FLOAT,
         floor VARCHAR(200),
         longitude FLOAT,
         latitude FLOAT,
         created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"""

cursor.execute(sql)
db.commit()
db.close()