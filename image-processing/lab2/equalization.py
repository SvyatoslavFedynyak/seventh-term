import cv2
import sys, os
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

def imhist(im):
	m, n = im.shape
	h = [0.0] * 256
	for i in range(m):
		for j in range(n):
			h[im[i, j]]+=1
	return np.array(h)/(m*n)

def cumsum(h):
	return [sum(h[:i+1]) for i in range(len(h))]

def histeq(im):
	h = imhist(im)
	cdf = np.array(cumsum(h))
	sk = np.uint8(255 * cdf) 
	s1, s2 = im.shape
	Y = np.zeros_like(im)
	for i in range(0, s1):
		for j in range(0, s2):
			Y[i, j] = sk[im[i, j]]
	H = imhist(Y)
	return Y , h, H, sk

data_root='data/'

img = cv2.imread(os.path.join(data_root, 'parrots.jpeg'))

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()


img_y_cr_cb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
y, cr, cb = cv2.split(img_y_cr_cb)

y_eq = cv2.equalizeHist(y)

img_y_cr_cb_eq = cv2.merge((y_eq, cr, cb))
img2 = cv2.cvtColor(img_y_cr_cb_eq, cv2.COLOR_YCR_CB2BGR)

cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')

img_hist = cdf[img]

hist,bins = np.histogram(img_hist.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img_hist.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

cv2.imwrite(os.path.join(data_root, 'equalized.jpeg'),img2)