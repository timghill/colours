"""
test_colours.py

Basic examples for setting colourmaps and colour cycles using the colours package.
"""

import numpy as np
from matplotlib import pyplot as plt

import colours

# 2D colourmap
fig1, ax1 = plt.subplots()
im=ax1.imshow(np.random.random((50, 50)), cmap=colours.get_colourmap('ccGeyser'))
fig1.colorbar(im)
ax1.axis('off')

# Lineplot
fig2, ax2 = plt.subplots()
xx = np.linspace(0, 1, 101)
yy1 = xx + 0.4*np.random.random((101,))
yy2 = -0.5 + 2*xx + 0.4*np.random.random((101,))
yy3 = yy1[::-1]
yy4 = yy2[::-1]
yy5 = 0.5 + 0.4*np.random.random((101,))

ax2.set_prop_cycle(color=colours.get_colourscheme('tab-GreenOrange'))
ax2.plot(xx, yy1)
ax2.plot(xx, yy2)
ax2.plot(xx, yy3)
ax2.plot(xx, yy4)
ax2.plot(xx, yy5)
ax2.legend(['y1', 'y2', 'y3', 'y4', 'y5'], frameon=False)

plt.show()
