from connect import *

def does_title_exist(film_title):
    dbCursor.execute("SELECT * FROM tblFilms WHERE title = ?", (film_title,))
    result = dbCursor.fetchone()
    return result is not None

def does_record_exist(record, column_name):
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE {column_name} = ?", (record,))
    result = dbCursor.fetchall()
    return len(result) > 0
 
def should_continue():
    user_input = input("Do you want to continue searching through the films (Y/N): ").lower()
    if user_input != "y":
        print("Exiting submenu option.")
        return True

def search_film():
    while True: 
        film_title = input("Enter film title to search for: ")
        if does_title_exist(film_title):
            dbCursor.execute("SELECT * FROM tblFilms WHERE title == ?",(film_title,))
            film_record = dbCursor.fetchone()
            print(film_record)
        else:
            print(f"No records for the title '{film_title}' exist.")
        if should_continue():
            return
        print("----------------------------")

def search_by_genre():
     while True: 
        film_genre = input("Enter genre to search: ").title()
        if does_record_exist(film_genre, 'genre'):
            dbCursor.execute("SELECT * FROM tblFilms WHERE genre == ?",(film_genre,))
            film_record = dbCursor.fetchall()
            print(film_record)
            print("")
            if should_continue():
                return
            print("----------------------------")
        else:
            print(f"No records for the genre '{film_genre}' exist.")
            if should_continue():
                return
            print("----------------------------")

def search_by_year():
     while True: 
        try:
            film_year = int(input("Enter year to search e.g. 2001: "))
            if does_record_exist(film_year, 'yearReleased'):
                dbCursor.execute("SELECT * FROM tblFilms WHERE yearReleased == ?",(film_year,))
                film_record = dbCursor.fetchall()
                print(film_record)
                print("")
                if should_continue():
                    return
                print("----------------------------")
            else:
                print(f"No records for the year '{film_year}' exist.")
                if should_continue():
                    return
                print("----------------------------")
        except ValueError:
            print("Invalid datatype.")
            if should_continue():
                return
            print("----------------------------")

def search_by_rating():
     while True: 
        film_rating = input("Enter rating to search e.g. pg: ").upper()
        if does_record_exist(film_rating, 'rating'):
            dbCursor.execute("SELECT * FROM tblFilms WHERE rating == ?",(film_rating,))
            film_record = dbCursor.fetchall()
            print(film_record)
            print("")
            if should_continue():
                return
        else:
            print(f"No records for the rating '{film_rating}' exist.")
            if should_continue():
                return
            print("----------------------------")

if __name__ == "__main__":
    search_film()
    search_by_genre()
    search_by_year()
    search_by_rating()