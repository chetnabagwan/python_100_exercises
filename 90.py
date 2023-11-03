import sqlite3
import pandas

conn = sqlite3.connect(r"C:\\Users\\cbagwan\Downloads\database.db")
cur=conn.cursor()
cur.execute("SELECT * FROM countries WHERE area>=2000000")
rows = cur.fetchall()
conn.close()

df = pandas.DataFrame.from_records(rows)
df.columns = ["id","Country", "Area","Population"]
df.to_csv("Countries_big_area.csv",index=False)