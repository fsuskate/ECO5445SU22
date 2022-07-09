# -*- coding: utf-8 -*-

from multiprocessing.dummy import Array
import numpy as np

print("""
##################################################
#
# ECO 5445: Assignment 03
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

print ("Folder and file Assignment03 and Assignment03.py was created")

print("""
##################################################
## Questions 2
##################################################
""")

A = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

print(A)    
print(type(A))

print("""
##################################################
## Questions 3
##################################################
""")

print(f'* number 7: A[1][2] = {A[1][2]}')
print(f'* row 1: A[0] = {A[0]}')
print(f'* column 2: A[:, 2] = {A[:, 2]}')
print(f'* rows 2 and 3: A[1:2, :] = {A[1:3, :]}')
print(f'* values 7,8,11, and 12: A[1:3, 2:4] = {A[1:3, 2:4]}')

print("""
##################################################
## Questions 4
##################################################
""")

B = 2 * A
print(f'B = 2 * A is \n{B}\n')
B -= 8
print(f'B -= 8 is \n{B}\n')
B = 2*A-8
print(f'B = 2 * A - 8 is \n{B}\n')
print(f'B\'s transpose is \n{B.T}\n')

def getCummulativeSumOfRows(array: Array, message: str):
    cummulativeSumOfRows = 0
    print(message)
    for idx, row in enumerate(array, start=1):
        rowSum = np.sum(row)
        print(f'    ({idx}) -> {rowSum}')
        cummulativeSumOfRows += rowSum
    return cummulativeSumOfRows

cummulativeSumOfRows = getCummulativeSumOfRows(B, '* sum of row values: ')
# use B's transpose to get columns
cummulativeSumOfCols = getCummulativeSumOfRows(B.T, '* sum of col values: ')

print(f'* cummulative sum of row values: {cummulativeSumOfRows}')
print(f'* cummulative sum of col values: {cummulativeSumOfCols}')

print("""
##################################################
## Questions 5
##################################################
""")

ln_array = np.log(B)
print(f'natural log: np.log(B) = \n{ln_array}\n')
sqrt_array = np.sqrt(B)
print(f'square root: np.sqrt(B) = \n{sqrt_array}\n')
square_array = np.square(B)
print(f'square: np.square(B) = \n{square_array}\n')
abs_array = np.abs(B)
print(f'absolute value: np.abs(B) = \n{abs_array}\n')

print("""
##################################################
## Questions 6
##################################################
""")

# create the matrices

# coefficients
A = np.matrix([[1,20], [1,-40]])
print(f'Coefficients matrix A is \n{A}\n')
# results
B = np.matrix([[286], [88]])
print(f'Results matrix B is \n{B}\n')

# calculate the inverse of A
A_inv = np.linalg.inv(A)
print(f'Inverse of A, A_inv, is \n{A_inv}\n')


print ("""
Solve for X matrix:

        A * X = B
 A^-1 * A * X = A^-1 * B
            X = A^-1 * B 
""")


# solve for X 
X = A_inv * B

print(f'Equilibrium price = {X[1][0]} and equilibrium quantity = {X[0][0]}')