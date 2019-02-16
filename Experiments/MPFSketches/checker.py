import pprint

import Constants
from MPFFuns import circulant, MPF
from Utils.checkers import check_anticirculant
from Utils.generators import generate_anticirculant_rand_word_mat
from Utils.words_matrices_utils import pwords, plambda, pmiu, pmod_mat, get_lambda_mat
from Word import Word

X = circulant([20, 20, 20])
Y = circulant([20, 20, 20])

print("X mod p mat:")
pmod_mat(X, Constants.REDUCTION_P)
print("Y mod p mat:")
pmod_mat(Y, Constants.REDUCTION_P)

# lets search for a word that would make this condition break?
counter = 0
for i in range(100000):
    rand_word = generate_anticirculant_rand_word_mat(3, [1, 3, -7])
    # check
    lambda_mat = get_lambda_mat(rand_word)
    if check_anticirculant(lambda_mat) != True:
        print("BAD ! ")
    if check_anticirculant(rand_word) != True:
        counter += 1
        #print("bad mat is : ")
        #pwords(rand_word)
        #print("bad!")

print("generated matrix:")
plambda(rand_word)



asd = 5

W = [
    [Word(0, 2, 3, 0), Word(0, 6, 9, 0), Word(1, 14, 6, 0)],
    [Word(0, 3, 6, 0), Word(0, 9, 3, 1), Word(1, 3, 3, 0)],
    [Word(1, 17, 9, 0), Word(0, 2, 3, 0), Word(1, 1, 4, 1)]
]
print("Initial lambda matrix:")
plambda(W)

print("Initial miu matrix:")
pmiu(W)

res = MPF(X, W, Y)
print("Resulting words matrix:")
pwords(res)

print("Resulting lambda matrix:")
plambda(res)

print("Resulting miu matrix:")
pmiu(res)


