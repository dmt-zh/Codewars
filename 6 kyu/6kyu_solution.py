# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the missing
# second character of the final pair with an underscore ('_').

# Examples:
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

from itertools import zip_longest
def solution(s):
    return list(map(''.join, zip_longest(s[::2], s[1::2], fillvalue='_')))
