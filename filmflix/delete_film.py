from connect import *

def check_id_exists(film_ID):
    dbCursor.execute("SELECT filmID FROM tblFilms WHERE filmID = ?", (film_ID,))
    result = dbCursor.fetchone()
    return result is not None

def should_continue():
    user_input = input("Do you want to continue deleting films (Y/N): ").lower()
    if user_input != "y":
        print("Exiting the delete films menu.")
        return True


def delete_data():
    while True:
        try:
            idField = int(input("Enter the integer filmID of the record to be deleted: "))
            if check_id_exists(idField):
                dbCursor.execute("DELETE FROM tblFilms WHERE filmID == ?", (idField,))
                dbCon.commit()
                print(f"Record {idField} successfully deleted from tblFilms.")
            else:
                print(f"Film ID '{idField}' does not exist in the table.")
            if should_continue():
                break
        except ValueError:
            print("Invalid datatype, please enter a valid integer.")
            if should_continue():
                break

if __name__ == "__main__":
    delete_data()