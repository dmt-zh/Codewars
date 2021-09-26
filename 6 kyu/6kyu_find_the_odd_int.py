# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    from collections import Counter
    cnt = Counter(seq)
    for k, v in cnt.items():
        if v % 2 != 0:
            return k