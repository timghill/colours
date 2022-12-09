"""
Test generating new colourschemes
"""

import numpy as np
from matplotlib import pyplot as plt

import colours

cont_cmap = colours.get_colourmap('pl-blue-8').reversed()

cc1 = cont_cmap(0.45)
cc2 = cont_cmap(0.65)

cont_cmap2 = colours.get_colourmap('pl-YellowFields').reversed()

cc3 = cont_cmap2(0.2)
cc4 = cont_cmap2(0.6)

cc5 = 0.3*np.ones(4)
cc6 = 0.5*np.ones(4)

cc5[-1] = 1
cc6[-1] = 1


fig, ax = plt.subplots()
xx = np.linspace(0, 1, 10)

colours = np.array([cc1, cc2, cc3, cc4, cc5, cc6])

print(colours)

for i in range(colours.shape[0]):
    ax.plot(xx, xx + np.random.random(xx.shape), color=colours[i])

np.savetxt('../data/categorical/6-bluegold-paired.txt', colours)
plt.show()
