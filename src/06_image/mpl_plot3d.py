# Obtained from: https://matplotlib.org/gallery/pyplots/whats_new_99_mplot3d.html#sphx-glr-gallery-pyplots-whats-new-99-mplot3d-py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def generate_3d_plot(output_filename):
    X = np.arange(-5, 5, 0.03)
    Y = np.arange(-5, 5, 0.01)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)

    plt.savefig(output_filename, format='png')

generate_3d_plot('../../mplot3d.png')