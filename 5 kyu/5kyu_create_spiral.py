# Your objective is to complete a function createSpiral(N) that receives an integer N and returns an NxN
# two-dimensional array with numbers 1 through NxN represented as a clockwise spiral.
# Return an empty array if N < 1 or N is not int / number
# Examples: N = 3 Output: [[1,2,3],[8,9,4],[7,6,5]]

def create_spiral(num):
    try:
        if num >= 1:
            mtx = [[0] * num for i in range(num)]
            cnt = 1
            for i in range(num):
                for j in range(i, num-i):
                    mtx[i][j] = cnt
                    cnt += 1
                for j in range(1+i, num-i):
                    mtx[j][num-1-i] = cnt
                    cnt +=1
                for j in reversed(range(i, num-1-i)):
                    mtx[num-1-i][j] = cnt
                    cnt += 1
                for j in reversed(range(1+i, num-1-i)):
                    mtx[j][i] = cnt
                    cnt +=1
            return mtx
        else:
            return []
    except:
        return []

print(create_spiral('s'))