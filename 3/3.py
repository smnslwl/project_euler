"""
   The prime factors of 13195 are 5, 7, 13 and 29.

   What is the largest prime factor of the number 600851475143?
"""

def largest_prime_factor(n):
    """Returns the largest prime factor of n"""
    factor = n
    divisor = 2
    while divisor * divisor < factor:
        while not factor % divisor:
            if factor == divisor:
                break
            factor /= divisor
        divisor += 1
    return factor

if __name__ == '__main__':
    number = 600851475143

    print(int(largest_prime_factor(number)))
