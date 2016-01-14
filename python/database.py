import sqlite3 as lite
import sys

con = lite.connect('test.db')
cur = con.cursor()    
#cur.execute("CREATE TABLE Global(Path Text)")
#cur.execute("CREATE TABLE Global2(id INT,Path Text)")
#cur.execute("DELETE FROM Global2")

def insert(path):
    with con:
        cur.execute("UPDATE Global2 SET Path=? WHERE id=1",(path,))
        
        #cur.execute("INSERT INTO Global(Path) VALUES (?)", (path,) )
        #globas=(1,path)
        #cur.execute("INSERT INTO Global2 VALUES (?,?)",globas )
        
def getpath():
    cur = con.cursor()    
    #cur.execute("SELECT * FROM Global")
    cur.execute("SELECT * FROM Global2")
    rows = cur.fetchall()
    j=""
    for row in rows:
        #print row
        j=row
    return j[1]

#insert("rudepath")
print getpath()
