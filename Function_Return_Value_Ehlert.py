"""
Program: Function_Return_Value_Ehlert.py
Author: Tony Ehlert
Last date modified: 2/2/2023

The purpose of this program is to define a function that gets a user's name, hours worked, and pay rate
and validates all inputs, then calls a separate function to calculate the weekly pay and returns that value.
Finally, the first function will return the calculated weekly pay and it will be printed in the driver

The input is a string (user's name), integer(hours worked), and float(pay rate)
The output is print statement to the console with the calculated weekly pay
"""
from Constants import HOURS_IN_WEEK


def weekly_pay(hours_worked, hourly_pay_rate):
    """
    Calculates the total weekly pay of an employee based on hours worked and their pay rate

    :param hours_worked: integer type representing total hours works
    :param hourly_pay_rate: float type representing the hourly rate of pay
    :return: float value representing the total weekly pay
    """
    calc_weekly_pay = hours_worked * hourly_pay_rate
    return calc_weekly_pay


def hourly_employee_input():
    """
    This function asks a user for their name, hours worked, and pay rate
    and prints a string containing the information

    :return: string representing the user's name and the calculated weekly pay amount
    """

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
        elif (hours_worked_as_int > HOURS_IN_WEEK):
            raise ValueError("There are only 168 hours in a week and you entered more than that.")
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

    # call of weekly_pay function to get calculated weekly pay
    weekly_pay_amount = weekly_pay(hours_worked_as_int, pay_rate_as_float)

    # create variable for final output string
    output_string = f"{user_name} will be paid ${weekly_pay_amount: 6.2f} for the week."

    # return final output string
    return output_string


# Driver
if __name__ == '__main__':
    # print of return value from hourly_employee_input()
    print(hourly_employee_input())
