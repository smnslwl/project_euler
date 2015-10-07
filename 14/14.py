"""
   The following iterative sequence is defined for the set of positive
   integers:

   n → n/2 (n is even)
   n → 3n + 1 (n is odd)

   Using the rule above and starting with 13, we generate the following
   sequence:

                   13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

   It can be seen that this sequence (starting at 13 and finishing at 1)
   contains 10 terms. Although it has not been proved yet (Collatz Problem),
   it is thought that all starting numbers finish at 1.

   Which starting number, under one million, produces the longest chain?

   NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def collatz_sequence(n):
    """Generates the Collatz sequence for n"""
    yield n
    while n > 1:
        n = 3 * n + 1 if n % 2 else n // 2
        yield n

def collatz_sequence_length(n):
    """Returns the length of the collatz sequence"""
    return sum(1 for _ in collatz_sequence(n))

if __name__ == '__main__':
    upper = 1000000

    max_number = max(range(upper), key=collatz_sequence_length)
    
    print(max_number)

"""
ALTERNATE SOLUTION
    
    upper = 1000000
    max_length, max_number = 0, 0
    for n in range(1, upper):
        c_chain = [n]
        while (n > 1):
            n = 3 * n + 1 if n % 2 else n // 2
            c_chain.append(n)
        if len(c_chain) > max_length:
            max_length, max_number = len(c_chain), c_chain[0]
    print(max_number)
    
"""
