"""
   The n^th term of the sequence of triangle numbers is given by, t[n] =
   ½n(n+1); so the first ten triangle numbers are:

                    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

   By converting each letter in a word to a number corresponding to its
   alphabetical position and adding these values we form a word value. For
   example, the word value for SKY is 19 + 11 + 25 = 55 = t[10]. If the word
   value is a triangle number then we shall call the word a triangle word.

   Using << words.txt >>, a 16K text file containing nearly two-thousand common
   English words, how many are triangle words?
"""

from math import sqrt
from os.path import dirname, abspath, join
from string import ascii_uppercase

def alpha_value(text):
    """Return the sum of alphabetical value for uppercase letters in text"""
    return sum(ascii_uppercase.index(c) + 1 for c in text if c.isupper())

def is_triangle(t):
    """Return true if t is a triangle number"""
    for n in range(1, int(sqrt(2 * t)) + 2):
        if 2 * t == n * (n + 1):
            return True
    return False

if __name__ == '__main__':
    with open(join(dirname(abspath(__file__)), 'words.txt')) as f:
        words = (x[1:-1] for x in f.read().split(','))

    t_words = sum(1 for w in words if is_triangle(alpha_value(w)))
    
    print(t_words)


"""
NOTE:
A triangle number must be for the form n(n+1)/2 = t, or 2t = n(n+1).
Hence the upper bound for n to see if t is a triangle number will be
less than the square root of 2t.
"""
