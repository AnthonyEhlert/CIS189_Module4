"""
Program: Function_Parameter_And_Return_Ehlert.py
Author: Tony Ehlert
Last date modified: 2/2/2023

The purpose of this program is to call a function that accepts a string class name and integer number
and then returns a string containing the repeated class name equal to the number
The input is class name as a string, and a number as an integer
The output is a print to the console with the class name repeating
"""


def multiply_string(class_name, times_to_repeat):
    """
    This function returns a string of the string input repeating by the number input

    :param class_name: a string representing a favorite class
    :param times_to_repeat: integer representing the number of times the class_name is to be repeated
    :return: string value with the class_name repeating by the value of times_to_repeat
    """

    # try/except block used for parameter validation
    try:
        times_to_repeat_as_int = int(times_to_repeat)
        if (2 < times_to_repeat < 7):
            output_string = (class_name) * times_to_repeat
        else:
            raise ValueError("The number must be between 2 and 7")
    except:
        output_string = "Invalid function call. Number must be a whole number between 2 and 7"
    return output_string

#driver
if __name__ == '__main__':
    print(multiply_string("Java!", 4))