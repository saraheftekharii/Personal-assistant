import json
from prompt_toolkit import prompt
def load_notes(user_name):

    try:
        with open(f"notes/{user_name}.json", "r") as file:
            return json.load(file)

    except(FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_note(user_name, notes):

    with open(f"notes/{user_name}.json", "w") as file:
        json.dump(notes, file)


def add_notes(user_name):

    notes = load_notes(user_name)

    while True:

        title = input("Enter your note title: ")
        duplicate = False

        for note in notes:
            if note["title"] == title:
                duplicate = True
        
        if duplicate:
            print("This title already exists! Try another one.")
            continue
        else:
            print("Title added successfully!")
            break

    new_note = input("Enter your new note:\n")
    note = {
        "title" : title,
        "text" : new_note
    }
    notes.append(note)
    save_note(user_name, notes)
    print("Note added successfully!")


def show_notes(user_name):

    notes = load_notes(user_name)

    while True:

        title = input("Enter your note title: ")

        for note in notes:

            if note["title"] == title:

                print("Title:", note["title"])
                print("Text:", note["text"])

                return

        print("Title does not exist! Try again.")



def edit_notes(user_name):

    notes = load_notes(user_name)

    while True:

        title = input("Enter your note title: ")

        for note in notes:

            if note["title"] == title:

                new_note = prompt("Text: ",default=note["text"])

                note["text"] = new_note

                save_note(user_name, notes)

                print("Note updated successfully!")

                return

        print("Title does not exist! Try again.")

def delet_note(user_name):

    notes = load_notes(user_name)

    while True:

        title = input("Enter your note title: ")

        for note in notes:

            if note["title"] == title:

                notes.remove(note)

                save_note(user_name, notes)

                print("Note deleted successfully!")

                return

        print("Title does not exist! Try again.")

        

def note_menu():
    
    while True:
        choice = input(" 1.Add note \n 2.Show note \n 3.Delet note 4.Exit\n")

        if choice == "1":
            add_notes()

        elif choice == "2":
            show_notes()

        elif choice == "3":
            delet_note()

        elif choice == "4":
            break

        else:
            print("Not valid!")
            continue



    
     
    
