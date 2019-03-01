import cv2 as cv


def show_img1():
    cv.namedWindow("Image", cv.WINDOW_NORMAL)
    cv.resizeWindow("Image", 1000, 1000)
    img = cv.imread("Q1.1.jpg")
    cv.imshow("Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def show_img2():
    cv.namedWindow("Image", cv.WINDOW_NORMAL)
    cv.resizeWindow("Image", 1000, 1000)
    img = cv.imread("Q1Part2.jpg")
    cv.imshow("Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
