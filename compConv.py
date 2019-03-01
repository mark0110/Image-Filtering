import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time
import scipy.signal


def comp():
    img = cv.imread("3.jpg")
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    k_size = [3, 5, 7, 13, 21, 31, 41, 51, 71]
    con_time1 = [None] * 9
    con_time2 = [None] * 9

    for i in range(len(k_size)):
        kernal = np.matmul(cv.getGaussianKernel(ksize=k_size[i], sigma=2),
                           np.transpose(cv.getGaussianKernel(k_size[i], 0.01)))
        start = time.time()
        con = scipy.signal.convolve2d(gray, kernal)
        end = time.time()
        con_time1[i] = (end - start) * 1000

    plt.plot(k_size, con_time1, '-b', label='Spatial domain')

    dft = cv.dft(np.float32(gray), flags=cv.DFT_REAL_OUTPUT)

    for i in range(len(k_size)):
        kernal = np.matmul(cv.getGaussianKernel(ksize=k_size[i], sigma=0.01),
                           np.transpose(cv.getGaussianKernel(k_size[i], 0.01)))
        start = time.time()
        con = scipy.signal.convolve2d(dft, kernal)
        end = time.time()
        con_time2[i] = (end - start) * 1000

    plt.plot(k_size, con_time2, '-r', label='Frequency domain')
    plt.ylabel('Execution time (ms)')
    plt.xlabel('Kernel size')
    plt.legend(loc='upper left')
    plt.show()
