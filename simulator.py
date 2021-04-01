from random import seed, random
import numpy as np
seed()

def chance(rate):
    return random() <= rate

# Simulator
def simulateHits(hits, refRange, initRate = 0.05):
    """
    :hits:     Amount of hits to simulate
    :refRange: Weapon refinement range
    :initRate: Initial character's CRIT Rate (without the passive stack).

    Returns the number of CRIT hits scored
    """
    stack = 0.08 + 0.02*(refRange - 1) # CRIT Rate passive stack
    rate  = initRate                   # Initial CRIT Rate
    crits = 0 # CRIT hits scored
    stacks= 0 # Passive stacks count

    for i in range(int(hits)):
        # if a CRIT hit is scored
        if chance(rate): 
            crits+= 1 # adds it to the counter
            rate  = initRate # remove the passive stacks
            stacks= 0 # reset the passive stacks counter

        # if a non-CRIT hit is scored
        elif stacks < 5: 
            rate  += stack # stacks the passive
            stacks+= 1 # increment the counter

    return crits