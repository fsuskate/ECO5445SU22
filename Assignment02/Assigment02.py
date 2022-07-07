# -*- coding: utf-8 -*-
class colors:
    black = "30m"
    red = "31m"
    green = "32m"
    yellow = "33m"
    blue = "34m"
    magenta = "35m"
    cyan = "36m"
    white = "37m"

def pretty_print(string: str, color=colors.white):
    print(f'\33[1;{color}{string}\33[37m')

def pretty_print_heading(string: str, color=colors.yellow):
    pretty_print(str, color)

pretty_print_heading("""
##################################################
#
# ECO 5445: Assignment 01
#
# Francis Surroca
#
# Due July 5, 2022
# 
##################################################\033[1;37m
""")

pretty_print_heading("""
##################################################
## Questions 1
##################################################
""")

print ("File Assignment02.py was created")

pretty_print_heading("""
##################################################
## Questions 2
##################################################
""")

intTwo = 2
floatTwo = 2.0
mixed = 10j
aString = "2 Cool for School"
aBool = True

print(type(intTwo))
print(type(floatTwo))
print(type(mixed))
print(type(aString))
print(type(aBool))

pretty_print_heading("""
##################################################
## Questions 3
##################################################
""")

A = [intTwo, floatTwo, mixed, aString, aBool];
print(A)

pretty_print_heading("""
##################################################
## Questions 4
##################################################
""")

B = "I like pie more than cake."
print(B[:6])
print(B[7:15])
print(B[16:]) # Didn't want period included (-2)
print(B[:6] + " " + B[11:16] + B[21:]) # Follow through error

pretty_print_heading("""
##################################################
## Questions 5
##################################################
""")

def foobar(value: int) -> str:
    """ This function takes an integer and applies the following rules: 
    * If it is a multiple of 3 return the string "foo"
    * If it is a multiple of 5 return the string "bar"
    * If it is a multiple of 15 return the string "foobar"
    * If it does not satisfy any of those, return the string "Not a multiple of 3, 5, or 15"
    # >>> foobar(9)
    # "foo"
    # >>> foobar(10)
    # "bar"
    # >>> foobar(45)
    # "foobar"
    # >>> foobar(19)
    # "Not a multiple of 3, 5, or 15"   
    """ # Missing examples. I inserted some (-5)
    if (type(value) != int):
        print("Only integer values can be entered.")
        return "invalid"

    if (value % 15 == 0):
        return "foobar"
    elif (value % 3 == 0):
        return "foo"
    elif (value % 5 == 0):
        return "bar"

    return "Not a multiple of 3, 5, or 15"

pretty_print_heading("""
##################################################
## Test Cases
##################################################
""")

help(foobar)
print('\033[1;32m it should return foo when passed a multiple of 3 -> \033[1;37m', foobar(33))
print('\033[1;32m it should return foobar when passed a multiple of 15 -> \033[1;37m', foobar(60))
print('\033[1;32m it should return bar when passed a multiple of 5 -> \033[1;37m', foobar(40))
print('\033[1;32m it should return not a multiple message when passed no multiples of 3, 5, or 15 -> \033[1;37m', foobar(11))
print('\033[1;32m it should return invalid when passed invalid input string \"dog\" -> \033[1;37m', foobar("dog"))
print('\033[1;32m it should return invalid when passed invalid input float 2.0 -> \033[1;37m', foobar(2.0))
