import cv2 as cv
import numpy as np


city_img = cv.imread("city.jpg")
city_img = cv.cvtColor(city_img, cv.COLOR_BGR2GRAY)
city_ft = np.fft.fft2(city_img)

face_img = cv.imread("face.jpg")
face_img = cv.cvtColor(face_img, cv.COLOR_BGR2GRAY)
face_ft = np.fft.fft2(face_img)

combined1 = np.multiply(np.abs(face_ft), np.exp(1j*np.angle(city_ft)))
image1 = np.real(np.fft.ifft2(combined1)).astype(np.uint8)

combined2 = np.multiply(np.abs(city_ft), np.exp(1j*np.angle(face_ft)))
image2 = np.real(np.fft.ifft2(combined2)).astype(np.uint8)

cv.imshow("Image 1", image1)
cv.imshow("Image 2", image2)
cv.waitKey(0)
cv.destroyAllWindows()

