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