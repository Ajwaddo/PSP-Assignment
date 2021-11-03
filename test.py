import sqlite3
from sqlite3.dbapi2 import Cursor
connection=sqlite3.connect("user.db")

#to show which dat we choose
cursor=connection.cursor()

cursor.execute("update userdata")