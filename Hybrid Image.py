import cv2 as cv
import numpy as np


hybrid1 = cv.imread("hybrid1.jpg", cv.IMREAD_GRAYSCALE)
hybrid2 = cv.imread("hybrid2.jpg", cv.IMREAD_GRAYSCALE)

h1_low_pass = cv.GaussianBlur(hybrid1, (5, 5), 500)
h1_high_pass = hybrid1 - h1_low_pass
h2_low_pass = cv.GaussianBlur(hybrid2, (5, 5), 600)
hybrid = h1_high_pass + h2_low_pass
cv.imshow("Image", hybrid)
cv.waitKey(0)
cv.destroyAllWindows()