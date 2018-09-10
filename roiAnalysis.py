# -*- coding: utf-8 -*-
"""
This example demonstrates the use of ImageView, which is a high-level widget for
displaying and analyzing 2D and 3D data. ImageView provides:
  1. A zoomable region (ViewBox) for displaying the image
  2. A combination histogram and gradient editor (HistogramLUTItem) for
     controlling the visual appearance of the image
  3. A timeline for selecting the currently displayed frame (for 3D data only).
  4. Tools for very basic analysis of image data (see ROI and Norm buttons)
"""
## Add path to library (just for examples; you do not need this)
#import initExample

import numpy as np
import scipy.ndimage.filters
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg

app = QtGui.QApplication([])

## Create window with ImageView widget
win = QtGui.QMainWindow()
win.resize(800,800)
imv = pg.ImageView()
win.setCentralWidget(imv)
win.show()
win.setWindowTitle('pyqtgraph : augmented ImageView')

## Create strcutured 3D data
decay = np.exp(-np.linspace(0,2,10))[:,np.newaxis,np.newaxis]
data = np.ones((10,20,20))
data += 2
data[:,:10,:10] = 1
data[:,10:,:10] = 2
data[:,:10,10:] = 3
data[:,10:,10:] = 4

data = data * decay

## Display the data and assign each frame a time value from 1.0 to 3.0
imv.setImage(data, xvals=np.linspace(1., 3., data.shape[0]))

#r1 = pg.PolyLineROI([[80, 60], [90, 30], [60, 40]], pen=(6,9), closed=True,removable=True)
#rois.append(pg.PolyLineROI([[80, 60], [90, 30], [60, 40]], pen=(6,9), closed=True,removable=True))
#imv.addItem(r1)

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
