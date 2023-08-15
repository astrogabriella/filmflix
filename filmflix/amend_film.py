from connect import *

def check_id_exists(film_ID):
    dbCursor.execute("SELECT filmID FROM tblFilms WHERE filmID = ?", (film_ID,))
    result = dbCursor.fetchone()
    return result is not None

def capitalise_words(film_name):
    film_title = film_name.split(" ")
    capitalised_title = []
    for word in film_title:
        capitalised_title.append(word.title())
    return " ".join(capitalised_title)   


def should_continue():
    user_input = input("Do you want to continue amending films (Y/N): ").lower()
    if user_input != "y":
        print("Exiting the amend films menu.")
        return True

def amend_data():
    while True:
        try:
            while True:
                idField = int(input("Enter the filmID of the record to be updated: "))
                if check_id_exists(idField):
                    film_title = input("Enter the film title: ")
                    if film_title.strip():
                        film_title = capitalise_words(film_title)
                        break
                    else:
                        print("Title cannot be empty.")
                        if should_continue():
                            return
                        print("----------------------------")
                else:
                    print(f"Film ID '{idField}' does not exist in the table.")
                    if should_continue():
                            return
                    print("----------------------------")

            film_year_released = int(input("Enter film year released e.g. 2001: "))
            film_rating = input("Enter film rating: ").upper()
            film_duration = int(input("Enter film duration in minutes: "))
            film_genre = input("Enter film genre: ").title()

            film_title = "'" + film_title + "'"
            film_rating = "'" + film_rating + "'"
            film_genre = "'" + film_genre + "'"

            dbCursor.execute(f"UPDATE tblFilms SET title={film_title}, yearReleased={film_year_released},rating = {film_rating},duration = {film_duration}, genre={film_genre} WHERE filmID == {idField}")
            dbCon.commit()    
            print(f"Record {idField} successfully updated.")
            if should_continue():
                return
            print("----------------------------")

        except ValueError:
            print("Invalid input.")
            if should_continue():
                return
            print("----------------------------")

if __name__== "__main__":
    amend_data()