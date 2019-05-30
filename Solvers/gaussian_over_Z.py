import math
from fractions import gcd as mathgcd
import numpy as np
def numpy_set_gcd(a):
    gcd = a[0]
    for i in a[1:]:
        if i != 0:
            gcd = i
            break
    for i in a[1:]:
        if i == 0:
            continue
        gcd = mathgcd(abs(i), abs(gcd))
        if gcd == 1:
            return 1
    if math.isnan(gcd):
        return 1
    return max(1,gcd)
def solve_linsys_Z(sys, b):
    # let's solve it

    for iter in range(8):#sys.shape[0]):
        # check if swap is needed
        if sys[iter,iter] == 0:
            # swap quickly
            swap_index = None
            for i in range(iter, sys.shape[0]):
                if sys[i,iter] != 0:
                    swap_index = i
                    break
            if swap_index is None:
                raise Exception("Whole {} column is populated with zeros! Exiting".format(iter))

            sys[[swap_index,iter]] = sys[[iter, swap_index]]
        for i in range(8):#sys.shape[0]):
            if i == iter or sys[i,iter] == 0:
                continue
            sys[i] = (sys[i, iter]) * sys[iter] - (sys[iter, iter]) * sys[i]
            set_gcd = numpy_set_gcd(sys[i])
            sys[i] /= set_gcd

    return sys


