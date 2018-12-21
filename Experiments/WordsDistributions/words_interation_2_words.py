from Word import Word
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#plt.rcParams['text.usetex'] = True
#plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}'] #for \text command

# initial word
test_word_1 = Word(1, 8, 6, 1)
test_word_2 = Word(0, 3, 2, 0)
test_word_3 = Word(0, 6, 8, 0)
test_word_4 = Word(0, 2, 3, 0)


counts_i = {}
counts_j = {}

for index_1 in range(1, 15):
    for index_2 in range(1, 15):
        for index_3 in range(1, 15):
            for index_4 in range(1, 15):
                powed1 = (test_word_1 ** index_1)
                powed2 = (test_word_2 ** index_2)
                powed3 = (test_word_3 ** index_1)
                powed4 = (test_word_4 ** index_2)

                powed = powed1 * powed2 * powed3 * powed4

                powed.medial_reduce()

                if powed.i not in counts_i:
                    counts_i[powed.i] = {}
                if powed.j not in counts_i[powed.i]:
                    counts_i[powed.i][powed.j] = 0
                counts_i[powed.i][powed.j] += 1

                if powed.j not in counts_j:
                    counts_j[powed.j] = {}
                if powed.i not in counts_j[powed.j]:
                    counts_j[powed.j][powed.i] = 0
                counts_j[powed.j][powed.i] += 1

figs, axes = plt.subplots(4, 2)
sns.set_style("ticks")

plt.suptitle('Two words exponentiation, intial words = ${}$, ${}$'.format(test_word_1.print(), test_word_2.print()))
y, x = -1, -1
for cols in axes:
    x += 1
    y = -1
    for row in cols:
        y += 1
        try:
            if y == 0:
                row.set_title('$j = {}$'.format(x + 1), fontsize=7)
                row.set_xlabel('$i$', fontsize=5)
                row.plot(counts_j[x + 1].keys(), counts_j[x + 1].values(), '.', markersize=2)
            else:
                row.set_title('$i = {}$'.format(x + 1), fontsize=7)
                row.set_xlabel('$j$', fontsize=5)
                row.plot(counts_i[x + 1].keys(), counts_i[x + 1].values(), '.', markersize=2)
        except:
            pass



        row.grid(alpha=0.3)
        row.set_ylabel('Count   ', fontsize=5)

plt.tight_layout(rect=[0, 0.03, 1, 0.95], pad=0.2)
plt.show()
# lets save it
plt.savefig('Results\Plots\\2Words\{}{}.pdf'.format(test_word_1.print(), test_word_2.print()))
