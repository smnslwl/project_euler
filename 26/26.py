"""
   A unit fraction contains 1 in the numerator. The decimal representation of
   the unit fractions with denominators 2 to 10 are given:

     1/2  =  0.5
     1/3  =  0.(3)
     1/4  =  0.25
     1/5  =  0.2
     1/6  =  0.1(6)
     1/7  =  0.(142857)
     1/8  =  0.125
     1/9  =  0.(1)
     1/10 =  0.1

   Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
   be seen that 1/7 has a 6-digit recurring cycle.

   Find the value of d < 1000 for which ^1/[d] contains the longest recurring
   cycle in its decimal fraction part.
"""

def recurring_cycle_len(d):
    """Return the length of the recurring cycle of decimals in 1/d"""
    for i in range(1, d):
        if 10 ** i % d == 1:
            return i
    return 0

if __name__ == '__main__':
    upper = 1000

    longest_len, longest_d = 0, 0
    for d in range(3, upper, 2):
        if recurring_cycle_len(d) > longest_len:
            longest_len = recurring_cycle_len(d)
            longest_d = d
    
    print(longest_d)

"""
NOTE:
Even numbers will not have any recurring decimals, they can be skipped.
"""
