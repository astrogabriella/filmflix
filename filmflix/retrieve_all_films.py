from connect import *

def read_films():
    dbCursor.execute("SELECT * FROM tblFilms")
    filmRecords = dbCursor.fetchall()

    for filmRecord in filmRecords:
        print(filmRecord)
    
if __name__ == "__main__":
    read_films()                