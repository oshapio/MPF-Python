import glob
import os
import pickle
import matplotlib.pyplot as plt
import numpy as np
def get_approx_matrices_count(m, L_prk):
    return (L_prk**m - (L_prk - 1) ** m - L_prk) ** 2

plt.rcParams.update({'font.size': 30})
# plt.rcParams.update({'axes.labelsize': 20})

plt.rc('text', usetex=True)

    # read limit 5 and limit 8 results and produce plots
def read_folder(folder_path):
    os.chdir(folder_path)

    results = []
    for file in reversed(sorted(glob.glob("*"))):
        if "x" not in file:
            continue
        dict = pickle.load(open(file,"rb"))
        results.append(dict)
    return results

# 5 limit data
data_5 = read_folder(r"C:\Users\a\Documents\projects\MPF-Python\Experiments\FullProbability\Results\Limit5")
# display results
figs, axes = plt.subplots(2,2,figsize=(14,7),sharey=True, sharex=True)
iter = 0

for i in range(len(data_5)):
    # calculate std of this batch
    probs = []
    for j in range(len(data_5[i])):
        probs.append(data_5[i][j]["hist_count"])
    probs = np.array(probs)
    stds = np.std(probs,axis=0)


    y,x=i//2,i%2
    axes[y,x].bar(data_5[i][0]["bins"][1:-29],data_5[i][0]["hist_count"][1:-28], yerr=stds[1:-28])
    axes[y,x].set_title("$m = {}$".format(2+i))

    axes[y,x].grid(alpha=0.3)
    axes[y, x].set_ylim((0, 1.1))
    axes[y, x].set_xlim((0, 5))


axes[1,1].set_xlabel("$x$")
axes[1,0].set_xlabel("$x$")
axes[0,0].set_ylabel("$P(x)$")
axes[1,0].set_ylabel("$P(x)$")


# figs.xlabel("Count of public keys that are being mapped by private keys $x$ times")
# figs.ylabel("$P(x)$")
plt.subplots_adjust(hspace=0.9)
plt.tight_layout()

#plt.suptitle("$\\text{Solutions distribution for varying public parameter } W \\text{ order, } L_{PrK} = 5$",
#             horizontalalignment='center', y=1)
# save plot
plt.savefig(r"C:\Users\a\Documents\projects\MPF-Python\Experiments\FullProbability\Figs\limit_5.pdf")

figs.show()
k = 4