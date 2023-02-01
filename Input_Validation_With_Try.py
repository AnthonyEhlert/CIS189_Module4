"""
Program: Input_Validation_With_Try.py
Author: Tony Ehlert
Last date modified: 2/1/2023

The purpose of this program is accept user input to display a formatted string
   representing a user's first name, last name, age, and average score.
   It includes try/except statements for input validation on the scores being entered
The input is a user's first name, last name, and age. As well as three scores for the user
The output is a string displaying the user's last name, first name, age, and average score
"""
#import Constants.py for constant variables
import Constants

# prompt user for first name and store it in first_name variable
first_name = input("Please enter your first name: ")

# use capitalize() method to format first name
first_name = first_name.capitalize()

# prompt user for last name and store it in first_name variable
last_name = input("Please enter your last name: ")

# use capitalize() method to format last name
last_name = last_name.capitalize()

# test print line to verify name variables start with upper case characters
#print(last_name + " " + first_name)

# prompt user for their age & store it in user_age_as_int variable (input cast to int)
# try/except block used for input validation
try:
    user_age = int(input("Please enter your age as a whole number: "))
    if (user_age < 0 or user_age > 150):
        raise ValueError("age cannot be less than 0 or greater than 150")
except:
    print("You did not enter a valid age. Age recorded as 0")
    user_age = 0


# cast input to float type to handle incorrect entry
#user_age_as_float = float(user_age)

# cast to int type for future manipulations
#user_age_as_int = int(user_age_as_float)
# if (user_age == null):
#     user_age = "Invalid Age"
# test print line to validate that user_age_as_int was cast as int
# print(user_age_as_int + 1)

# prompt user for their three scores (cast to int) & assign to variables
# try/except blocks used for input validation
try:
    score_one_as_int = int(input("Please enter your first score as a whole number: "))
    if (0 > score_one_as_int or score_one_as_int > 100):
        score_one_as_int = 0
        raise ValueError("Score out of Range, Score recorded as 0")
except:
    print("Invalid score entry. Score recorded as 0")
    score_one_as_int = 0

# score 2
try:
    score_two_as_int = int(input("Please enter your second score as a whole number: "))
    if (0 > score_two_as_int or score_two_as_int > 100):
        score_two_as_int = 0
        raise ValueError("Score out of Range, Score recorded as 0")
except:
    print("Invalid score entry. Score recorded as 0")
    score_two_as_int = 0

# score 3
try:
    score_three_as_int = int(input("Please enter your third score as a whole number: "))
    if (0 > score_three_as_int or score_three_as_int > 100):
        score_three_as_int = 0
        raise ValueError("Score out of Range, Score recorded as 0")
except:
    print("Invalid score entry. Score recorded as 0")
    score_three_as_int = 0

# calculate total score and assign to variable
scores_total = score_one_as_int + score_two_as_int + score_three_as_int

# test to verify scores_total is correct
# print(scores_total)

# calculate average score and assign to variable
avg_score = scores_total / Constants.NUM_OF_SCORES

# test to verify avg_score was calculated correctly
# print(avg_score)

# creation of output string and assigning to variable
output_string = f"{last_name}, {first_name} age: {user_age} average grade: {avg_score: 5.2f}"

# print out of final output_string
print(output_string)

# observed outputs after manually running code
# Test 1, TONY eHLERT 36 100 100 100 = "Ehlert, Tony age:  36 average grade:  100.00"
# Test 2, jane doe 33 95 100 105 = "Doe, Jane age:  33 average grade:  100.00"
# Test 3, John Smith 25 70 80 90 = "Smith, John age:  25 average grade:  80.00"
# Test 4, jIM BoB 100.25 65 80 90 = "Bob, Jim age:  0 average grade:  78.33"
# Test 5, jim bob 65 -1 100 50 = "Bob, Jim age:  65 average grade: 50.00"
# Test 6, jim bob -65 100 100.0 50 = "Bob, Jim age:  0 average grade: 50.00"
# Test 7, jim bob 65 100 50 75.5 = "Bob, Jim age:  65 average grade: 50.00"
# Test 8, jim bob 151 100 50 105 = "Bob, Jim age:  0 average grade: 50.00"
# Test 9, jim bob 150 90.0 90.0 90.0 = "Bob, Jim age:  150 average grade: 0.00"
# Test 10, jim bob xii 101 101 101 = "Bob, Jim age:  0 average grade: 0.00"
# Test 11, jim bob 65 -1 -1 -1 = "Bob, Jim age:  65 average grade: 0.00"
# Test 12, jim bob 65 100 100 100 = "Bob, Jim age:  65 average grade: 100.00"
# Test 13, jim bob 65 aa aa aa = "Bob, Jim age:  65 average grade: 0.00"