from matplotlib import patches
import matplotlib.pyplot as plt
from matplotlib.path import Path
import pickle as pkl
import numpy as np
from operator import add
from math import sqrt

def set_rc_parameters():
	fig_width_pt = 400.0  # Get this from LaTeX using \showthe\columnwidth
	inches_per_pt = 1.0/72.27               # Convert pt to inch
	golden_mean = (sqrt(5)-1.0)/2.0         # Aesthetic ratio
	fig_width = fig_width_pt*inches_per_pt  # width in inches
	fig_height = fig_width*0.8      # height in inches
	fig_size =  [fig_width,fig_height]
	params = {'savefig.format': 'png',
	         'axes.labelsize': 10,
	         'text.fontsize': 10,
	         'legend.fontsize': 10,
	         'xtick.labelsize': 8,
	         'ytick.labelsize': 8,
	         'text.usetex': True,
	         'figure.figsize': fig_size,
	         'figure.dpi': 80}
	plt.rcParams.update(params)

set_rc_parameters()

with open('animal_data.p') as f:
	data=pkl.load(f)

usv_data = dict()
usv_data['false_killer_whale'] = [(500, 5430), (500, 8290) , (2000, 8290), (2000, 5430)]  
usv_data['rat'] = [(0.15580719694546694, 20e3),(0.15580719694546694, 80e3), (0.3293662323972531, 80e3), (0.3293662323972531, 20e3)] 
usv_data['sperm_whale'] =[(14e3, 400),(14e3, 15e3,) ,(41e3,15e3),(41e3,400)]
usv_data['bat'] = [(0.005, 25e3), (0.005, 70e3), (0.15, 70e3), (0.15,25e3)]
usv_data['mouse'] = [(0.01, 35e3), (0.01,90e3), (.025,90e3), (0.025,35e3)]

CODES = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

fig = plt.figure()
ax = fig.add_subplot(111, axisbg='white', aspect='equal')
mauve = [224./255,176./255,255./255]
label_size = 8
for d in data.iteritems():
	verts = d[1] + [d[1][0]]
	path = Path(verts, CODES)
	patch = patches.PathPatch(path, facecolor=mauve, lw=2)
	patch.set_zorder(3)
	ax.add_patch(patch)
	
	if d[0] == 'dog':
		xy = list(d[1][0])
		xytext = map(add, xy, [-5,-150])
		ax.annotate(d[0], xy=xy, xytext=xytext, size = label_size,
			arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3") , )
	elif d[0] == 'elephant':
		xy = list(d[1][1])
		xytext = map(add, xy, [-2000,100])
		ax.annotate(d[0], xy=xy, xytext=xytext, size = label_size,
			arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3")) 
	elif d[0] == 'rat':
		xy = list(d[1][2]) 
		xytext = map(add, xy, [0.3, 200]) 
		ax.annotate(d[0], xy=xy, xytext=xytext, size = label_size,
			arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"))
	elif d[0] == 'cat':
		xy = list(d[1][2]) 
		xytext = map(add, xy, [-4, 1000])
		ax.annotate(d[0], xy=xy, xytext=xytext, size = label_size,
			arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"))
	elif d[0] == 'gorilla':
		patch.set_zorder(4)
		xy = list(d[1][2]) 
		xytext = map(add, xy, [0,500])
		ax.annotate(d[0], xy=xy, xytext=xytext, size = label_size,
			arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"))
	elif d[0] == 'monkey':
		patch.set_zorder(4)
		xy = list(d[1][2]) 
		xytext = map(add, xy, [0,1000])
		ax.annotate(d[0], xy=xy, xytext=xytext, size = label_size,
			arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"))
	elif d[0] == 'human':
		xy = list(d[1][2]) 
		xytext = map(add, xy, [75,-250])
		ax.annotate(d[0], xy=xy, xytext=xytext, size = label_size,
			arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"))
	elif d[0] == 'horse':
		xy = list(d[1][2]) 
		xytext = map(add, xy, [500,1000])
		ax.annotate(d[0], xy=xy, xytext=xytext, size = label_size,
			arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"))
	
	

for d in usv_data.iteritems():
	verts = d[1] + [d[1][0]]
	path = Path(verts, CODES)
	patch = patches.PathPatch(path, facecolor='lightgreen', lw=2)
	patch.set_zorder(3)
	ax.add_patch(patch)

	if d[0] == 'rat':
		patch.set_zorder(5)
		xy = list(d[1][2]) 
		xytext = map(add, xy, [0.3, -37e3]) 
		ax.annotate(r'brown rat\\narrowband', xy=xy, xytext=xytext, size = label_size,
			arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"), )
	if d[0] == 'false_killer_whale':
		xy = list(d[1][2]) 
		xytext = map(add, xy, [-1950, 10e3]) 
		ax.annotate(r'\noindent false killer whale\\narrowband', xy=xy, xytext=xytext, size = label_size,
			arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"))

	if d[0] == 'sperm_whale':
		xy = list(d[1][2])
		xytext = map(add, xy, [-40e3, 10e3]) 
		ax.annotate(r'\noindent sperm whale\\broadband', xy=xy, xytext=xytext, size = label_size,
			arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"))

	if d[0] == 'mouse':
		xy = list(d[1][2])
		patch.set_zorder(5)
		xytext = map(add, xy, [0, 40e3]) 
		ax.annotate('house mouse narrowband', xy=xy, xytext=xytext, size = label_size,
			arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"))

	if d[0] == 'bat':
		xy = list(d[1][3])
		xy = map(add, xy, [-0.09, 0]) 
		patch.set_zorder(4)
		xytext = map(add, xy, [-0.04, -15e3]) 
		ax.annotate("Daubenton's bat broadband", xy=xy, xytext=xytext, size = label_size,
			arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"))


a = 0.4
m = np.arange(0.01,100e3)
ax.plot(m, 1300*m**(-a), color='black')
a = 0.33
ax.plot(m, 1200*m**(-a), color='black', linestyle='--')

ax.grid(True)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlim(0.01,100e3)
ax.set_ylim(10,350e3)
ax.set_xlabel('Animal mass (kg)')
ax.set_ylabel('Frequency (Hz)')
fig.tight_layout()
fig.savefig('/home/matthew/work/writing/jump_paper/frequency_scaling.png')

plt.show()