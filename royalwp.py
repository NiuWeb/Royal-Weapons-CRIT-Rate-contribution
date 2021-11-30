from simulator import simulateHits
import numpy as np
from datetime import datetime as dt


# ==== RUN SIMULATIONS ====

# Number of hits for the test
hits = 1e6
# Data output file
now = dt.now().strftime("%H%M%S")
fname = "results/royalwp-results-%s.csv" % (now)
print(fname)

# Data storing
incrCrit = []
baseCrit = np.arange(-1, 1, 0.01)
sample = len(baseCrit)
data = [baseCrit]

# Test for different refinement ranges:
for ref in range(1, 6):

    # Control
    n = 0
    p = 0

    # Test for different CRIT Rates:
    for rate in baseCrit:
        n += 1
        # simulate the hits
        crits = simulateHits(hits, ref, rate)
        # real CRIT Rate (CRIT hits scored / total hits scored)
        nrate = crits/hits
        incrCrit.append(nrate)

        # Control!
        if n >= sample/10:
            n = 0
            p += 10
            print("Ref {0} {1}\u0025 sampled".format(ref, p))

    data.append(np.array(incrCrit))
    incrCrit.clear()

# Data export
np.savetxt(fname, data, delimiter=',')