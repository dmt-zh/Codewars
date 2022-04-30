# Given a varying number of integer arguments, return the digits that are not present in any of them.

# Example:
# [12, 34, 56, 78]  =>  "09"
# [2015, 8, 26]     =>  "3479"

# Note: the digits in the resulting string should be sorted.

def unused_digits(*numbers):
    all_numbers = set([int(i) for i in range(10)])
    nums = [int(i) for i in str(numbers) if i.isdigit()]
    return ''.join(map(str, sorted(all_numbers.difference(nums))))