import matplotlib.pyplot as plt
import numpy as np
# parse the file
path = r"C:\Users\a\Documents\projects\MPF\algos\results\max_word_16\out.txt"

with open(path) as f:
    content = f.readlines()

parts = content[1].split(',')
res = [ (int(i.split(" ")[0]), int(i.split(" ")[1])) for i in parts[:-1]]

res = np.array(res)

plt.plot(res[:,0], res[:,1], '.-')
plt.grid()

# lets get accumulated
plt.figure()
acum = np.cumsum(res[:,1])
plt.plot(res[:,0], acum /acum[-1])
plt.grid()
plt.show()