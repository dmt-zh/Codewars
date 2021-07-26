# Finish the solution so that it takes an input n (integer) and returns a string that is the
# decimal representation of the number grouped by commas after every 3 digits.
#        1  ->           "1"
#       10  ->          "10"
#      100  ->         "100"
#     1000  ->       "1,000"

def group_by_commas(num):
    if len(str(num)) > 3:
        num = str(num)
        res = ''
        for i in range(len(str(num)), 0, -1):
            if i % 3 == 0:
                res += ','
            res += num[len(num) - i]
        return res.lstrip(',')
    return str(num)
