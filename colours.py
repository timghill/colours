"""

get_colourmap.py

"""

import numpy as np
from matplotlib.colors import ListedColormap

def get_colourmap(name):
    fpath = 'data/continuous/' + name + '.txt'
    colour_map = np.loadtxt(fpath)
    return ListedColormap(colour_map)

def get_colourscheme(name):
    return np.loadtxt('data/categorical/' + name + '.txt')

