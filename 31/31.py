"""
   In England the currency is made up of pound, £, and pence, p, and there
   are eight coins in general circulation:

     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

   It is possible to make £2 in the following way:

     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

   How many different ways can £2 be made using any number of coins?
"""

if __name__ == '__main__':
    coins = 1, 2, 5, 10, 20, 50, 100, 200
    amount = 200
    
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            ways[i] += ways[i - coin]

    print(ways[amount])

"""
NOTES:
Dynamic Programming is used to solve this problem.
 * There is only one way to give change to 0 using any coins.
 * There is only one way to give change to any amount using only 1p coins.
 * A coin can only add up to amounts equal to or more than itself.
"""
