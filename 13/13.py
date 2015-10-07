"""
   Work out the first ten digits of the sum of the following one-hundred
   50-digit numbers.
   
                {{ input_13.txt }}

"""

from os.path import dirname, abspath, join

if __name__ == '__main__':
    n = 10
    with open(join(dirname(abspath(__file__)), '13_input.txt')) as f:
        numbers = [int(x) for x in f.read().splitlines()]
    
    sum_of_numbers = sum(numbers)
    first_n_digits = int(str(sum_of_numbers)[:n])
    
    print(first_n_digits)


"""
ONE-LINER

    print(str(sum([int(x) for x in open('13_input.txt').splitlines()]))[:10])

"""
