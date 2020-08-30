# 'week1_QnA.py'
# CCOMP-11P-4316 - Fall 2020
# Written By: Christian Million
# Last Modified: 2020-08-15
#
# Purpose: 
# - Ask the user a question (with a numeric answer) using the input function.
# - Use the answer to write a response.
# - Use a typecast.
# - Use a formatted string.
# - Write well commented code.

# Prompt the user with a question:
ageResponse = input("What is your age?\n")

# Cast the users input to numeric
userAge = int(ageResponse)

# Respond to the user
print(f"{userAge} years old! Eesh! Good luck.")