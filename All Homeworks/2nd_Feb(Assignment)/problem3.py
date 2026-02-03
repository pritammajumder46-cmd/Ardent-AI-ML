# ONLINE LOGIN SYSTEM

import os
os.system("cls")

class InvalidCredentialsError(Exception):
    pass

credentials = dict()

while True:
    try:
        val = int(input("\n1. I want to sign in\n2. I want to login\n3. exit\n[Enter the serial number dorrectly]: "))
        match val:
            case 1:
                Username = input("Enter your username: ")
                Password = input("Enter your password: ")
                credentials.update({Username : Password})
            case 2:
                flag = 0

                Username_user = input("\nEnter your username: ")
                Password_user = input("Enter your password: ")

                if Username_user in credentials and credentials[Username_user] == Password_user:
                    print("\nWelcome to The Software")
                    flag = 1
                    break
                if flag == 0:
                    raise InvalidCredentialsError("Invalid Credintials")

            case 3:
                break
            case _:
                raise ValueError("Enter a value correctly")

                
    except ValueError as e:
        print("Error: ", e)
    except InvalidCredentialsError as e:
        print("Login Error: ", e)