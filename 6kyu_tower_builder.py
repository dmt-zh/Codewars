# Build Tower by the following given argument: number of floors (integer and always greater than 0).
# for example, a tower of 3 floors looks like below:
# [
#   '  *  ', 
#   ' *** ', 
#   '*****'
# ]


def tower_builder(n_floors):
    res = []
    for i in range(1, n_floors*2, 2):
        res.append(('*' * i).center(n_floors*2 - 1))
    return res

print(tower_builder(4))