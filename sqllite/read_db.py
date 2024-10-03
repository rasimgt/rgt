import sqlite3
conn = sqlite3.connect('example')
cursor = conn.cursor()
cursor.execute('select * from product')
items = cursor.fetchall()

print(items[0][1])

conn.close()
