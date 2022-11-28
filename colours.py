"""

get_colourmap.py

"""

import os
import math

import numpy as np
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import pyplot as plt

def get_colourmap(name):
    fpath = 'data/continuous/' + name + '.txt'
    colour_map = np.loadtxt(fpath)
    return ListedColormap(colour_map)

def get_colourscheme(name):
    return np.loadtxt('data/categorical/' + name + '.txt')

def join_cmaps(cm1, cm2, N1=128, N2=128, name='Joined Cmap', average=False):
    """Join two LinearSegmentedColormap instances
    Joins colormaps cm1 and cm2 by extracting lists of
    size (N1 x 4) from cm1 and (N2 x 4) from cm2. The
    new LinearSegmented colormap is computed from
    the concanetated arrays with the
    LinearSegmentedColormap.from_list method.
    The first colormap will be squeezed to take up
    a fraction N1 / (N1 + N2) of the resulting map,
    and the second colormap will take up a fraction
    N2 / (N1 + N2). The default N1=N2=128 results
    in equal-fraction colormaps.
    Parameters:
    --------
    cm1 : LinearSegmentedColormap
        First colormap to join.
        e.g., cm1 = palettes.get_cmap([cmap name])
    cm2 : LinearSegmentedColormap
        Second colormap to join
    N1 : int
        Number of samples from first colormap
    N2 : int
        Number of samples from second colormap

    average : int
        Window length to moving average filter
        the colormap to remove hard boundaries
    Returns:
    -------
    cm : LinearSegmentedColormap
    """
    cm1_data = cm1(np.linspace(0, 255, N1).astype(int))
    cm2_data = cm2(np.linspace(0, 255, N2).astype(int))

    cm_data = np.concatenate((cm1_data, cm2_data))

    cm_smooth = np.zeros(cm_data.shape)
    if average:
        for j in range(cm_smooth.shape[1]):
            col = cm_data[:, j]
            smooth_col = np.convolve(col, np.ones(average), 'valid')/average
            cm_smooth[:len(smooth_col), j] = smooth_col

        cm_data = cm_smooth[:len(smooth_col)]

    cm = LinearSegmentedColormap.from_list(name, cm_data)

    return cm

def show_continuous():
    db_path ='data/continuous/'
    cmap_files=sorted(os.listdir(db_path))

    all_cmap_paths=[f for f in cmap_files if os.path.splitext(f)[-1]=='.txt']
    
    fig,axs=plt.subplots(math.ceil(len(all_cmap_paths)/3),3, figsize=(8, 8))
    all_axs=axs.flatten()
    for ii in range(len(all_axs)):
        all_axs[ii].set_visible(False)

    cdata=np.repeat([np.linspace(0,1,129)],10,axis=0)
    x=np.linspace(0,1,129)
    y=np.linspace(0,1,10)
    xx,yy=np.meshgrid(x,y)

    for ii in range(len(all_cmap_paths)):
        cmap_name=os.path.splitext(os.path.split(all_cmap_paths[ii])[-1])[0]
        all_axs[ii].set_visible(True)
        all_axs[ii].imshow(cdata,cmap=get_colourmap(cmap_name))
        all_axs[ii].set_axis_off()

        all_axs[ii].text(0.5,0.5,cmap_name,transform=all_axs[ii].transAxes,horizontalalignment='center',verticalalignment='center')

    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.05, top=0.95)

    return fig

def show_categorical():
    db_path = 'data/categorical'
    cmap_files = sorted(os.listdir(db_path))
    all_paths = [f for f in cmap_files if os.path.splitext(f)[-1]=='.txt']

    fig, axs = plt.subplots(math.ceil(len(all_paths)/2),2)
    all_axs = axs.flat

    for ii in range(len(all_axs)):
        all_axs[ii].set_visible(False)

    cdata = np.repeat([np.linspace(0, 1, 129)], 10, axis=0)
    x = np.linspace(0, 1, 129)
    y = np.linspace(0, 1, 10)
    xx, yy = np.meshgrid(x, y)

    for ii in range(len(all_paths)):
        cmap_name = os.path.splitext(os.path.split(all_paths[ii])[-1])[0]

        data = get_colourscheme(cmap_name)
        all_axs[ii].set_visible(True)
        all_axs[ii].imshow(cdata, cmap=LinearSegmentedColormap.from_list('', data, N=data.shape[0]))
        all_axs[ii].set_axis_off()

        all_axs[ii].text(0.5, 0.5, cmap_name, transform=all_axs[ii].transAxes,
                horizontalalignment='center', verticalalignment='center')

    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.05, top=0.95,
            hspace=0.025, wspace=0.025)

    return fig

def show():
    f1 = show_continuous()
    f2 = show_categorical()

    plt.show()

    return f1, f2

if __name__=='__main__':
    f1,f2 = show()
    f1.savefig('continuous.png', dpi=600)
    f2.savefig('categorical.png', dpi=600)
