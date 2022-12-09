"""
Test generating new colourschemes
"""

import numpy as np
from matplotlib import pyplot as plt

import colours

cont_cmap = colours.get_colourmap('pl-green-brown-div')

cc1 = cont_cmap(0.2)
cc2 = cont_cmap(0.3)
cc3 = cont_cmap(0.8)
cc4 = cont_cmap(0.7)
cc5 = 0.3*np.ones(4)
cc6 = 0.5*np.ones(4)

fig, ax = plt.subplots()
xx = np.linspace(0, 1, 10)

colours = np.array([cc1, cc2, cc3, cc4, cc5, cc6])
colours[0] = colours[0]
colours[:, -1] = 1

print(colours)

for i in range(colours.shape[0]):
    ax.plot(xx, xx + np.random.random(xx.shape), color=colours[i])

np.savetxt('../data/categorical/6-greenbrown-paired.txt', colours)
np.savetxt('../data/categorical/3-greenbrown.txt', colours[np.array([0, 2, 5])])
plt.show()
