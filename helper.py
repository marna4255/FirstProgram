"""
methods
Checks whether the user's input is a number or a string,
Checking what time it is right now

"""
# Generic function 
# which checks whether the user's input is integer or string 
# if it's a number:
# check how many digits the number has
# check if the number is even or not
# check whether the number is divisible by 7 without a remainder
def checks_if_user_input_num(user_input):
    # .strip()
    # Remove spaces at the beginning and at the end of the string

    # .isdigit()
    # Check if all the characters in the text are digits
    # return True or False
    if user_input.strip().isdigit():
        print(f"The input {user_input} is a number")
        print(f"The number of digits are: {len(user_input)}")
        if int(user_input) % 2 == 0:
            print(f"The number {user_input} is even")
        else:
            print(f"The number {user_input} is odd")
        if int(user_input) % 7 == 0:
            print(f"The number {user_input} is divisible by 7 without a remainder")
        else:
            print(f"The number {user_input} is divisible by 7 with a remainder")
        
    else:
        print(f"The input {user_input} is a string")

# ------------------------------------------------------------------------------------------------------------------

from datetime import datetime

# A generic function that shows the time now
def see_what_time_it_is():
    while True:
        # current date and time
        now = datetime.now() 
        # strftime()
        # convert dates to strings
        time = now.strftime("%H:%M:%S")
        # end = "\r" means:
        # next line begin at the beginning of the current line
        # example
        # print("line1", end = "\r")
        # print("line2")
        # The print will be : line2
        print(time, end="\r")
       