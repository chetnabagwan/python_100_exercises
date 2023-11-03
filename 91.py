import sqlite3
import pandas

data=pandas.read_csv(r"C:\\Users\\cbagwan\Downloads\\ten_more_countries.txt")

conn = sqlite3.connect(r"C:\\Users\\cbagwan\Downloads\database.db")
cur=conn.cursor()
for index,row in data.iterrows():
    print(row["Country"],row["Area"])
    cur.execute("INSERT INTO countries VALUES (NULL,?,?,NULL)",(row["Country"], row["Area"]))

conn.commit()
conn.close()

