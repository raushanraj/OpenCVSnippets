import sqlite3 as lite
import sys

con = lite.connect('test.db')
cur = con.cursor()    
#cur.execute("CREATE TABLE Global(Path Text)")

def insert(path):
    with con:
         cur.execute("INSERT INTO Global(Path) VALUES (?)", (path,) )

def getpath():
    cur = con.cursor()    
    cur.execute("SELECT * FROM Global")
    rows = cur.fetchall()
    j=""
    for row in rows:
        j=row
    print j

insert("hello")
getpath()


