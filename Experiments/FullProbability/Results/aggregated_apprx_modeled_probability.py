import glob
import os
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statsmodels.compat import scipy
import scipy
from scipy.optimize import curve_fit
def get_approx_matrices_count(m, L_prk):
    return (L_prk**m - (L_prk - 1) ** m - L_prk) ** 2

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}'] #for \text command


    # read limit 5 and limit 8 results and produce plots
sns.set_style("ticks")
sns.set_context("talk")
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
order_5 = [2,3,4,5]
order_8=[2,3,4]
order = [2,3,4,5]

limit_5 = [5,5,5,5]
limit_8 = [8,8,8,8]
prob_5 = []
prob_8 = []

for i in range(len(data_5)):
    # calculate std , mean of this batch
    counts = []
    hists = []
    for j in range(len(data_5[i])):
        counts.append(data_5[i][j]["mats_count"])
        hists.append(data_5[i][j]["hist_count"])
    hists = np.array(hists)
    counts = np.array(counts)
    mean_hists = np.mean(hists,axis=0)
    mean=np.mean(counts)

    prob = 0
    for j in range(1, len(mean_hists) - 1):
        prob += j / mean * mean_hists[j]

    prob_5.append(prob)
    min,max=np.min(counts),np.max(counts)


    std = np.std(counts,axis=0)
    means.append(mean)
    mins.append(min)
    maxs.append(max)
    stds.append(std)
    # calculate
    #axes.bar(data_5[i][0]["bins"][1:-29],data_5[i][0]["hist_count"][1:-28], yerr=stds[1:-28])
    #axes.set_title("(W) = {}$".format(2+i))
# bad way of doing things..
means8, mins8, maxs8, stds8 = [], [], [], []

upper_bound8 = []
order8 = [2, 3, 4]
for i in range(len(data_8)):
    # calculate std , mean of this batch
    counts = []
    hists = []
    for j in range(len(data_8[i])):
        counts.append(data_8[i][j]["mats_count"])
        hists.append(data_8[i][j]["hist_count"])
    hists = np.array(hists)
    counts = np.array(counts)
    mean_hists = np.mean(hists,axis=0)
    mean=np.mean(counts)

    prob = 0
    for j in range(1, len(mean_hists) - 1):
        prob += j / mean * mean_hists[j]

    prob_8.append(prob)
    # axes.bar(data_5[i][0]["bins"][1:-29],data_5[i][0]["hist_count"][1:-28], yerr=stds[1:-28])
    # axes.set_title("(W) = {}$".format(2+i))

# find best variant

pars5, cov5 = curve_fit(lambda t,b,c: b*2**(-c*t), order_5[1:], prob_5[:-1][::-1],maxfev=50000)
f = lambda x :  pars5[0] * 2 **(-pars5[1] * x)


apprx_5 = []
for i in order_5:
    apprx_5.append(f(i))

# for limit 8:
pars8, cov8 = curve_fit(lambda t,b,c: b*2**(-c*t), order_8, prob_8[::-1],maxfev=50000)
f = lambda x :  pars8[0] * 2 **(-pars8[1] * x)

apprx_8 = []
for i in order_8:
    apprx_8.append(f(i))

axes.set_xticks(range(2,6))

#axes.semilogy(order8[::-1], upper_bound8, label="Upper bound of appropriate matrices, $L_{PrK} = 8$")
#axes.fill_between(order8[::-1],means8,np.array(upper_bound8), label="Difference of numerical and analytical estimations with $L_{PrK} = 8$",alpha=0.1)

axes.semilogy(order_5, prob_5[::-1], 's--',color="blue", label="Numerically estimated $p$, when $L_{PrK} = 5$")
axes.semilogy(order_5, apprx_5, 's--',color="blue", alpha=0.2, label="Approximated $p = "+str(round(pars5[0], 2)) + "\cdot2^{-" + str(round(pars5[1], 2)) + " \cdot m}$, when $L_{PrK} = 5$")


axes.semilogy(order_8, prob_8[::-1], '^--',color="red", label="Numerically estimated $p$, when $L_{PrK} = 8$")
axes.semilogy(order_8, apprx_8, '^--',color="red", alpha=0.2,label="Approximated $p = "+str(round(pars8[0], 2)) + "\cdot2^{-" + str(round(pars8[1], 2)) + " \cdot m}$, when $L_{PrK} = 8$")

axes.set_xlabel("$Order(W), x$")
axes.set_ylabel("$P(x)$")
axes.grid(alpha=0.3)

#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.legend()
#axes.set_ylim((0,1.1))

plt.subplots_adjust(hspace=0.9)
plt.tight_layout()

#plt.suptitle("$\\text{Solutions distribution for varying public parameter } W \\text{ order, } L_{PrK} = 5$",
#             horizontalalignment='center', y=1)
# save plot
#plt.savefig(r"C:\Users\a\Documents\projects\MPF-Python\Experiments\FullProbability\Figs\full_prob_estimation.pdf")

figs.show()
k = 4