import re

import numpy as np
import sympy
from numpy.linalg import matrix_rank
from sympy.interactive.printing import init_printing
init_printing(use_unicode=False, wrap_line=False)
from sympy import Matrix, pprint
import matplotlib.pyplot as plt

N = 3 # matrix dimension

def init_x(y, x):
    return "x_"+ str((x - y + N) % N)

def init_y(y, x):
    return "y_"+str((x - y + N) % N)


X = Matrix(N, N, init_x)



W_lambda = Matrix([
    [5,4],
    [10,8],
])

W_lambda = Matrix([
    ["w_1", "w_2"],
    ["c*w_1","c*w_2"],
])
W_lambda = Matrix([ # circulant yelds fine
    ["w_11", "w_12",    "w_13"],
    ["w_12", "w_13",    "w_11"],
    ["w_13", "w_11",    "w_12"]
])

W_lambda = Matrix([ # default
    ["w_11", "w_12",    "w_13"],
    ["w_21", "w_22",    "w_23"],
    ["w_31", "w_32",    "w_33"]
])

W_lambda = Matrix([
    ["w_11", "w_12",    "w_13"],
    ["w_21", "w_22",    "w_23"],
    ["w_31", "w_32",    "w_33"]
])


Y = Matrix(N, N, init_y)
matmul = X * W_lambda * Y

# display det
print("Determinant is : ")
print();print()
#pprint(sympy.simplify(sympy.det(matmul)))
res_mat = sympy.expand(matmul)

pprint(res_mat)

coeffs = {}

coeffs_mat = np.zeros((N*N, N*N))



dicto = {}

for y in range(N):
    for x in range(N):
        sums = res_mat[y,x]
        for arg in sums._sorted_args:
            num = 1
            stre = ""
            for inarg in arg._sorted_args:
                if inarg.has(sympy.Integer):
                    num = int(inarg)
                elif "w" in inarg.name:
                    num = str(num) + "*" + inarg.name
                else:
                    stre+=inarg.name+"_"
            numbs = [int(num) for num in re.findall(r"\d+", stre)]
            #coeffs[str(y)+str(x)+stre] = num
            #coeffs_w[y * N + x , numbs[0] * N + numbs[1] ] = num
            dicto[(y*N + x , numbs[0] * N + numbs[1])] = num
iter = 0
coeffs_w = Matrix(N*N,N*N,lambda x,y: dicto[(x, y)])

#print("Symbolic determinant is - " + str(sympy.det(coeffs_w)))
#print("Symbolic rank is - " + str(matrix_rank(coeffs_w)))


#
#for key, val in coeffs.items():
#    y,x = int(iter / (N*N)), iter % (N*N)
#    coeffs_mat[y,x]=val
#    iter += 1

print("rank is - " + str(matrix_rank(coeffs_mat)))

print("determinant is - " + str(np.linalg.det(coeffs_mat)))
#pprint(res_mat)
#sympy.preview(res_mat,mat_str='matrix')

sympy.preview(coeffs_w,mat_str='matrix')
plt.imshow(coeffs_mat)
plt.show()

exit(1)
pprint(X)
print()
pprint(Y)

print()
print()
pprint(res_mat)