import cv2 as cv


def show_img1():
    img = cv.imread("Q1.1.jpg")
    cv.imshow("Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def show_img2():
    img = cv.imread("Q1Part2.jpg")
    cv.imshow("Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
