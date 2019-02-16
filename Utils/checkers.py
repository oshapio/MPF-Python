
def check_anticirculant(words):
    basis = words[0]

    N = len(words)
    for i in range(N):
        for j in range(N):
            if words[i][j] != basis[ (j + i + N ) % N ]:
                return False
    return True
