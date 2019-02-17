import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time
import scipy.signal

def Mycanny(sigma):
    xKernal = cv.getGaussianKernel(ksize=5, sigma=sigma)
    yKernal = np.transpose(xKernal)

    img = cv.imread()