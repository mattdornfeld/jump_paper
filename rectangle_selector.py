from __future__ import print_function
"""
Do a mouseclick somewhere, move the mouse to some destination, release
the button.  This class gives click- and release-events and also draws
a line or a box from the click-point to the actual mouseposition
(within the same axes) until the button is released.  Within the
method 'self.ignore()' it is checked wether the button from eventpress
and eventrelease are the same.

"""
from matplotlib.widgets import RectangleSelector
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
import pickle as pkl

global names, i, animals
names = ['rat', 'cat', 'monkey', 'horse', 'dog', 'gorilla', 'human', 'elephant']
i = 0
animals = dict()

def line_select_callback(eclick, erelease):
    global i, names, animals
    'eclick and erelease are the press and release events'
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    animals[names[i]] = pixel_to_data(x1, x2, y1, y2)
    print(names[i])
    i+=1
    with open('animal_freqs.p', 'wb') as f:
      pkl.dump(animals, f)

    #print ("(%3.2f, %3.2f) --> (%3.2f, %3.2f)" % (freqs[0], freqs[2], freqs[1], freqs[3]))
    print (" The button you used were: %s %s" % (eclick.button, erelease.button))

def toggle_selector(event):
    print (' Key pressed.')
    if event.key in ['Q', 'q'] and toggle_selector.RS.active:
        print (' RectangleSelector deactivated.')
        toggle_selector.RS.set_active(False)
    if event.key in ['A', 'a'] and not toggle_selector.RS.active:
        print (' RectangleSelector activated.')
        toggle_selector.RS.set_active(True)

def pixel_to_data(l, r, t, b):
  box_v = 222.97
  box_h = 116.13 
  freqs = [0, 0, 0, 0]
  freqs[0] = 10**(-2 + l / box_h)
  freqs[1] = 10**(-2 + r / box_h)
  freqs[2] = 10**(4 - t / box_v)
  freqs[3] = 10**(4 - b / box_v)

  return freqs


fig, current_ax = plt.subplots()                    # make a new plotingrange
img = imread('fs.png')
current_ax.imshow(img)




print ("\n      click  -->  release")

# drawtype is 'box' or 'line' or 'none'
toggle_selector.RS = RectangleSelector(current_ax, line_select_callback,
                                       drawtype='box', useblit=True,
                                       button=[1,3], # don't use middle button
                                       minspanx=5, minspany=5,
                                       spancoords='pixels')
plt.connect('key_press_event', toggle_selector)
plt.show()