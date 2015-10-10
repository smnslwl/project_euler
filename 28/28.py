"""
   Starting with the number 1 and moving to the right in a clockwise
   direction a 5 by 5 spiral is formed as follows:

                                 21 22 23 24 25
                                 20  7  8  9 10
                                 19  6  1  2 11
                                 18  5  4  3 12
                                 17 16 15 14 13

   It can be verified that the sum of the numbers on the diagonals is 101.

   What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
   formed in the same way?
"""

if __name__ == '__main__':
    upper = 1001

    sum_diagonals = 1
    for i in range(3, upper + 1, 2):
        for j in range(4):
            sum_diagonals += i ** 2 - j * (i - 1)
    
    print(sum_diagonals)
    
"""
NOTE:
The diagonals for a 5*5 grid are: 1, 3, 5, 7, 9, 13, 17, 21, 25.

1*1: 1
3*3: 9, 7, 5, 3 --> 3^2, 3^2 - (3-1), 3^2 - 2*(3-1), 3^2 - 3*(3-1)
5*5: 25, 21, 17, 13 --> same as above 

For a n*n grid, the kth corner (where 0 <= k < 4) is given by:
    n^2* k * (n - 1)
"""
