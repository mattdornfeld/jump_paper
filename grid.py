import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np
from os import listdir
from os import chdir
from PIL import Image

chdir('/home/matthew/Dropbox/Work/writing/'+
    'paper_preperation/jump_figs')
files = listdir('/home/matthew/Dropbox/Work/writing/'+
    'paper_preperation/jump_figs')

images = [Image.open(f) for f in files]
def product(*args, **kwds):
        pools = map(tuple, args) * kwds.get('repeat', 1)
        result = [[]]
        for pool in pools:
            result = [x+[y] for x in result for y in pool]
        for prod in result:
            yield tuple(prod)


def squiggle_xy(a, b, c, d, i=np.arange(0.0, 2*np.pi, 0.05)):
    return np.sin(i*a)*np.cos(i*b), np.sin(i*c)*np.cos(i*d)

fig = plt.figure()

num_rows = 2
num_cols = 5
# gridspec inside gridspec
outer_grid = gridspec.GridSpec(num_rows, num_cols, wspace=0.0, hspace=0.0)

for i in range(num_cols*num_rows):
    inner_grid = gridspec.GridSpecFromSubplotSpec(1,1,
            subplot_spec=outer_grid[i], wspace=0.0, hspace=0.0)
    a, b = int(i/num_cols)+1,i%num_cols+1
    for j, (c, d) in enumerate(product(range(1, num_cols), repeat=2)):
        ax = plt.Subplot(fig, inner_grid[j])
        ax.plot(*squiggle_xy(a, b, c, d))
        ax.set_xticks([])
        ax.set_yticks([])
        fig.add_subplot(ax)

all_axes = fig.get_axes()

#show only the outside spines
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

plt.show()

