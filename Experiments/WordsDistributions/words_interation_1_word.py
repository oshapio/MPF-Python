from Word import Word
import numpy as np
import matplotlib.pyplot as plt

# initial word
test_word = Word(0,1,4,0)

counts = {}

for index in range(1,1000):
    powed = test_word ** index

    if powed.i not in counts:
        counts[powed.i] = {}
    if powed.j not in counts[powed.i]:
        counts[powed.i][powed.j] = 0
    counts[powed.i][powed.j] += 1

figs, axes = plt.subplots(3, 1)
plt.suptitle('One word exponentiation, intial word = {}'.format(test_word.print()))
for i in range(1,4):
    axes[i-1].plot(counts[i].values())

plt.show()