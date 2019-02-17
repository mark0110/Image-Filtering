import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time
import scipy.signal

def Mycanny(sigma):
    xKernal = cv.getGaussianKernel(ksize=5, sigma=2)
    yKernal = np.transpose(xKernal)

    img = cv.imread("bowl-of-fruit.jpg", cv.IMREAD_GRAYSCALE)

    conImg = scipy.signal.convolve(img, xKernal)
    conImg = scipy.signal.convolve(conImg, yKernal)

    lopImg = cv.Laplacian(conImg, cv.CV_16S, 3)
    lopImgFinal = cv.convertScaleAbs(lopImg)

    cv.imshow("lop", lopImgFinal)
    cv.waitKey(0)
    cv.destroyAllWindows()


Mycanny(3)