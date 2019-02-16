import itertools
import random

from MPFFuns import circulant, MPF
from Utils.generators import generate_anticirculant_rand_word_mat
from Utils.words_matrices_utils import pwords, find_matrix_max_exponent, find_matrix_max_delta
from Word import Word as Wo, Word

W = generate_anticirculant_rand_word_mat(3,[20,-19,-1], 50)
W = [
    [Word(0, 20, 0, 0), Word(0, 0, 20, 0), Word(0,0,0,0)],
    [Word(0, 0, 20, 0), Word(0, 0, 0, 0), Word(0,20,0,0)],
    [Word(0, 0, 0, 0), Word(0, 20, 0, 0), Word(0,0,20,0)]
]
W = generate_anticirculant_rand_word_mat(3,[14,-5,-8], 20)


pwords(W)


x_try = range(0, 4)
y_try = range(0, 4)
max_delta = 0
iter = 0
best_x, best_y = 0,0
for x_for in itertools.product(x_try, repeat=3):
    for y_for in itertools.product(x_try, repeat=3):
        X = circulant(x_for)
        Y = circulant(y_for)
        res = MPF(X,W,Y)
        max_delta_loc = find_matrix_max_delta(res)
        if max_delta_loc > max_delta:
            max_delta = max_delta_loc
            best_x = x_for
            best_y = y_for
        iter += 1




print()
pwords(res)
