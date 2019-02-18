import cv2 as cv

def showImg1():
    img = cv.imread("Q1.1.jpg")
    cv.imshow("Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def showImg2():
    img = cv.imread("Q1Part2.jpg")
    cv.imshow("Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()