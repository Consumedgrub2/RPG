import random
import io
import os

exit_code = 0
game_loop = False
game_version = "0.0.1"

while game_loop == False:
    user_input = input("Enter a command:\n")
    if user_input == "quit":
        game_loop = True
    elif user_input == "version":
        print("Version: " + str(game_version))
    elif user_input == "help":
        commands = "quit, version,"
    elif user_input == "start":
        user_input = input("Select your dificulty:\n"\
                           + "0,1,2,3,4\n")
        while user_input not in "01234":
            user_input = input("Not a valid command. Try again\n")
        difficulty = int(user_input)
