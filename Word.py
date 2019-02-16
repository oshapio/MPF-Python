import copy

import Constants
class Word:
    def __init__(self, b, i, j, a):
        self.beta = b
        self.i = i
        self.j = j
        self.alpha = a
    def max(self):
        return max(self.beta, self.i, self.j, self.alpha)

    def get_lambda(self):
        return self.beta + self.j- self.i - self.alpha
    def get_miu(self):
        return (self.beta + self.i + self.j + self.alpha) % (2 * Constants.REDUCTION_P)
    def print(self):
        return "[" + str(self.beta) + ", " + str(self.i) + ", " +  str(self.j) + ", " + str(self.alpha) + "]"

    def __str__(self):
        return "[" + str(self.beta) + ", " + str(self.i) + ", " +  str(self.j) + ", " + str(self.alpha) + "]"

    def reduce_two(self, j, i, mode=0):
        mino = min(i, j)
        maxo = max(i, j)
        lam = 0
        if i == j:
            lam = max(0, int((maxo - 2) / 3))
        else:
            lam = max(0, int((mino - 1) / 3))
        return (i - lam * 3, j - lam * 3)

    def medial_reduce(self):
        if self.beta == 0 and self.i == 0 and self.j > 0:
            self.beta += 1
            self.j -= 1

        if self.alpha == 0 and self.j == 0 and self.i > 0:
            self.alpha += 1
            self.i -= 1

        if self.alpha == 0 and self.beta == 0:
            reduced = self.reduce_two(self.j, self.i)
            self.i = reduced[0]
            self.j = reduced[1]
        elif self.alpha == 1 and self.beta == 1:
            reduced = self.reduce_two(self.j, self.i)
            self.i = reduced[0]
            self.j = reduced[1]
        elif self.alpha == 0 and self.beta == 1:
            if self.i >= Constants.REDUCTION_P + 2 and self.beta + self.j >= Constants.REDUCTION_P + 1:
                reduced = self.reduce_two(self.j, self.i)
                self.i = reduced[0]
                self.j = reduced[1]
        elif self.alpha == 1 and self.beta == 0:
            if self.j >= Constants.REDUCTION_P + 2 and self.alpha + self.i >= Constants.REDUCTION_P + 1:
                reduced = self.reduce_two(self.j, self.i)
                self.i = reduced[0]
                self.j = reduced[1]

    def is_empty(self):
        return self.beta == 0 and self.i == 0 and self.j == 0 and self.alpha == 0

    def __pow__(self, power):
        # binary exponentiation
        if power == 0:
            return Word(0,0,0,0)

        result = copy.deepcopy(self)
        current = copy.deepcopy(self)

        power -= 1

        while power > 0:
            if power & 1 == 1:
                result = (current * result)
                result.medial_reduce()

            current = (current * current)
            current.medial_reduce()

            power = int(power / 2)
        return result

    def __mul__(self, other):
        return Word(self.beta, self.i + self.alpha + other.i, self.j + other.beta + other.j, other.alpha)