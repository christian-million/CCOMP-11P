# operations worksheet written by Joe Manlove
# Used in Programming and Methodologies 1 in Python
# Last Revised 5/19/2020

# Instructions: You should write code below each comment attempting to carry out the instructions
# you should also include print statements about what you're doing so the output is readable.
# There's an example at the start of the Boolean Section
# I've included some print statements to keep sections straight, no need to change them.
# in cases where errors are generated, feel free to comment out your attempt, but please explain the error
# ================================================================
# Modified per the instructions by Christian Million on 2020-08-28

# This section is for numerical operations
print('Numerical Operations Section')

# make two numerical values x and y, initialize them to 4 and 9 respectively
x = 4
y = 9

# Print out the types of x and y.
print(f'{x} is {type(x)} and {y} is {type(y)}.')

# print x+y
print(f'{x} + {y} is {x + y}.')

# print x/y
print(f'{x} / {y} is {x / y}.')

# print the type of x/y
print(f'{x} / {y} returns type {type(x / y)}.')

# print x*y
print(f'{x} * {y} is {x * y}.')

# print the type of x*y
print(f'{x} * {y} returns type {type(x * y)}.')

# print x + 0.0
print(f'{x} + 0.0 is {x + 0.0}.')

# print the type of x+0.0
print(f'{x} + 0.0 returns type {type(x + 0.0)}.')

# print x//y
print(f'{x} // {y} returns {x // y}.')

# print the type of x//y
print(f'{x} // {y} returns type {type(x // y)}.')

# write a comment explaining the difference between // and /.
# / is a division operator which returns the exact quotient of two numbers
# whereas // returns the nearest whole integer (rounded down) of a  quotient, without decimals.

# print x<y
print(f'{x} < {y} returns {x < y}.')

# why is (x<y) == True?
print(f'{x} < {y} == True because {x} (x) is less than {y} (y).')
print('The \'<\' operator compares whether the left-hand side is less than the right hand side.')

# Notice that == and = are different, perform some experimentation or googling to discover the difference
# print out a string explaining the difference
print('\'=\' is an assignment operator, meaning it is used to establish a relationship between a name and a value for variables. The \'==\' is an operator used to test equality.')

# print y%x
# being confused by this one is ok. There'll be a deeper dive on this seperately.
print(f'{y} % {x} returns {y % x}.')

# this is the Boolean Section
# a boolean is a variable that is either True or False
# notice that True and False are case sensative
print('Boolean Operations Section')

# make a variable t and a variable f, set them to True and False respectively
t = True
f = False

# print t and f
# I did this one for you, you're welcome :)
# notice and is a special word, don't try to use it as a variable name :P
print(f'{t} and {f} is: {t and f}.')

# print t or f
print(f'{t} or {f} returns {t or f}.')

# print !t
print(f'!{t} returns an error, but not({t}) returns {not(t)}.')
print('https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals')
print('Apparently, \'!\' instroduces a \'conversion field\'. But I don\'t know what that means.')
# print !f
print(f'!{f} returns an error, but not({f}) returns {not(f)}.')
print('https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals')
print('Apparently, \'!\' instroduces a \'conversion field\'. But I don\'t know what that means.')
# This is the String Section
print('String Operations Section')

# make two variables, s and ten set them to 'This is a string.' and '10' respectively.
s = "This is a string."
ten = '10'

# print s + ten
print(f'\'{s}\' + \'{ten}\' returns {s + ten}.')

# print s - ten
print(f'\'{s}\' - \'{ten}\' returns an error because there is no \'operand type\' for the \'-\' operator between 2 strings.')

# print ten + s
print(f'\'{ten}\' + \'{s}\' returns {ten + s}.')

# print the type of ten
print(f'type({ten}) returns {type(ten)}')

# print ten.isnumeric()
print(f'ten.isnumeric() returns {ten.isnumeric()}.')

# print len(ten) and len(s)
print(f'len({ten}) is {len(ten)} and len({s}) is {len(s)}.')

# print a string explaining the results
print('The len() function returns the length of an object. In the case of \'ten\' and \'s\', since they are both strings, the length is the number of characters that build up the string.')

# print s[:4]
print(f's[:4] returns {s[:4]}')

# print s[:4]
print(f's[:4] returns {s[:4]}')

# print s[0:4]
print(f's[0:4] returns {s[0:4]}')

# print s[2:]
print(f's[2:] returns {s[2:]}')

# print s[-4:]
print(f's[-4:] returns {s[-4:]}')

# print s[0]
print(f's[0] returns {s[0]}')

# print a string that explains this [] thing...
print('[] is the syntax used to access the index of an object. For example s[0] is a way to access the 0th index of the s variable.')

# This is the Mixed Type Section
print('Mixed Type Section')

# print x*ten
print(f'{x} * {ten} is {x * ten}')

# print 2 * s
print(f'{2} * {s} is {2 * s}')

# print t*y
print(f'{t} * {y} is {t*y}')

# print f*y
print(f'{f} * {y} is {f * y}')

# print the first 5 letters of s six times
for each_num in range(6):
    print(s[0:5])
# Or maybe you meant this:
print(f'Or maybe you meant this: {s[0:5] * 6}.')

# print s + y or explain the issue
print(f'{s} + {y} doesn\'t work because you cannot concatenate str variables with int variables.')

# print ten + y or explain the issue
print(f'{ten} + {y} doesn\'t work because you cannot concatenate str variables with int variables.')

# force ten + y to work by turning both into strings
print(f'{ten} + str({y}) is {ten + str(y)}')

# force ten + y to work by turning both into numbers
print(f'int({ten}) + {y} is {int(ten) + y}')
