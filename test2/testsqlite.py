import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()

sql = ""

c.execute(sql)
conn.commit()
conn.close()
print("open database")