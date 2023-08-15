import film_reports, retrieve_all_films

def display_report_menu():
    with open("filmflix/database_and_txt_files/report_menu.txt") as report_menu_file:
        report_menu_content = report_menu_file.read()
    return report_menu_content

def get_user_choice():
    valid_choices = ["1", "2", "3", "4", "5", "6"]
    menu_content = display_report_menu()

    while True:
        print(menu_content)
        user_input = input("Enter an option from the menu above: ")
        if user_input not in valid_choices:
            print(f"'{user_input}' is not a valid choice. Please try again.")
        else:
            return user_input

def handle_user_choice():
    while True:
        user_choice = get_user_choice()

        if user_choice == "1":
            retrieve_all_films.read_films()
        elif user_choice == "2":
            film_reports.search_film()
        elif user_choice == "3":
            film_reports.search_by_genre()
        elif user_choice == "4":
            film_reports.search_by_year()
        elif user_choice == "5":
            film_reports.search_by_rating()
        else:
            print("Exiting the reports menu")
            print("----------------------------")
            break


if __name__ == "__main__":
    handle_user_choice()
    # print(f"User selected: {user_selection}")
