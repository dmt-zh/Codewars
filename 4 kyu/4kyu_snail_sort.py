# Snail Sort
# Given an n x n array, return the array elements arranged from outermost
# elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]

# For better understanding, please follow the numbers of the next array consecutively:
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

# NOTE: The idea is not sort the elements from the lowest value to the highest;
# the idea is to traverse the 2-d array in a clockwise snailshell pattern.

# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

def snail(snail_map):
    if len(snail_map[0]) < 2:
        return snail_map[0]
    else:
        mtx = []
        num = len(snail_map)
        cnt = 1
        while cnt <= num ** 2:
            for i in range(num):
                for j in range(i, num-i):
                    mtx.append(snail_map[i][j])
                    cnt += 1
                for j in range(1+i, num-i):
                    mtx.append(snail_map[j][num-1-i])
                    cnt += 1
                for j in reversed(range(i, num-1-i)):
                    mtx.append(snail_map[num-1-i][j])
                    cnt += 1
                for j in reversed(range(1+i, num-1-i)):
                    mtx.append(snail_map[j][i])
                    cnt += 1
        return mtx