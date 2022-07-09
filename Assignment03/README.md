# Assignment03
 
Upload your url to your folder that you create.

1. Create a folder called "Assignment03"
2. Construct the following array "A" with i = 3 rows and j = 4 columns: 
```
    [ 1,  2,  3,  4 ]
A = [ 5,  6,  7,  8 ]
    [ 9, 10, 11, 12 ]
```
3. From array A show how to extract each of the following by scalar selection or slicing:
    * number 7
    * row 1
    * column 2
    * rows 2 and 3
    * values 7, 8, 11, and 12
4. Create the array B = 2*A - 8. From B, determine the following:
    * the sum of the row values
    * the sum of the column values
    * the cumulative sum of row values
    * the cumulative sum of column values
5. From array B, create new arrays containing the element-by-element:
    * natural logarithm
    * square root
    * square
    * absolute value
6. In 1992, Giancarlo Moschini and Karl Meilke published a paper to the Journal of Agricultural Economics. In this paper, they estimated linear demand and supply functions of pork in Canada. I have simplified the equations into the following format:                                                   
    >(Demand) Q = 286 - 20p

    >(Supply) Q = 88 + 40p

    We can write this in matrix notation as:

    $\begin{bmatrix}1 &  20\\\\1 & -40\end{bmatrix}\cdot\begin{bmatrix}Q\\\\p\end{bmatrix}=\begin{bmatrix}286\\\\88\end{bmatrix}$

    Using the tools provided in the lecture, solve for the equilibrium price and quantity.
