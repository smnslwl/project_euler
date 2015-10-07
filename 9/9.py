"""
   A Pythagorean triplet is a set of three natural numbers, a < b < c, for
   which,

                                a^2 + b^2 = c^2

   For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

   There exists exactly one Pythagorean triplet for which a + b + c = 1000.
   Find the product abc.
"""

def product_of_triplet_with_sum(n):
    for i in range(1, n // 2):
        for j in range(i, n - i):
            k = n - i - j
            product = i * j * k
            if i ** 2 + j ** 2 == k ** 2:
                return product

if __name__ == '__main__':
    triplet_sum = 1000
    
    print(product_of_triplet_with_sum(triplet_sum))
