import cv2 as cv
import numpy as np
import math



def myConv():
    cimg = cv.imread("1.jpg")
    img = cv.cvtColor(cimg, cv.COLOR_BGR2GRAY)
    xKernal = cv.getGaussianKernel(ksize=13, sigma=2)
    yKernal = cv.getGaussianKernel(13, 2)
    kernal = np.matmul(xKernal, np.transpose(yKernal))
    newKernal = [0] * len(kernal)
    for i in range(len(kernal)):
        newKernal[i] = [0] * len(kernal[i])
    for i in range(len(kernal), 0, -1):
        for j in range(len(kernal[i - 1]) , 0, -1):
            newKernal[len(kernal) - i][len(kernal) - j] = kernal[i - 1][j - 1]
    padding = math.floor(len(kernal)/2)
    newImg = np.zeros((2*padding + len(img), 2*padding + len(img[0])), np.uint8)
    for i in range(padding, len(img) + padding):
        for j in range(padding, len(img[0]) + padding):
            newImg[i][j] = img[i - padding][j - padding]
    newerImg = np.zeros((len(img), len(img[0])), np.uint8)
    for i in range(padding, len(newImg) - padding):
        for j in range(padding, len(newImg[i]) - padding):
            arr = newImg[i-padding:i+padding, j-padding:j+padding]
            newerImg[i - padding][j - padding] = applyConv(arr, newKernal)
    filtImg = cv.filter2D(img, ddepth=-1, kernel=kernal)
    compared = abs(filtImg - newerImg)
    cv.imshow("Image",compared)
    cv.waitKey(0)
    cv.destroyAllWindows()

def applyConv(arr, kernal):
    total = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            total += arr[i][j]*kernal[i][j]
    return total
