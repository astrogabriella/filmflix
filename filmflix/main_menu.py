import retrieve_all_films, add_film, amend_film, delete_film, report_menu

def display_main_menu():
    with open("filmflix/database_and_txt_files/main_menu.txt") as main_menu_file:
        main_menu_content = main_menu_file.read()
        return main_menu_content
    
def get_user_selection():
    valid_choices = ["1", "2", "3", "4", "5", "6"]
    menu_content = display_main_menu()

    while True:
        print(menu_content)
        user_input = input("Enter an option from the main menu: ")
        if user_input not in valid_choices:
            print(f"'{user_input}' is not a valid choice. Please try again.")
        else:
            return user_input
   
def handle_user_selection():
    while True:
        user_choice = get_user_selection()
        if user_choice == "1":
            retrieve_all_films.read_films()    
        elif user_choice == "2":
            add_film.add_record()
        elif user_choice == "3":
            amend_film.amend_data()
        elif user_choice == "4":
            delete_film.delete_data()
        elif user_choice == "5":
            report_menu.handle_user_choice()
        else:
            print("Exiting main menu")
            break

if __name__ == "__main__":
    handle_user_selection() 