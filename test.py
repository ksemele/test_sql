import csv
import sqlite3


con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS posts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rubrics TEXT,
            text TEXT,
            created_date TEXT 
            );""")
con.commit()

with open('./posts.csv', 'r') as f:
    reader = csv.reader(f)
    columns = next(reader) 
    query = 'INSERT INTO posts(text, created_date, rubrics) VALUES (?, ?, ?)'
    for data in reader:
        cur.execute(query, (data[0], data[1], data[2]))
    con.commit()
