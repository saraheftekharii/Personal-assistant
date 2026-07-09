import users
import note
import json


def account_menu():
    while True:

        choice = input(" 1.Login \n 2.Register \n 3.Exit\n")
        if choice == "1":
            user_name = users.login()
            if user_name:
                return user_name
                
        elif choice == "2":
            users.register()
        elif choice == "3":
            break
        else:
            print("Not valid!")
            continue


def note_menu(user_name):
    
    while True:
        choice = input(" 1.Add note \n 2.Show note \n 3.Delet note \n 4.Edit note \n 5.Exit\n")

        if choice == "1":
            note.add_notes(user_name)

        elif choice == "2":
            note.show_notes(user_name)

        elif choice == "3":
            note.delet_note(user_name)

        elif choice == "4":
            note.edit_notes(user_name)

        elif choice == "5":
            break

        else:
            print("Not valid!")
            continue


def main_menu():

    user_name = account_menu()

    if user_name:

        note_menu(user_name)

main_menu()