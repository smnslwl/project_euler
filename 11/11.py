"""
   In the 20×20 grid below, four numbers along a diagonal line have been
   marked in red.

                {{ 11_input.txt }}

   The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

   What is the greatest product of four adjacent numbers in the same
   direction (up, down, left, right, or diagonally) in the 20×20 grid?
"""

from os.path import dirname, abspath, join
from itertools import chain

def prod(iterable):
    """Returns the accumulated product of the iterable"""
    product = 1
    for x in iterable:
        product *= x
    return product

if __name__ == '__main__':
    n = 4
    with open(join(dirname(abspath(__file__)), '11_input.txt')) as f:
        lines = f.read().splitlines()
    grid = [[int(y) for y in x.split()] for x in lines]
    rs, cs = len(grid), len(grid[0])

    horz = (grid[r][c:c+n] 
            for r in range(rs) for c in range(cs - n + 1))
    vert = ([grid[r + i][c] for i in range(n)] 
            for c in range(cs) for r in range(rs - n + 1))
    dg_l = ([grid[r + i][c + i] for i in range(n)]
            for r in range(rs - n + 1) for c in range(cs - n + 1))
    dg_r = ([grid[r + i][c - i] for i in range(n)]
            for r in range(rs - n + 1) for c in range(n - 1, cs))

    greatest_product = max(map(prod, chain(horz, vert, dg_l, dg_r)))
    
    print(greatest_product)
