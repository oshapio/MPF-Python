from fractions import gcd


def solve_linsys_Z(sys, b):
    # let's solve it

    for iter in range(3):#sys.shape[0]):
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
        for i in range(4):#sys.shape[0]):
            if i == iter:
                continue
            multiplier =  (sys[i,iter] * sys[iter,iter]) #// gcd(sys[i,iter], sys[iter,iter])
            sys[i] = (multiplier // sys[i, iter]) * sys[i] -  (multiplier // sys[iter, iter]) * sys[iter]
    return sys


