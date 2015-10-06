"""
   2520 is the smallest number that can be divided by each of the numbers
   from 1 to 10 without any remainder.

   What is the smallest positive number that is evenly divisible by all of
   the numbers from 1 to 20?
"""

def prime_factors(n):
    """Generates the prime factors of n"""
    divisor = 2
    while divisor <= n:
        if not n % divisor:
            yield divisor
            n /= divisor
        else:
            divisor += 1

def highest_common_factor(m, n):
    """Returns the HCF/GCD of m and n"""
    while n:
        m, n = n, m % n
    return m

if __name__ == '__main__':
    lower, upper = 1, 20

    lcm = 1
    for i in range(lower, upper + 1):
        lcm = i * lcm / highest_common_factor(lcm, i)

    print(int(lcm))
