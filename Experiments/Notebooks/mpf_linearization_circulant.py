
# coding: utf-8

# In[187]:


# imports and helper classes
import copy
import numpy as np
import random
import re as rd
import numpy as np
from IPython.core.display import display
from sympy import *
from sympy import expand
import sympy
from sympy import Matrix, pprint,symbols
from numpy.linalg import matrix_rank
from sympy.interactive.printing import init_printing

from Solvers.gaussian_over_Z import solve_linsys_Z

init_printing(use_unicode=False, wrap_line=False)

import matplotlib.pyplot as plt
REDUCTION_P = 3

class Word:
    def __init__(self, b, i, j, a):
        self.beta = b
        self.i = i
        self.j = j
        self.alpha = a
    def max(self):
        return max(self.beta, self.i, self.j, self.alpha)

    def get_lambda(self):
        return self.beta + self.j- self.i - self.alpha
    def get_miu(self):
        return (self.beta + self.i + self.j + self.alpha) % (2 * REDUCTION_P)
    def print(self):
        return "[" + str(self.beta) + ", " + str(self.i) + ", " +  str(self.j) + ", " + str(self.alpha) + "]"

    def __str__(self):
        return "[" + str(self.beta) + ", " + str(self.i) + ", " +  str(self.j) + ", " + str(self.alpha) + "]"

    def reduce_two(self, j, i, mode=0):
        mino = min(i, j)
        maxo = max(i, j)
        lam = 0
        if i == j:
            lam = max(0, int((maxo - 2) / 3))
        else:
            lam = max(0, int((mino - 1) / 3))
        return (i - lam * 3, j - lam * 3)

    def medial_reduce(self):
        if self.beta == 0 and self.i == 0 and self.j > 0:
            self.beta += 1
            self.j -= 1

        if self.alpha == 0 and self.j == 0 and self.i > 0:
            self.alpha += 1
            self.i -= 1

        if self.alpha == 0 and self.beta == 0:
            reduced = self.reduce_two(self.j, self.i)
            self.i = reduced[0]
            self.j = reduced[1]
        elif self.alpha == 1 and self.beta == 1:
            reduced = self.reduce_two(self.j, self.i)
            self.i = reduced[0]
            self.j = reduced[1]
        elif self.alpha == 0 and self.beta == 1:
            if self.i >= REDUCTION_P + 2 and self.beta + self.j >= REDUCTION_P + 1:
                reduced = self.reduce_two(self.j, self.i)
                self.i = reduced[0]
                self.j = reduced[1]
        elif self.alpha == 1 and self.beta == 0:
            if self.j >= REDUCTION_P + 2 and self.alpha + self.i >= REDUCTION_P + 1:
                reduced = self.reduce_two(self.j, self.i)
                self.i = reduced[0]
                self.j = reduced[1]

    def is_empty(self):
        return self.beta == 0 and self.i == 0 and self.j == 0 and self.alpha == 0

    def __pow__(self, power):
        # binary exponentiation
        if power == 0:
            return Word(0,0,0,0)

        result = copy.deepcopy(self)
        current = copy.deepcopy(self)

        power -= 1

        while power > 0:
            if power & 1 == 1:
                result = (current * result)
                result.medial_reduce()

            current = (current * current)
            current.medial_reduce()

            power = int(power / 2)
        return result

    def __mul__(self, other):
        return Word(self.beta, self.i + self.alpha + other.i, self.j + other.beta + other.j, other.alpha)

def generate_anticirculant_rand_word_mat(dim, lambda_req, max_val = 50):
    res =[ [[] for j in range(dim)] for i in range(dim) ]
    for i in range(dim):
        for j in range(dim):
            beta = random.randint(0, 1)
            ii = random.randint(0, max_val)
            jj = random.randint(0, max_val)
            alpha = random.randint(0, 1)

            diff = (beta + jj) - (alpha + ii)
            required = lambda_req[ (j + i + dim ) % dim] - diff

            if required >= 0:
                jj += required
            else:
                ii += -required

            res[i][j] = Word(beta, ii, jj, alpha)
            res[i][j].medial_reduce()
    return res

def circulant(basis):
    """

    :param basis:
    :return:
    """
    res = []
    N = len(basis)
    for i in range(N):
        curr = []
        for j in range(N):
            curr.append(basis[ (j - i + N) % N ])
        res.append(curr)
    return res

def MPF(X, W, Y):
    """
    Compute MPF
    :param X:
    :param W:
    :param Y:
    :return:
    """
    result = [None] * len(X)
    for i in range(len(X)):
        result[i] = [None] * len(X)
        for j in range(len(X[i])):
            for k in range(len(X)):
                for l in range(len(X[k])):
                    if k == l and l == 0:
                        result[i][j] = W[k][l] ** (X[i][k] * Y[l][j])
                    else:
                        result[i][j] = result[i][j] * (W[k][l] ** (X[i][k] * Y[l][j]))
                    result[i][j].medial_reduce()
    return result

def get_delta_mat(words):
    res = [ [word.get_lambda() for word in row] for row in words]
    return res

def get_sigma_mat(words):
    res = [ [word.get_miu() for word in row] for row in words]
    return res


# In[229]:


N = 4
W = generate_anticirculant_rand_word_mat(4,[6,7,-2,-3], 50)
deltaW = np.array(get_delta_mat(W))

X = circulant([1, 5, 7, 3])
Y = circulant([3, 3, 6, 1])

res = MPF(X,W,Y)

print("delta(W) => \n {}".format(deltaW))


# In[230]:


deltas = np.array(get_delta_mat(res))
sigmas = np.array(get_sigma_mat(res))


# In[231]:


print(deltas)
print(sigmas)


# In[234]:


# construct first block n x n, assume that z_{n+1:} are zeros (so x{1:} are zeros)

def init_x(y, x):
    return "x_"+ str((x - y + N) % N)

def init_y(y, x):
    return "y_"+str((x - y + N) % N)

W_lambda = Matrix([ # circulant yelds fine
    ["w_00", "w_01",    "w_02", "w_03"],
    ["w_01", "w_02",    "w_03", "w_00"],
    ["w_02", "w_03",    "w_00", "w_01"],
    ["w_03", "w_00",    "w_01", "w_02"]
])

X = Matrix(N, N, init_x)
Y = Matrix(N, N, init_y)
matmul = X * W_lambda * Y
res_mat = sympy.expand(matmul)
#res_mat = matmul
#display(res_mat)

coeffs = {}

coeffs_mat = np.zeros((N*N, N*N))

dicto = {}
dicto_org = {}

for y in range(N):
    for x in range(N):
        sums = res_mat[y,x]
        for arg in sums._sorted_args:
            num = 1
            stre = ""
            w_index = 0
            for inarg in arg._sorted_args:
                if inarg.has(sympy.Integer):
                    num = int(inarg)
                elif "w" in inarg.name:
                    num = str(num) + "*" + inarg.name
                    w_index = [int(num) for num in rd.findall(r"\d+", inarg.name)]
                else:
                    stre+=inarg.name+"_"
            numbs = [int(num) for num in rd.findall(r"\d+", stre)]

            if not isinstance(w_index, list) or len(w_index) <= 1:
                w_index = [0, w_index]
            #coeffs[str(y)+str(x)+stre] = num
            #coeffs_w[y * N + x , numbs[0] * N + numbs[1] ] = num
            dicto[(y*N + x , numbs[0] * N + numbs[1])] = sympy.var(num)
            dicto_org[(y*N + x , numbs[0] * N + numbs[1])] = (w_index[0], w_index[1])
iter = 0
coeffs_w = Matrix(N*N,N*N,lambda x,y: dicto.get((x, y), 0))
print(dicto_org)
# plug-in from delta
for key, val in dicto.items():
    print("{} -> {}".format(val, deltaW[dicto_org[key][0], dicto_org[key][1]]))
    coeffs_w = coeffs_w.subs({val:deltaW[dicto_org[key][0], dicto_org[key][1]]})
#display(coeffs_w.subs({dicto[(1,4)]:33333}))
print("Solving gaussian .. ")
linearized_arr = np.array(coeffs_w).astype(object)
linearized_arr = np.hstack((linearized_arr[:4], np.expand_dims(deltas[0,:],1)))
ans = solve_linsys_Z(linearized_arr, 1)
display(coeffs_w)
#display(coeffs)

