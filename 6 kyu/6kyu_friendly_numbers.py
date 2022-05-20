# The Abundancy (A) of a number n is defined as:
# (sum of divisors of n) / n

# For example:
# A(8) = (1 + 2 + 4 + 8) / 8 = 15/8
# A(25) = (1 + 5 + 25) / 25  = 31/25

# Friendly Pairs are pairs of numbers (m, n), such that their abundancies are equal: A(n) = A(m).
# Write a function that returns "Friendly!" if the two given numbers are a Friendly Pair. Otherwise
# return their respective abundacies as strings separated by a space, e.g. "1 15/8"

# Notes:
# All fractions must be written in their most reduced form (e.g. 2/3 instead of 8/12)
# Every number that is being checked is under 2400
# Floats should be left on without rounding when you compare the abundancies of the two numbers


from fractions import Fraction
def friendly_numbers(n, m):
    n_sum = sum([i for i in range(1, n + 1) if not n % i])
    m_sum = sum([i for i in range(1, m + 1) if not m % i])

    if n_sum/n == m_sum/m:
        return f'Friendly!'
    else:
        return ' '.join([str(Fraction(n_sum, n)), str(Fraction(m_sum, m))])