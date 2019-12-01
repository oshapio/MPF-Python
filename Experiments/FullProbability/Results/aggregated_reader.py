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
# data_5 = read_folder(r"C:\Users\a\Documents\projects\MPF-Python\Experiments\FullProbability\Results\Limit5")
data_5 = pickle.load(open(r"C:\Users\a\Documents\projects\MPF-Python\Experiments\FullProbability\Results\Limit5\dmp.pkl","rb"))
# display results
figs, axes = plt.subplots(2,2,figsize=(14,7),sharey=True, sharex=True)
iter = 0

for i in range(len(data_5)):
    # calculate std of this batch
    probs = []
    for j in range(len(data_5[i])):
        probs.append(data_5[i][j]["hist_count"])
    probs = np.array(probs)
    mean_probs=np.mean(probs,axis=0)
    stds = np.std(probs,axis=0)

    y,x=1-i//2,1-i%2
    axes[y,x].bar(data_5[i][0]["bins"][1:-29],mean_probs[1:-28], yerr=stds[1:-28], capsize = 20)
    axes[y,x].set_title("$m = {}$".format(5-i))

    print("m = {:.2f} & {:.2f} \pm {:.3f} \\".format(5 - i, mean_probs[1], stds[1]))

    axes[y,x].grid(alpha=0.3)
    axes[y, x].set_ylim((0, 1.1))
    axes[y, x].set_xlim((0, 5))


plt.xticks((1,2,3,4), ("$1$", "$2$", "$3$", "$4$"))
axes[1,1].set_xlabel("$k$")
axes[1,0].set_xlabel("$k$")
axes[0,0].set_ylabel("$P_{\\texttt{avg}}(k)$")
axes[1,0].set_ylabel("$P_{\\texttt{avg}}(k)$")


# figs.xlabel("Count of public keys that are being mapped by private keys $x$ times")
# figs.ylabel("$P(x)$")
plt.subplots_adjust(hspace=0.9)
plt.tight_layout()

#plt.suptitle("$\\text{Solutions distribution for varying public parameter } W \\text{ order, } L_{PrK} = 5$",
#             horizontalalignment='center', y=1)
# save plot
plt.savefig(r"C:\Users\a\Documents\projects\MPF-Python\Experiments\FullProbability\Figs\limit_5.png",dpi=200)

figs.show()
k = 4