from connect import *

def retrieve_last_film_ID():
    dbCursor.execute("SELECT MAX(filmID) FROM tblFilms")
    available_ID = dbCursor.fetchone()[0]
    return available_ID

def capitalise_words(film_name):
    film_title = film_name.split(" ")
    capitalised_title = []
    for word in film_title:
        capitalised_title.append(word.title())
    return " ".join(capitalised_title)   

def should_continue():
    user_input = input("Do you want to continue adding films (Y/N): ").lower()
    if user_input != "y":
        print("Exiting the add films menu.")
        return True
    
def is_id_taken(film_id):
    dbCursor.execute("SELECT COUNT(*) FROM tblFilms WHERE filmID=?", (film_id,))
    count = dbCursor.fetchone()[0]
    return count > 0

def add_record():
    while True:
        try:
            while True:
                film_ID = int(input(f"Enter ID for film record to be added (Next available ID is {retrieve_last_film_ID()+1}): "))
                if is_id_taken(film_ID):
                    print(f"Film ID {film_ID} is already taken.")
                    if should_continue():
                        return
                    print("----------------------------")
                    continue
                film_title = input("Enter film title: ")
                if film_title.strip():
                    film_title = capitalise_words(film_title)
                    break
                else:
                    print("Film title cannot be empty.")
                    if should_continue():
                        return
                    print("----------------------------")
                    continue
            film_year_released = int(input("Enter film year released e.g. 2001: "))
            film_rating = input("Enter film rating: ").upper()
            film_duration = int(input("Enter film duration in minutes: "))
            film_genre = input("Enter film genre: ").title()
            
            dbCursor.execute("INSERT INTO tblFilms(filmID,title,yearReleased,rating,duration,genre) VALUES (?,?,?,?,?,?)", (film_ID,film_title,film_year_released,film_rating,film_duration,film_genre))
            dbCon.commit()
            print(f"Successfully added {film_title} to tblFilms")

            if should_continue():
                return
            print("----------------------------")
        except ValueError:    
            print("Invalid input. Please make sure ID, year and duration are integers.")
            if should_continue():
                return
            print("----------------------------")

if __name__ == "__main__":
    add_record()