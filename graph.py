import matplotlib.pyplot as plt
import numpy as np
from math import floor
from regression import *

# Data file
data = np.loadtxt('results/royalwp-results-183226.csv', delimiter=',')
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

    # Generate polynomial regression
    z = Regression(initCrit, incrCrit)
    # Save function string
    funcs.append("ref%d(x)="%ref + str(z))

    label1 = 'ref' + str(ref)
    label2 = label1 + " (poly)"
    # Plot file data
    plt.plot(initCrit, incrCrit, color=colors[ref-1], label=label1)
    # Plot generated poly function
    plt.plot(initCrit, z.eval(initCrit), color=colors[ref-1],label=label2,ls='--',alpha=0.5)

# Save function strings
np.savetxt("polyfunctions.txt",funcs, fmt="%s")

# Graph configuration
plt.xticks(np.arange(0, 1.05, 0.05))
plt.yticks(np.arange(0, 0.25, 0.01))

plt.title("[GI] Royal Weapons CRIT Rate contribution")
plt.xlabel("Initial CRIT Rate")
plt.ylabel("CRIT Rate contribution")

plt.legend()
# Save graph
plt.savefig("graph.png")
plt.show()