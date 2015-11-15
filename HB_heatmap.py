#!/home/caiy/anaconda/bin/python

import numpy as np
import pandas as pd
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams

def set_pub():
    rc('font', weight='bold')    # bold fonts are easier to see
    rc('ytick', labelsize=15)     # tick labels bigger
    rc('xtick', labelsize=15)
    #rc('lines', lw=1, color='k') # thicker black lines (no budget for color!)
    #rc('grid', c='0.5', ls='-', lw=0.5)  # solid gray grid lines
    rcParams['figure.figsize']=10,7.15
    rc('savefig', dpi=300)       # higher res outputs

set_pub()

dataMatrix =pd.read_csv("HB_occupancy.csv", index_col=0)

print dataMatrix
print dataMatrix.shape[0]
print dataMatrix.shape[1] 
print np.arange(dataMatrix.shape[0])+0.5
print np.arange(dataMatrix.shape[1])+0.5

column_labels=["R-cdA","S-cdA","UNDA","R-cdG","S-cdG","cis-BP-dG","UNDG"]
row_labels=["H3-LYS115","H3-LYS122","H3(2)-LYS115","H3-VAL117","H3-THR118"]

fig =plt.figure()
ax =figure().add_subplot(111)
heatmap = ax.pcolor(dataMatrix, cmap=plt.cm.Blues)
#ax.plot_surface(xs,ys,zs)

# add the major ticks 
ax.set_xticks(np.arange(dataMatrix.shape[1])+0.5, minor=False)
ax.set_yticks(np.arange(dataMatrix.shape[0])+0.5, minor=False)

ax.invert_yaxis()
ax.xaxis.tick_top()

ax.set_xticklabels(column_labels,rotation=0, minor=False)
ax.set_yticklabels(row_labels,rotation=45, minor=False)
#plt.show() 

savefig('HB_heatmap.jpg',figsize=(10, 7.15), dpi=300, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format=None, transparent
=False, bbox_inches=None, pad_inches=0.1, frameon=None)
 

