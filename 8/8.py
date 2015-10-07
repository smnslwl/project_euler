"""
   The four adjacent digits in the 1000-digit number that have the greatest
   product are 9 × 9 × 8 × 9 = 5832.

                {{ 8_input.txt }}

   Find the thirteen adjacent digits in the 1000-digit number that have the
   greatest product. What is the value of this product?
"""

from os.path import dirname, abspath, join

if __name__ == '__main__':
    
    digits = 13
    with open(join(dirname(abspath(__file__)), '8_input.txt')) as f:
        number = ''.join(f.read().splitlines())
    
    greatest_product = 0
    for i in range(len(number) - digits + 1):
        product = 1
        for j in range(i, i + digits):
            product *= int(number[j])
        if product > greatest_product:
            greatest_product = product
    
    print(greatest_product)
