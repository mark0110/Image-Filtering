import cv2 as cv
import numpy as np
import math

xKernal = cv.getGaussianKernel(ksize=13, sigma=2)
yKernal = cv.getGaussianKernel(13, 2)
kernal = np.matmul(xKernal, np.transpose(yKernal))

img = cv.imread("3.jpg")

cv.imshow("image", img)