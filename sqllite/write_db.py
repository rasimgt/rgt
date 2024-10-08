import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('create table if not exists music(track, time, rating)')
data = [('в лесу родилась елочка', 10.40, 4.5), ('белые розы', 3.40, 5.5)]
cursor.executemany('insert into music values(?,?,?)', data)
conn.commit()
conn.close()