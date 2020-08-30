# 'undo_upper_decker_week5.py'
# CCOMP-11P-4316 - Fall 2020
# Written By: Christian Million
# Last Modified: 2020-08-17
#
# PROMPT:
# This is the opposite of the previous assignment. (This is also doomed to failure, I do not know a flawless automated solution to this.)
# Make a best attempt at this, but it will not be expected to be flawless.
# 
# Here's your task: 
#  - read a text file that has had all the spaces removed from it and put them back.
#  - (Use your previous program to generate some sample to play with.)
#  - You may need a list of words to compare to, here's one (https://github.com/dwyl/english-words/blob/master/words_alpha.txt). 
# 
# Some suggestions:
# 
# - You can probably assume that commas and periods should be followed by a space.
# - The issue here is that some words are tricky because they can be split up multiple ways. Think 'a' and 'bet' vs 'abet'.
# - Proper nouns are a nightmare.
# - There's a split method for strings that might be helpful.
# - Your program doesn't have to be fully functional, but it should be able to handle simple cases.
#
# Bonus:
# 
# - Write a separate program to find as many problem words as possible.
# - Come up with the funniest example of a sentence that can be parsed two ways.