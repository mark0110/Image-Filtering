import cv2 as cv
import numpy as np


hybrid1 = cv.imread("hybrid1.jpg", cv.IMREAD_GRAYSCALE)
hybrid2 = cv.imread("hybrid2.jpg", cv.IMREAD_GRAYSCALE)

h1_low_pass = cv.GaussianBlur(hybrid1, (3,3), 1)
h2_low_pass = cv.GaussianBlur(hybrid2, (5, 5), 1)
h2_high_pass = hybrid2 - h2_low_pass
hybrid = h2_high_pass + h1_low_pass
cv.imshow("Image", hybrid)
cv.waitKey(0)
cv.destroyAllWindows()