# 'functions_week3.py'
# CCOMP-11P-4316 - Fall 2020
# Written By: Christian Million
# Last Modified: 2020-08-30
#
# PROMPT:
# Functions will be one of the major tools you use for writing programs.
# For this assignment, write five functions.
# At least 3 must take input, at least 3 must return something
# and at least one must take multiple inputs.
# You can make up your own if you like, but here are some ideas.

# Use the random library

from random import randint, shuffle, choices


# FUNCTION 1
# Takes input: True
# Return Val: True
# Multiple Input: True
def into_parts(num, parts):
    '''Randomly divides a number (num) into a specifice number of bins (parts). Returns a list.

    This function could take 10 and divide it into 3 parts: (3, 4, 3).
    It is good for generating random weights.

    Arguments
    ---------
    num: int
        The number to divide

    parts: int
        The number of bins to distribute the number into
    '''
    # Can't divide num into parts > num
    if(parts > num):
        return None

    # Ends recursive and its easy to dive nums into 1 part
    if(parts == 1):
        return [num]

    # Else return a random num between 1 and num-parts (this is so each 'part' has at least 1 in it)
    else:
        x = randint(1, num - parts)
        # Recursively call the into_parts function
        groups = [x] + into_parts(num - x, parts - 1)

    return(groups)


# FUNCTION 2
# Takes input: True
# Return Val: True
# Multiple Input: False
# Description:
def unlist(a_list):
    """Turn a list of lists into a single list"""

    # This is just a shortcut function for a common
    # list comprehension
    return [col for row in a_list for col in row]


# FUNCTION 3
# Takes input: True
# Return Val: True
# Multiple Input: False
def transpose(a_list):
    """Transposes a matrix-like list"""

    # Create an empty "Transposed" version of the list.
    # e.g., a 3x4 matrix would become a 4x3 matrix
    # Loop through number of columns THEN number of rows (typically the other way around)
    shell = [[None for r in range(len(a_list))] for c in range(len(a_list[0]))]

    # Then for each row and column in the original list
    # swap the indexes and assign the value to the new index
    # e.g., "a" at (2, 3) becomes (3, 2)
    for ri, row in enumerate(a_list):
        for ci, col in enumerate(row):
            shell[ci][ri] = col

    return shell


# FUNCTION 4
# Takes input:
# Return Val:
# Multiple Input:
def histogram(a_list, levels=None):
    """Prints a histogram of a given list. Defauls assumed all levels of a factor are included in the list.

    Summarises the elements of a list and prints a histogram to the console. Levels argument exists for when
    all known levels might not be present in the list. e.g., summarize sales by month, but no sales in Oct, I'd
    want to see Oct empty (not just Sept then Nov.)

    Arguments
    ---------

    a_list: list
        A list to summarise and "graph"

    levels: list
        A unique list of known possible elements in a_list.
    """
    # Default
    if levels is None:
        # If list is all integers then levels should be range(min, max)
        if all([isinstance(i, int) for i in a_list]):
            levels = [range(min(a_list), max(a_list))]

        # Otherwise levels are unique elements in a_list
        else:
            levels = list(set(a_list))

    # If list is provided make sure it is unique
    else:
        levels = list(set(levels))

    # Sort the levels, so printing is ordered rationally
    levels.sort()

    # Dictionary comprehension of counts. Result {item: count}
    dist = {each: sum([1 for i in a_list if i == each]) for each in levels}

    # Find the element with most characters for consistent printing
    pad = len(max(levels, key=len)) + 1

    # Print the Histogram with padding for axis variables
    for i in dist:
        marker = " " * (pad - len(i)) + "|"
        print(i, marker, "=" * dist.get(i))


# FUNCTION 5
# Takes input: True
# Return Val: True
# Multiple Input: False
def gen_password(length):
    """Generates a random password with a specified length"""

    # A good password should have lowercase, uppercase, numbers, and symbols
    # Use a dicitonary to store potential options
    opts = {'alpha': 'abcdefghijklmnopqrstuvwxyz',
            'alpha_cap': 'abcdefghijklmnopqrstuvwxyz'.upper(),
            'num': '0123456789',
            'sym': '!-_@#$%&'}

    # Generate a random list of weights for each of the 'opts' types
    # e.g, alpha might be weighted more heavily than num (we don't want equal weights because it is more predictable)
    weights = into_parts(length, 4)

    # Make it random because I think `into_parts` might return larger numbers in the beginning indexes??
    shuffle(weights)

    # Select `weight` number of characters with replacement from each opts.values
    # I wonder if this can be done with ZIP
    # ALTERNATIVE APPROACH : chars = map(lambda x,y: random.choices(population = x, k = y), opts.values(), weights)
    chars = []
    for each_option, each_weight in zip(opts.values(), weights):
        chars.append(choices(each_option, k=each_weight))

    # The above returns a list of lists - this flattens it to just a list
    flat_char = unlist(chars)

    # Randomize elements in the list
    shuffle(flat_char)

    # Turn into a single string
    password = "".join(flat_char)

    # Return the password
    return(password)


def main():
    # Initialize some example lists to test out the functions
    a_list = [[1, 2, 3], ['a', 'b', 'c'], ['aa', 'bb', 'cc'], ['00', '00', '00']]
    h = ['a', 'd', 'a', 'c', 'a', 'd', 'd', 'a', 'd', 'a', 'a', 'a', 'c', 'd', 'd', 'a', 'c', 'a']

    # Example of Function #1
    print("Function #1: into_parts(10, 3)\n", into_parts(10, 3))

    print()

    # Example of Function #2
    print("Function #2: unlist(a_list)")
    print("a_list:", a_list)
    print("unlist(a_list):", unlist(a_list))

    print()

    # Example of Function #3
    print("Function #3: transpose(a_list)")
    print("a_list:", a_list)
    print("transpose(a_list):", transpose(a_list))

    print()

    # Example of Function #4
    print("Function #4: histogram(h)")
    print("h:", h)
    print("histogram(h, ['a', 'b', 'c', 'd']):")
    histogram(h, ['a', 'b', 'c', 'd'])

    print()

    # Example of Function #5
    print("Function #5: gen_password(10)\n", gen_password(10))


if __name__ == '__main__':
    main()
