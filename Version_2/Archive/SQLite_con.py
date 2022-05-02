import sqlite3

con = sqlite3.connect("C:\SQLite\EST_database.db")
cur = con.cursor()
statement = f"Select username from users where username='{username}' and password= '{password}'"
cur.execute(statement)
if not cur.fetchone():
    pass
else:
    pass