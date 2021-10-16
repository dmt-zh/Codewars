# Write a function that generates factors for a given number. The function takes
# an integer on the standard input and returns a list of integers. That list contains
# the prime factors in numerical sequence.

# Examples
# 1  ==>  []
# 3  ==>  [3]
# 8  ==>  [2, 2, 2]
# 9  ==>  [3, 3]
# 12 ==>  [2, 2, 3]

def prime_factors(x):
    if x in [0, 1]:
        return []
    if x >= 2:
        factors = []
        for num in range(2, int(x**0.5) + 1):
            while x % num == 0:
                factors.append(num)
                x //= num
        if x != 1:
            factors.append(x)
    return factors