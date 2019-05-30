import random

from MPFFuns import circulant, MPF
from Utils.generators import generate_anticirculant_rand_word_mat
from Utils.words_matrices_utils import pwords, get_lambda_mat, plambda
from Word import Word as Wo
W = [
[Wo(0, 15, 24, 0 ), Wo( 1, 13, 2, 0 ), Wo(0, 8, 13, 0 ), Wo( 0, 8, 1, 0 )],
[Wo(0, 18, 8, 0  ), Wo(  1, 0, 4, 0), Wo( 0, 7, 0, 0 ), Wo( 0, 19, 28, 0 )] ,
[Wo(1, 20, 25, 1 ), Wo( 0, 18, 11, 0 ), Wo(0, 16, 25, 0 ), Wo( 1, 17, 6, 0 )] ,
[Wo(1, 22, 14, 0 ), Wo( 0, 13, 22, 0 ), Wo(0, 24, 15, 1 ), Wo( 1, 14, 18, 0 )]
]

print("Original matrix's delta = >")
plambda(W)

X = circulant([8,8,8,8])
Y = circulant([8,8,8,8])
#random.seed(20)
W = generate_anticirculant_rand_word_mat(4,[6,2,-2,-6], 50)

pwords(W)

X = circulant([2,5,7,8])
Y = circulant([3,7,4,2])



res = MPF(X,W,Y)

print("Deltas -> ")
plambda(res)