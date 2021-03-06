# For a given list of digits 0 to 9, return a list with the same digits in the same order,
# but with all 0s paired. Pairing two 0s generates one 0 at the location of the first one.

# Examples
# input: [0, 1, 0, 2]
# paired: ^-----^
#     -> [0, 1,   2]
#   kept: ^

# input: [0, 1, 0, 0]
# paired: ^-----^
#     -> [0, 1,    0]

# Notes
# Pairing happens from left to right. For each pairing, the second 0 will always be paired towards the first ( right to left ).
# 0s generated by pairing can NOT be paired again.

def pair_zeros(arr):
    bitwise = 0
    return [i for i in arr if i or (bitwise := bitwise^1)]