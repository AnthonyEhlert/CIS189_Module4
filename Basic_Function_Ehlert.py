"""
Program: Basic_Function_Ehlert
Author: Tony Ehlert
Last date modified: 2/1/2023

The purpose of this program is to define a function that gets a user's name, hours worked, and pay rate
and validates all inputs, then prints out the outputs as a string
The input is a string (user's name), integer(hours worked), and float(pay rate)
The output is print statement to the console with the inputted data
"""
# define the function
"""
This function asks a user for their name, hours worked, and pay rate
and prints a string containing the information
"""


def hourly_employee_input():
    # try/except blocks used for input validation
    try:
        # prompt user for their name
        user_name = input("Please enter your name: ")

        # check to ensure something was entered, if not set name to "No Name Entered" and raise error
        if (len(user_name) == 0):
            user_name = "No Name Entered"
            raise ValueError
    except:
        print("You didn't enter anything!")

    try:
        # prompt user for hours worked and ensure an integer was entered
        hours_worked_as_int = int(input("How many hours(whole number) did you work: "))

        # if statement checks for positive number
        if (hours_worked_as_int < 0):
            raise ValueError("You did not enter a positive number")
    except:
        hours_worked_as_int = 0
        print("Invalid input for hours worked. Hours worked will be set to 0 ")

    try:
        # prompt user for pay rate and ensure a string was not entered
        pay_rate_as_float = float(input("What is your hourly pay rate: "))

        # if statement to check for positive number
        if (pay_rate_as_float < 0):
            raise ValueError("You did not enter a positive number")
    except:
        pay_rate_as_float = 0
        print("Invalid input for pay rate. Pay rate will be set to 0 ")

    # create variable for final output string
    output_string = f"{user_name} worked {hours_worked_as_int} hours at a rate of ${pay_rate_as_float: 5.2f} per hour"

    # print output_string variable
    print(output_string)

# Driver
if __name__ == '__main__':
    hourly_employee_input()
