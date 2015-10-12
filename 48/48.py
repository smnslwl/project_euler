"""
   The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

   Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

if __name__ == '__main__':
    upper = 1000
    digits = 10
    
    sum_series = 0
    for i in range(1, upper + 1):
        sum_series += i ** i
    last_n_digits = str(sum_series)[-digits:]

    print(last_n_digits)
