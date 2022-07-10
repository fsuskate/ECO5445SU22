# -*- coding: utf-8 -*-

import numpy as np
import time

print("""
##################################################
#
# ECO 5445: Assignment 04
#
# Francis Surroca
#
# Due July 10, 2022
# 
##################################################
""")

print("""
##################################################
## Questions 1
##################################################
""")

print ("Folder and file Assignment04 and Assignment04.py was created")

print("""
##################################################
## Questions 2
##################################################
""")

# Constants
r = .5
r_sqr = r**2
circle_center = .5

def isInCircle(x: float, y: float) -> bool:
    return ((x-circle_center)**2 + (y-circle_center)**2) <= r_sqr

def estimatePi(numTries=10000, verbose=False) -> float: 
    """ 
    Estimates the value of PI using the Monte Carlo method https://en.wikipedia.org/wiki/Monte_Carlo_method. 

    Summary:
    We generate randomized 'rain' drops that will 'fall' on the circle and the square keeping track of how 
    many drops fall on each.

    Then, using a unit square of length = 1, with a unit circle of diameter = 1 and radius = .5, we have
    * the probability P of a rain drop landing in the circle = (pi*r^2)/(4*r^2)
    ** using the distance formula d = sqrt((x_p-x_c)^2 + (y_p-y_c)^2)
    ** if d^2 <= r*2, then a point (x,y) is in the circle
    * so, 4 * P(rain in circle) = pi
    * and pi = 4 * P(rain in circle) 
    * since, P(rain in circle) = rain falls in circle / rain falls in square
    ** where C = rain falls in circle
    ** and S = rain falls in square
    * we have estimate_of_pi = 4C/S

    """
    C = 0
    S = 0

    for _ in range(numTries): 
        x = np.random.uniform(0,1)
        y = np.random.uniform(0,1)
        S += 1
        if (isInCircle(x, y)):
            C += 1
    estimate_of_pi = 4*C/S

    if (verbose):
        print(f'In circle: {C}')
        print(f'In square: {S}')
        print(f'Probability of being in circle: {C/S}')
        print(f'Estimated pi: {estimate_of_pi}\n')

    return estimate_of_pi

def runTimedEstimate(numTries: int):
    start = time.time()
    estimate = estimatePi(numTries)
    end = time.time()
    print(f'Estimate of pi with {numTries} rain drops: \033[32m{estimate}\033[0m took \033[33m{round(end-start, 4)}\033[0m seconds. ')

help(estimatePi)

print("""\n\33[36mRunning default simulation in 'verbose' mode.\n\33[0m""")
estimatePi(verbose=True)

print("""\n\33[36mRunning simulation with several predefined values for rain drops.\n\33[0m""")

tries = [10000, 25000, 100000, 250000, 500000, 1000000]
for curr_try in tries:
    runTimedEstimate(curr_try)

print("""\n\33[36mNow you give it a few tries...go crazy. Enter a value for the number of 
rain drops to randomize. When you are ready to stop, just enter 'X' or 'x'.\n\33[0m""")

val = ''
while (True):
    val = input('Enter a number of rain drops: ')
    if (val == 'X' or val == 'x'):
        break
    runTimedEstimate(int(val))