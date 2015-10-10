"""
   An irrational decimal fraction is created by concatenating the positive
   integers:

                     0.123456789101112131415161718192021...

   It can be seen that the 12^th digit of the fractional part is 1.

   If d[n] represents the n^th digit of the fractional part, find the value
   of the following expression.

      d[1] × d[10] × d[100] × d[1000] × d[10000] × d[100000] × d[1000000]
"""

if __name__ == '__main__':
    indexes = 1, 10, 100, 1000, 10000, 100000, 1000000

    upper = 200000
    d = ''.join(str(i) for i in range(1, upper))
    product = 1
    for index in indexes:
        product *= int(d[index - 1])
    
    print(product)


"""
NOTE:
The list d needs to have a of minimum length 1000000, and it seems like
200000 is a big enough upper bound of numbers.
All in all a pretty naive and memory-heavy implementation.
"""
