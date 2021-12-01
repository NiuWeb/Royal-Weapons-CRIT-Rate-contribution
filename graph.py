import matplotlib.pyplot as plt
import numpy as np
from math import floor
from regression import *

# Data file
data = np.loadtxt('results/royalwp-results-202302.csv', delimiter=',')
# Base CRIT Rate data
initCrit = data[0]

# List of function strings
funcs = []

# Styles
colors = ('tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple')
plt.figure(figsize=(12,8))

for ref in range(1, 6):
    # CRIT Rate contribution data
    incrCrit = data[ref]

    x = []
    y = []
    for i in range(len(incrCrit)):
        if incrCrit[i] > 0:
            x.append(initCrit[i])
            y.append(incrCrit[i])
            i=i+1

    # Generate polynomial regression
    z = Regression(x, y, 6)
    # Save function string
    funcs.append("ref%d(x)="%ref + str(z))

    label1 = 'ref' + str(ref)
    label2 = label1 + " (poly)"
    # Plot file data
    plt.plot(x, y, color=colors[ref-1], label=label1)
    # Plot generated poly function
    plt.plot(x, z.eval(x), color=colors[ref-1],label=label2,ls='--',alpha=0.5)

# Save function strings
np.savetxt("results/polyfunctions.txt",funcs, fmt="%s")

# Graph configuration
plt.xticks(np.arange(-1, 1.05, 0.1))
plt.yticks(np.arange(0, 1, 0.05))

plt.title("[GI] Royal Weapons CRIT Rate contribution")
plt.xlabel("initial CRIT Rate")
plt.ylabel("Effective CRIT Rate with Royal weapon")

plt.legend()
# Save graph
plt.savefig("results/graph.png")
plt.savefig("results/graph.svg")
plt.show()