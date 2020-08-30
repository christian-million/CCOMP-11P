# 'dieroll.py'
# CCOMP-11P-4316 - Fall 2020
# Written By: Christian Million
# Last Modified: 2020-08-28
#
# PROMPT:
# Your goal is to write a dice roller that duplicates the above* functionality in Python.
# To submit your assignment, provide a link to your repl or upload a file.
#   *How many die would you like to roll? (prompt user)
#    - 17 (user input)
#   *How many sides should they have? (prompt user)
#    - 5 (user input)
#
# Challenge modes:
#   - Ascii art
#   - Information summaries, max, min, sum, average, etc
#   - Validate user input

# Use the randint function
from random import randint


# Create a DieRoll class that keeps track of key features of die rolls.
class DieRoll:
    """ A class used to capture a sequence of dice rolls

    Attributes
    ----------
    rolls: list
        a list containing the value of each roll
    sides: int
        the number of sides each die
    min: int
        the lowest value of `rolls`
    max: int
        the highest value of `rolls`
    sum: int
        the sum of all `rolls`
    mean: float
        the average value of `rolls`

    Methods
    -------
    dist()
        Returns a dictionary of frequencies for each `side` {side: count}
    hist()
        Prints a histogram of dist to the console
    """
    def __init__(self, rolls, sides):
        self.rolls = rolls
        self.max = max(rolls)
        self.min = min(rolls)
        self.sum = sum(rolls)
        self.mean = sum(rolls)/len(rolls)
        self.sides = sides

    def __str__(self):
        x = "====== Roll Summary ======\n" + \
            f"  Rolls: {len(self.rolls)}; Sides: {self.sides}\n" + \
            f"  Rolls 1-10: {', '.join(map(str, self.rolls[:10]))}, ...\n" + \
            f"  Min Roll: {self.min}" + \
            f"  Max Roll: {self.max}" + \
            f"  Sum Rolls: {self.sum}" + \
            f"  Mean Rolls: {round(self.mean, 2)}"
        return x

    def dist(self):
        """Summarises the number of times each side was rolled"""
        # Uses a Dictionary Comprehension to return a dictionary of counts for each side
        # Reference: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
        return {side: sum([1 for i in self.rolls if i == side]) for side in range(1, self.sides + 1)}

    def hist(self):
        """Prints a histogram of rolls"""
        # Get Distribution of Rolls
        dist = self.dist()

        # Print title and remind user how may rolls and sides
        print("====== HISTOGRAM ======")
        print(f" Rolls: {len(self.rolls)}; Sides: {self.sides}\n")

        # Print "=" for each count
        for i in dist:
            # Add a space before "|" if the side value < 10
            # This is to align y-axis labels
            # Uses inline ifelse statement
            #  (reference: https://docs.python.org/3/reference/expressions.html#conditional-expressions)
            marker = " |" if i < 10 else "|"
            print(i, marker, "=" * dist.get(i))


def roll_die(num, sides):
    """Simulates rolling dice by generating 'num' random integers between 1 and 'sides'. Returns a DieRoll object.

    Arguments
    ---------
    num: int
        The number of dice to roll
    sides: int
        The number of sides each die should have
    """
    rolls = [randint(1, sides) for each in range(num)]
    return DieRoll(rolls, sides)


# Create function to capture a "ranged" integer from user
def get_ranged_int(prompt, min, max):
    """Forces user to respond with an integer between 'min' and 'max'

    Arguments
    ---------
    prompt: str
        A prompt to send the user
    min: int
        The minimum value the user can enter
    max: int
        The maximum value the user can enter
    """

    x = None
    criteria = f'It must be an integer between {min} and {max}.'

    # Keep prompting user until input is valid (i.e., int between min and max)
    while x not in list(range(min, max + 1)):
        print(prompt, criteria)

        # try casting input as int and check if it is within range
        try:
            x = int(input("> "))
            if x not in list(range(min, max + 1)):
                print("Hm... Not quite. Remember:", criteria)
        except:
            print("Hm... Not quite. Remember:", criteria)
    # Return user input
    return x


def main():
    # Get User Input
    user_num = get_ranged_int("How many die?", 1, 100)
    user_sides = get_ranged_int("How many sides?", 1, 20)

    # Roll Die and return DieRoll object
    my_rolls = roll_die(user_num, user_sides)

    # Print the list of rolls for the user
    print("Rolls:\n", my_rolls.rolls, "\n")

    # Print the DieRoll object (a summary of rolls)
    print(my_rolls, "\n")

    # Show user the distribution of rolls
    print("Roll Distribution:\n", my_rolls.dist(), "\n")

    # Generate a histogram
    my_rolls.hist()


# Run the program if script executed directly.
if __name__ == "__main__":
    main()
