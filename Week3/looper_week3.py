# 'looper_week3.py'
# CCOMP-11P-4316 - Fall 2020
# Written By: Christian Million
# Last Modified: 2020-08-29
#
# PROMPT:
# For this one, I'd like you to write a program that includes at least two loops, preferably nested.
# Some example idea that you might use are provided, but you're welcome to be creative and come up with your own .
# - noVowelsPlus, a program consisting largely of a single function that takes a list of strings and removes the vowels.
#   (loop through stings in list, and characters in strings.)
# - Ascii art hangman (a while loop outside and a for loop printing out ascii art line by line)
# - Ascii art your dice roller
# - pythonTNT project, use this stackoverflow post and this image file to print out which pixels in the image are black.
#   (This was the starting point for rendering a giant statue of the word 'Python' out of TNT in Minecraft.)

# Program Description:
# https://www.practicepython.org/


# Tutorial on matplotlib.image: https://matplotlib.org/tutorials/introductory/images.html

# Import some image processing packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# Returns a list of tuples identifying which pixels contain which values
def which_pix(img, r=0, g=0, b=0, a=0):
    """Returns a list of tuples that identify which pixels contain the requested rgba values.

    NOTE: Defaults to blank pixels

    Arguments
    ---------

    img: list
        an image object returned from matplotlib.image.imread()

    r: float
        the amount of red in the pixel from 0 to 1

    g: float
        the amount of green in the pixel from 0 to 1

    b: float
        the amount of blue in the pixel from 0 to 1

    a: float
        the amount of transparency in the pixel from 0 to 1
    """

    # Initialize an empty list to add desired pixels to.
    pix = []

    for ri, row in enumerate(img):
        for ci, col in enumerate(row):
            # If the pixel contains the requested values append a tuple of
            #   it's row index and column index
            #   into the pixel list
            if col[0] == r and col[1] == g and col[2] == b and col[3] == a:
                pix.append((ri, ci))

    # Send the user the list of pixels
    return(pix)


# Create a function to replace the pizels of an image
def replace_pix(img, pix, color):
    """Replaces specific pixels with a desired color (in the form [r, g, b, a])

    Arguments
    ---------

    img: list
        an image object returned from matplotlib.image.imread()

    pix: list of tuples
        which pixels to change

    color: list
        a list of 4 floating numbers between 0 and 1
    """
    # Replace every pixel identified in pix with color
    for pixel in pix:
        img[pixel[0]][pixel[1]] = color

    # Return the modified img
    return img


# Function to grab the dimensions of the image
def img_dim(img):
    """Returns the dimensions of an image as a tuple (height, width)

    Arguments
    ---------

    img: list
        an image object returned from matplotlib.image.imread()
    """
    # Images from matplotlib.image.imread have the rows as the outer list
    h = len(img)

    # The columns are the inner lists
    w = len(img[0])

    # Return the dimensions as a tuple
    return (h, w)


# Helper function to turn interger based RGBA values into the percentages
# That matplotlib.image.imread seems to interpret
def rgba_to_perc(rgba):
    new = [[color/255 for color in i] for i in rgba]
    return new


def main():

    # Read in the Python Pixels Image
    # Convert it to a normal list (seems to be brought in as a numpy array)
    img = mpimg.imread('pythonPixels.png').tolist()

    # Unpack image dimensions to initialize height and width variables
    height, width = img_dim(img)

    # Get a list of all available pixels in the image
    pixels = [(h, w) for h in range(height) for w in range(width)]

    # Apparently the only thing that distinguishes the letters in the PYTHON image, is that the alpha is at 1
    # Find out which pixels those are:
    py_pix = which_pix(img, 0, 0, 0, 1)

    # Get the non-PYTHON pixels (aka the background)
    # ALTERNATIVE APPROACH: which_pix() (defaults to blank pixels)
    background = [p for p in pixels if p not in py_pix]

    # Let's change the PYTHON color to grey
    new_img = replace_pix(img, py_pix, [.5, .5, .5, 1])

    # Let's change the BACKGROUND color to RED at half opacity
    new_img = replace_pix(new_img, background, [1, 0, 0, .5])

    # Not entirely sure about these lines of code, yet.
    # If it's like ggplot2, then you can create a graph
    # and then show the most recently created graph.
    # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html
    # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.show.html
    imgplot = plt.imshow(new_img)
    plt.show()


if __name__ == '__main__':
    main()
