

def get_lambda_mat(words):
    res = []
    for i in range(len(words)):
        curr = []
        for j in range(len(words[i])):
            curr.append(words[i][j].get_lambda())
        res.append(curr)
    return res
def find_matrix_max_exponent(words_mat):
    max_exp = 0
    for i in range(len(words_mat)):
        for j in range(len(words_mat[i])):
            max_exp = max(max_exp, words_mat[i][j].max())
    return max_exp
def find_matrix_max_delta(words_mat):
    max_delta = 0
    for i in range(len(words_mat)):
        for j in range(len(words_mat[i])):
            max_delta = max(max_delta, words_mat[i][j].get_lambda())
    return max_delta
def get_miu_mat(words):
    res = []
    for i in range(words):
        curr = []
        for j in range(words[i]):
            curr.append(words[i][j].get_miu())
        res.append(curr)
    return res

def pwords(words):
    for i in range(len(words)):
        for j in range(len(words[i])):
            print(words[i][j].print() + ", ", end='')
        print()

def plambda(words, disp=True):
    for i in range(len(words)):
        print("[ ",end='')
        for j in range(len(words[i])):
            print(str(words[i][j].get_lambda()) + ", ", end='')
        print("]")

def pmiu(words):
    for i in range(len(words)):
        print("[ ",end='')
        for j in range(len(words[i])):
            print(str(words[i][j].get_miu()) + ", ", end='')
        print("]")

def pmod_mat(mat, mod):
    for i in range(len(mat)):
        print("[ ", end='')
        for j in range(len(mat[i])):
            print(str(mat[i][j] % mod) + ", ", end='')
        print("]")
