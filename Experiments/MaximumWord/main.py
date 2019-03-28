import itertools
import random

from MPFFuns import circulant, MPF
from Utils.generators import generate_anticirculant_rand_word_mat
from Utils.words_matrices_utils import pwords, find_matrix_max_exponent, find_matrix_max_delta
from Word import Word as Wo, Word

W = generate_anticirculant_rand_word_mat(3,[20,-19,-1], 50)
W = [
    [Word(0, 20, 0, 0), Word(0, 0, 20, 0), Word(0,0,0,0)],
    [Word(0, 0, 20, 0), Word(0, 0, 0, 0),  Word(0,20,0,0)],
    [Word(0, 0, 0, 0),  Word(0, 20, 0, 0), Word(0,0,20,0)]
]
W = generate_anticirculant_rand_word_mat(6,[11,-13,7,-20,14,-3,], 20)
# [11,7,-14,-3] => 26 * 9 = 234 (sum of some abs)
# [11,-14,7,-3] => 36 * 9 = 324 (sum of all abs)
# [-14,11,7,-3] => 22 * 9 = 198 (sum of first and third abs)
# [-14,7,11,-3] => 26 * 9 = 234 (sum of first and thrid)
# [-20, 0,0, 21] =>  42 * 9 => 378 (sum of all)
# [-20, -19, 18, 22] => 42 * 9 => 378 (sum of second and forth + sum of all ofc)
# [-20, -19, 22, 18] => 43 * 9 => 387 (sum of first and third abs)
pwords(W)

x_try = [0, 3]
y_try = [0, 3]
max_delta = 0
iter = 0
best_x, best_y = 0, 0
best_lst = []

for x_for in itertools.product(x_try, repeat=6):
    for y_for in itertools.product(x_try, repeat=6):
        X = circulant(x_for)
        Y = circulant(y_for)
        res = MPF(X,W,Y)
        max_delta_loc = find_matrix_max_delta(res)
        if abs(max_delta_loc) > abs(max_delta):
            max_delta = max_delta_loc
            best_x = x_for
            best_y = y_for
            best_lst = [ (x_for, y_for)]
            print("new value found! => {}".format(max_delta))
        elif abs(max_delta_loc) == abs(max_delta):
            best_lst.append( (x_for, y_for))
            print("Candidate found! => {}".format((x_for, y_for)))
        iter += 1




print()
pwords(res)
