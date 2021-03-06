# A format for expressing an ordered list of integers is to use a comma separated list of either:
# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.
# The range includes all integers in the interval including both endpoints. It is not considered a range unless it
# spans at least 3 numbers. For example "12,13,15-17". Complete the solution so that it takes a list of integers in
# increasing order and returns a correctly formatted string in the range format.
# Example:
# solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"

def solution(args):
    
    args.append(args[-1]+2)
    ans = ''
    res = []
    start = args[0]
    res.append(start)
    
    for i in range(1, len(args)):
        if len(range(start, args[i])) == 1:
            res.append(args[i])
            start = args[i]
        else:
            if len(res) > 2:
                ans += f'{str(res[0])}-{str(res[-1])},'
                start = args[i]
                res = [start]
            elif len(res) == 2:
                ans += f'{str(res[0])},{str(res[-1])},'
                start = args[i]
                res = [start]
            else:
                ans += f'{str(start)},'
                start = args[i]
                res = [start]
    return ans[:-1]
