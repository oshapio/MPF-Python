from MPFFuns import circulant, MPF
from Utils.generators import generate_anticirculant_rand_word_mat
from Utils.words_matrices_utils import pwords

max_W = generate_anticirculant_rand_word_mat(3, [20, 20, 20])
X = circulant([20,20,20])
Y = circulant([20,20,20])

res = MPF(X,max_W,Y)

pwords(res)
