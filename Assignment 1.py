import numpy
import cv2 as cv
import matplotlib

i = cv.imread('2.jpg')

cv.imshow('this is it', i)
cv.waitKey(0)