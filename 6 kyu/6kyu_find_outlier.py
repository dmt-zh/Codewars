# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
# Write a method that takes the array as an argument and returns this "outlier" N.
# [2, 4, 0, 100, 4, 11, 2602, 36] => Should return: 11 (the only odd number)


def find_outlier(integers):
    a = [i for i in integers if i % 2 != 0]
    b = [j for j in integers if j % 2 == 0]
    if len(a) == 1:
        return a[0]
    return b[0]

n = [2, 4, 0, 100, 4, 11, 2602, 36]
print(find_outlier(n))
