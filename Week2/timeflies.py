# 'timeflies.py'
# CCOMP-11P-4316 - Fall 2020
# Written By: Christian Million
# Last Modified: 2020-08-29
#
# PROMPT:
# When time flies, we often find ourselves converting a huge number of
# seconds to something more reasonable.
# Your task today is to write a program that has the following:
#
# - generate a random number between 100 and 8000, assume this represents a number of seconds
# - convert that number of seconds into minutes (and perhaps hours?)
# - Provide nicely formatted output for the user telling them about the calculations (including the starting number)
# - Output should look something like '196 seconds is 3 minutes and 16 seconds, because 3*60 + 16 = 196.'
# - It's ok if it says '196 seconds is 0 hours, 3 minutes and 16 seconds, because 0*3600 + 3*60 + 16 = 196.', but it'd be better if it didn't.
# - Commented code
#
# Note: If needed, this can be adapted to accomodate turning more than 24 hours into e.g., "1 day and 2 hours..."

# Bring in a function to generate random integers from the 'random' library.
from random import randint


def main():
    # Generate a random number between 100 and 8000
    random_seconds = randint(100, 8000)

    # How many times can randSeconds be divided by 3600 (3600 seconds in an hour)
    # Use // to return just the integer (no remainder)
    num_hours = random_seconds // 3600

    # How many seconds remain after dividing random_seconds by 3600?
    # Use % to capture remainder
    remaining_seconds = random_seconds % 3600

    # How many minutes fit into the remaining seconds?
    # Just want the integer, so use //
    num_minutes = remaining_seconds // 60

    # How many seconds remain after fitting seconds into minutes?
    # Finding remainder so use %
    remaining_seconds = remaining_seconds % 60

    # If hour is 0, we don't need to print it.
    # We COULD provide some ifelse statments to make sure the singular/plural form of e.g., minute(s) is used.
    if num_hours == 0:
        print(f'{random_seconds} seconds is {num_minutes} minute(s) and {remaining_seconds} second(s), because {num_minutes}*60 + {remaining_seconds} = {random_seconds}.')
    else:
        print(f'{random_seconds} seconds is {num_hours} hour(s), {num_minutes} minute(s) and {remaining_seconds} second(s), because {num_hours}*3600 + {num_minutes}*60 + {remaining_seconds} = {random_seconds}.')


# Run the main function if this file is executed directly
if __name__ == "__main__":
    main()
