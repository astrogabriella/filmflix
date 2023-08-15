import sqlite3 as sql

dbCon = sql.connect("filmflix/database_and_txt_files/filmflix.db")
#establishes a connection to an SQLite database 
dbCursor = dbCon.cursor()
# A cursor acts as a pointer that you can use to execute SQL queries and fetch results from the database.