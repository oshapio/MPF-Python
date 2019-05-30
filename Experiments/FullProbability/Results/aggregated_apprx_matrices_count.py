import glob
import os
import pickle
import matplotlib.pyplot as plt
# import seaborn as sns
import numpy as np
def get_approx_matrices_count(m, L_prk):
    # return (L_prk**m - (L_prk - 1) ** m - L_prk) ** 2
    return (L_prk**m - (L_prk - 1) ** m ) ** 2

plt.rcParams.update({'font.size': 26})
plt.rc('text', usetex=True)

# plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}'] #for \text command

    # read limit 5 and limit 8 results and produce plots
# sns.set_style("ticks")
# sns.set_context("talk")
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
data_8 = read_folder(r"C:\Users\a\Documents\projects\MPF-Python\Experiments\FullProbability\Results\Limit8")
# display results
figs, axes = plt.subplots(1,figsize=(14,7))
iter = 0

means,mins,maxs,stds=[],[],[],[]

upper_bound = []
order = [2,3,4,5]
for i in range(len(data_5)):
    # calculate std , mean of this batch
    counts = []
    for j in range(len(data_5[i])):
        counts.append(data_5[i][j]["mats_count"])
    counts = np.array(counts)
    mean=np.mean(counts)
    min,max=np.min(counts),np.max(counts)
    upper_bound.append(get_approx_matrices_count(order[3-i],5))
    std = np.std(counts,axis=0)
    means.append(mean)
    mins.append(min)
    maxs.append(max)
    stds.append(std)
    #axes.bar(data_5[i][0]["bins"][1:-29],data_5[i][0]["hist_count"][1:-28], yerr=stds[1:-28])
    #axes.set_title("(W) = {}$".format(2+i))
# bad way of doing things..
means8, mins8, maxs8, stds8 = [], [], [], []

upper_bound8 = []
order8 = [2, 3, 4]
for i in range(len(data_8)):
    # calculate std , mean of this batch
    counts = []
    for j in range(len(data_8[i])):
        counts.append(data_8[i][j]["mats_count"])
    counts = np.array(counts)
    mean = np.mean(counts)
    min, max = np.min(counts), np.max(counts)
    upper_bound8.append(get_approx_matrices_count(order[2 - i], 8))
    std = np.std(counts, axis=0)
    means8.append(mean)
    mins8.append(min)
    maxs8.append(max)
    stds8.append(std)
    # axes.bar(data_5[i][0]["bins"][1:-29],data_5[i][0]["hist_count"][1:-28], yerr=stds[1:-28])
    # axes.set_title("(W) = {}$".format(2+i))

axes.set_xticks(range(2,6))
colors = ["#e6194b", "#3cb44b"]
axes.semilogy(order[::-1],means,'.--', color=colors[0],label="Mean empirical count, $L_{PrK} = 5$", alpha=0.5)
axes.semilogy(order[::-1], upper_bound,'.-', color=colors[0],label="Upper bound, $L_{PrK} = 5$")
axes.fill_between(order[::-1],means,np.array(upper_bound), color=colors[0],alpha=0.1)

axes.semilogy(order8[::-1],means8,'x--',color=colors[1],label="Mean emprical count, $L_{PrK} = 8$", alpha=0.5)
axes.semilogy(order8[::-1], upper_bound8, 'x-',color=colors[1],label="Upper bound, $L_{PrK} = 8$")
axes.fill_between(order8[::-1],means8,np.array(upper_bound8),  color=colors[1],alpha=0.1)


axes.set_xlabel("$m$")
axes.set_ylabel("$C(x)$")
axes.grid("--",alpha=0.3)

#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

# plt.legend()

box = axes.get_position()
axes.set_position([box.x0, box.y0 + box.height * 0.10,
                 box.width, box.height * 0.9])
legd3 = axes.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
          fancybox=True, shadow=True, ncol=2)



#axes.set_ylim((0,1.1))

plt.subplots_adjust(hspace=0.9)

# plt.tight_layout()

#plt.suptitle("$\\text{Solutions distribution for varying public parameter } W \\text{ order, } L_{PrK} = 5$",
#             horizontalalignment='center', y=1)
# save plot
plt.savefig(r"C:\Users\a\Documents\projects\MPF-Python\Experiments\FullProbability\Figs\count_estimation.pdf",  bbox_extra_artists=(legd3,), bbox_inches='tight')

figs.show()
k = 4