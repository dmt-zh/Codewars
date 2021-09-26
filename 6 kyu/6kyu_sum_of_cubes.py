# The task is to find, or not, the "cubic" numbers in the string and then to make the sum of these "cubic"
# numbers found in the string, if any, and to return a string such as:
# s = "aqdf&0#1xyz!22[153(777.777" the groups of at most 3 digits are 0 and 1 (one digit), 22 (two digits), 153, 777, 777 (3 digits)
# Only 0, 1, 153 are cubic and their sum is 154 Return: "0 1 153 154 Lucky"

def is_sum_of_cubes(s):
    from re import findall
    nums = findall('\d{1,3}', s)
    cub_nums = [i for i in nums if sum(int(j)**3 for j in i) == int(i)]
    if not cub_nums:
        return 'Unlucky'
    else:
        return ' '.join(cub_nums + [str(sum(map(int, cub_nums))), "Lucky"])

a = "aqdf&0#1xyz!22[153(777.777"
print(is_sum_of_cubes(a))