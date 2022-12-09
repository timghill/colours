"""
Test generating new colourschemes
"""

import numpy as np
from matplotlib import pyplot as plt

import colours

cc1 = colours.get_colourmap('ccBurg')(0.5)
cc2 = colours.get_colourmap('pl-blue-8')(0.5)
cc3 = colours.get_colourmap('ccPurpOr')(0.8)
cc4 = colours.get_colourmap('pl-blue-11')(0.8)
cc5 = colours.get_colourmap('ccBurgYl')(0.35)
cc6 = colours.get_colourmap('pl-blue-3')(0.3)

fig, ax = plt.subplots()
xx = np.linspace(0, 1, 10)

colours = np.array([cc1, cc2, cc3, cc4, cc5, cc6])
colours[0] = colours[0]
colours[:, -1] = 1

print(colours)

for i in range(colours.shape[0]):
    ax.plot(xx, xx + np.random.random(xx.shape), color=colours[i])

np.savetxt('../data/categorical/6-bluepurple.txt', colours)
plt.show()
