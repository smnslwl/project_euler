"""
   Using << names.txt >>, a 46K text file containing over five-thousand first
   names, begin by sorting it into alphabetical order. Then working out the
   alphabetical value for each name, multiply this value by its alphabetical
   position in the list to obtain a name score.

   For example, when the list is sorted into alphabetical order, COLIN, which
   is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
   COLIN would obtain a score of 938 × 53 = 49714.

   What is the total of all the name scores in the file?
"""

from os.path import dirname, abspath, join
from string import ascii_uppercase

def alpha_value(text):
    """Return the sum of alphabetical value for uppercase letters in text"""
    return sum(ascii_uppercase.index(c) + 1 for c in text if c.isupper())

if __name__ == '__main__':
    with open(join(dirname(abspath(__file__)), 'names.txt')) as f:
        names = sorted(x[1:-1] for x in f.read().split(','))
    
    total = sum((i + 1) * alpha_value(name) for i, name in enumerate(names))
    
    print(total)
