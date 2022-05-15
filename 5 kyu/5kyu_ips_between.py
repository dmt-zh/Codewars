# Implement a function that receives two IPv4 addresses, and returns the number of addresses
# between them (including the first one, excluding the last one).
# All inputs will be valid IPv4 addresses in the form of strings. The last address will always
# be greater than the first one.


import numpy as np
def ips_between(start, end):
    x = np.array([int(i) for i in start.split('.')])
    y = np.array([int(j) for j in end.split('.')])
    msk = [256 ** 3, 256 ** 2, 256, 1]
    ip1 = np.sum(x * msk) + 1
    ip2 = np.sum(y * msk) + 1
    return ip2 - ip1