import cv2 as cv
import numpy as np
import time
import scipy.signal

def timeCalc():
    img = cv.imread("img_q1.5.jpg", cv.IMREAD_GRAYSCALE)
    timeTrack = [None] * 2

    xKernal = cv.getGaussianKernel(ksize=3, sigma=8)
    kernal = np.matmul(xKernal, np.transpose(xKernal))

    start = time.time()
    con1D = scipy.signal.convolve(img, xKernal)
    con1DFinal = scipy.signal.convolve(con1D, xKernal)
    end = time.time()

    timeTrack[0] = (end - start) * 1000

    start = time.time()
    con2D = scipy.signal.convolve(img, kernal)
    end = time.time()

    timeTrack[1] = (end-start) * 1000

    return timeTrack