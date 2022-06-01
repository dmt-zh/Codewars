# Extra perfect number is the number that first and last bits are set bits.
# Given a positive integer N. Return the extra perfect numbers in range from 1 to N.
# extraPerfect(3)  ==>  return {1,3}

# Explanation:
# (1)10 =(1)2
# First and last bits as set bits.
# (3)10 = (11)2
# First and last bits as set bits.

def extra_perfect(n):
    return [i for i in range(1, n + 1) if bin(i)[2] == '1' and bin(i)[-1] == '1']