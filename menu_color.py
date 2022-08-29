
from helper import *
from termcolor import cprint

def menu():
    cprint("Welcome to the menu", 'blue','on_white', attrs=['bold'])
    cprint("press 1 to analyze the input from the user", 'red',attrs=['bold']) 
    cprint("press 2 to see what time it is", 'green',attrs=['bold']) 
    cprint("press 3 to exit",  'yellow',attrs=['bold'])   
    user_selection = input("Please enter your selection: ")
    return int(user_selection)


def main():
    user_selection = menu()
    while user_selection != 3:
        if user_selection == 1: checks_if_user_input_num(input("Please enter your name: "))
        if user_selection == 2: see_what_time_it_is()
        user_selection = menu()
    


if __name__ == "__main__":
    main()