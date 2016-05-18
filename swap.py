def swap(l, i1, i2):
	l[i1], l[i2] = l[i2], l[i1]

	return l

#lb, lt, rt, rb
def make_coords(old_dict):
	new_dict = dict()
	for d in old_dict.iteritems():
		data = d[1]
		new_data = [(data[0], data[2]), (data[0], data[3]), (data[1], data[3]), (data[1], data[2])]
		new_dict[d[0]] = new_data

	return new_dict

from matplotlib import patches
import matplotlib.pyplot as plt
from matplotlib.path import Path

CODES = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

fig = plt.figure()
ax = fig.add_subplot(111)
for d in data.iteritems():
	verts = d[1] + [d[1][0]]
	print(verts)
	path = Path(verts, CODES)
	patch = patches.PathPatch(path, facecolor='orange', lw=2)
	ax.add_patch(patch)

plt.show()


