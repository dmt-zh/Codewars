# There is an array with some numbers. All numbers are equal except for one. Try to find it.
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2

def find_uniq(arr):
    from collections import Counter
    counter = Counter(arr)
    return counter.most_common()[:-2:-1][0][0]

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
