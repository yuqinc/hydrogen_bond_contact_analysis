#!/home/caiy/anaconda/bin/python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pylab import *

from matplotlib import rc, rcParams

def set_pub():
    rc('font', weight='bold')    # bold fonts are easier to see
    rc('ytick', labelsize=15)     # tick labels bigger
    rc('xtick', labelsize=15)
    #rc('lines', lw=1, color='k') # thicker black lines (no budget for color!)
    #rc('grid', c='0.5', ls='-', lw=0.5)  # solid gray grid lines
    rcParams['figure.figsize']=10,10
    rc('savefig', dpi=300)       # higher res outputs
set_pub()
df =pd.read_csv("HB_occupancy.csv", index_col=0) #dataframe
#column_labels=("R-cdA","S-cdA","UNDA","R-cdG","S-cdG","cis-dG","UNDG")
#row_labels=list("H3-LYS115","H3-LYS122","H3(2)-LYS115","H3-VAL117","H3-THR118")  
df2 =pd.read_csv("HB_occupancy.csv", index_col=0) #dataframe
df3=df2.T  #tranpose 
colors=["blue","cyan","yellow","red","pink"]
width =0.45

df3.plot(kind='bar', stacked=True, color=colors, edgecolor="white", linewidth=4, alpha= 1); 
plt.legend(loc='upper center', bbox_to_anchor=(0.5,1.1), fancybox=True,shadow=True,ncol=3)
#plt.set_xticklabels(column_labels,rotation=90, minor=False,labelsize=15)
#set_ylabel("Hydrogen bond occupancies", fontsize=15)

#plt.show() 

savefig('HB_bar_stacked.png',figsize=(10, 10), dpi=300, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format=None, transparent
=False, bbox_inches=None, pad_inches=0.1, frameon=None)
 



