import sqlite3

conn = sqlite3.connect(r"C:\\Users\\cbagwan\Downloads\database.db")
cur=conn.cursor()
cur.execute("SELECT * FROM countries WHERE area>=2000000")
rows = cur.fetchall()
conn.close()

for i in rows:
    print(i[1])