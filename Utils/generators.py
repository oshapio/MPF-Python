import random

from Word import Word
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
def generate_rand_word_mat(dim, max_val = 20):
    res = [ [ [] for j in range(dim)] for i in range(dim)]
    for i in range(dim):
        for j in range(dim):
            beta = random.randint(0, 1)
            ii = random.randint(0, max_val)
            jj = random.randint(0, max_val)
            alpha = random.randint(0, 1)

            res[i][j] = Word(beta, ii, jj, alpha)
            res[i][j].medial_reduce()
    return res