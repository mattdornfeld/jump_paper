import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np
from os import listdir
from os import chdir
from PIL import Image
import matplotlib.gridspec as gridspec

chdir('/home/matthew/Dropbox/Work/writing/'+
	'paper_preperation/jump_figs')
files = listdir('/home/matthew/Dropbox/Work/writing/'+
	'paper_preperation/jump_figs')

images = [Image.open(f) for f in files]


"""
fig = plt.figure()

grid = ImageGrid(fig, 111, # similar to subplot(111)
                nrows_ncols = (2, 5), # creates 2x2 grid of axes
                axes_pad=0.1, # pad between axes in inch.
                )
"""

num_rows = 2
num_cols = 5

fig = plt.figure()
gs = gridspec.GridSpec(num_rows, num_cols, wspace=0.0)

ax = [plt.subplot(gs[i]) for i in range(num_rows*num_cols)]
gs.update(hspace=0)
#gs.tight_layout(fig, h_pad=0,w_pad=0)

for i,im in enumerate(images):
    ax[i].imshow(im)
    ax[i].axis('off')
    #ax_grid[i/num_cols,i-(i/num_cols)*num_cols].imshow(im) # The AxesGrid object work as a list of axes.
    #ax_grid[i/num_cols,i-(i/num_cols)*num_cols].axis('off')

"""
all_axes = fig.get_axes()
for ax in all_axes:
    for sp in ax.spines.values():
        sp.set_visible(False)
    if ax.is_first_row():
        ax.spines['top'].set_visible(True)
    if ax.is_last_row():
        ax.spines['bottom'].set_visible(True)
    if ax.is_first_col():
        ax.spines['left'].set_visible(True)
    if ax.is_last_col():
        ax.spines['right'].set_visible(True)
"""
plt.show()