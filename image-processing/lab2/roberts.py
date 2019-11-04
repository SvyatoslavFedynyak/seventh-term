import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from skimage.filters import roberts
from skimage.io import imread

image = imread('data/parrots.jpeg', as_gray=True)
edge_roberts = roberts(image)

plt.imsave('data/parrots-roberts.png', edge_roberts, cmap='gray', format='png')