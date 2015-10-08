"""
   By starting at the top of the triangle below and moving to adjacent
   numbers on the row below, the maximum total from top to bottom is 23.

                                       3
                                      7 4
                                     2 4 6
                                    8 5 9 3

   That is, 3 + 7 + 4 + 9 = 23.

   Find the maximum total from top to bottom of the triangle below:

                {{ 18_input.txt }}

   NOTE: As there are only 16384 routes, it is possible to solve this problem
   by trying every route. However, Problem 67 is the same challenge with
   a triangle containing one-hundred rows; it cannot be solved by brute
   force, and requires a clever method! ;o)
"""

from os.path import dirname, abspath, join

if __name__ == '__main__':
    with open(join(dirname(abspath(__file__)), '18_input.txt')) as f:
        lines = f.read().splitlines()
    rows = [[int(y) for y in x.split()] for x in lines if x]

    for i in range(1, len(rows)):
        rows[i][0] += rows[i-1][0]    
        rows[i][-1] += rows[i-1][-1]
        for j in range(1, len(rows[i]) - 1):
            rows[i][j] += max(rows[i-1][j-1], rows[i-1][j])
    max_total = max(rows[-1])

    print(max_total)
