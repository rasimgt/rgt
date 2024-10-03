import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('select * from product')
items = cursor.fetchall()
print(items)

#cursor.execute('select * from sqlite_master where type="table"')
#tabl = cursor.fetchall()
#print(tabl)
#for tab in tabl:
#    print(tab)
conn.close()
