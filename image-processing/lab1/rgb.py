import cv2
import numpy as np

def rgb_subtraction(name, formate, color):
    base_img = cv2.imread('data/original.bmp').astype(np.float)
    target_img = cv2.imread('data/{}.{}'.format(name, formate)).astype(np.float)
    if (color == 'blue'):
        base_img[:, :, 2] = np.absolute(base_img[:, :, 2] - target_img[:, :, 2])
    elif (color == 'red'):
        base_img[:, :, 0] = np.absolute(base_img[:, :, 0] - target_img[:, :, 0])
    elif (color == 'green'):
        base_img[:, :, 1] = np.absolute(base_img[:, :, 1] - target_img[:, :, 1])
    elif (color == 'all'):
        for rgb in range (2):
            base_img[:, :, rgb] = np.absolute(base_img[:, :, rgb] - target_img[:, :, rgb])

    img = base_img.astype(np.uint8)
    cv2.imwrite('results/{}-{}.{}'.format(color, name, formate), img) 
       

if __name__ == "__main__":
    rgb_subtraction('jpeg', 'jpg', 'blue')
    rgb_subtraction('jpeg', 'jpg', 'red')
    rgb_subtraction('jpeg', 'jpg', 'green')
    rgb_subtraction('jpeg', 'jpg', 'all')
    rgb_subtraction('tif-lzw', 'tif', 'blue')
    rgb_subtraction('tif-lzw', 'tif', 'red')
    rgb_subtraction('tif-lzw', 'tif', 'green')
    rgb_subtraction('tif-lzw', 'tif', 'all')