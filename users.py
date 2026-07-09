import json



def load_users():

    try:
        with open("users.json", "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_users(users):

    with open("users.json", "w") as file:
        json.dump(users,file)

def register():
    users = load_users()
    while True:
        user_name = input("Enter your username:")
        duplicate = False

        for user in users:
            if user["user_name"] == user_name:
                duplicate = True
        if duplicate:
            print("Username already exists!")
            continue
        else:
            pass_word = input("Enter your password:")
            break
    user = {
        "user_name":user_name,
        "pass_word":pass_word
    }
    users.append(user)
    save_users(users)
    print("Register successful!")


def login():

    users = load_users()

    user_name = input("Enter your username: ")

    for user in users:

        if user["user_name"] == user_name:

            while True:

                pass_word = input("Enter your password: ")

                if user["pass_word"] == pass_word:

                    print(f"Login successful!\nHello {user_name}")
                    return user_name
                
                    
                

             
                print("Wrong password. Try again!")


    print("User not found!")


def account_menu():
    while True:

        choice = input(" 1.Login \n 2.Register \n 3.Exit\n")
        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            break
        else:
            print("Not valid!")
            continue
