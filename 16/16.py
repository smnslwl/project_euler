"""
   2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

   What is the sum of the digits of the number 2^1000?
"""

if __name__ == '__main__':
    a, b = 2, 1000
    number = a ** b
    
    digits = []
    while number:
        digits.append(number % 10)
        number //= 10
    sum_of_digits = sum(digits)

    print(sum_of_digits)

"""
ONE-LINER

    print(sum(int(x) for x in str(2 ** 1000)))

"""
