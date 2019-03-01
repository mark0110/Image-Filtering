import cv2 as cv
import numpy as np
import scipy.signal


def my_canny(img, sigma, thres):
    img = cv.imread(img, cv.IMREAD_GRAYSCALE)

    x_kernal = cv.getGaussianKernel(ksize=5, sigma=sigma)
    y_kernal = np.transpose(x_kernal)

    con_img = scipy.signal.convolve(img, x_kernal)
    con_img = scipy.signal.convolve(con_img, y_kernal).astype(np.uint8)

    sobel_y = cv.Sobel(con_img, cv.CV_16S, 0, 1, ksize=3)
    sobel_x = cv.Sobel(con_img, cv.CV_16S, 1, 0, ksize=3)
    sobel_y = cv.convertScaleAbs(sobel_y)
    sobel_x = cv.convertScaleAbs(sobel_x)
    sobel_xy = cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

    angle_mat = np.arctan2(sobel_y, sobel_x)
    angle_mat = (angle_mat * 180 / np.pi)
    zero_max = get_highest_intensity(sobel_xy, angle_mat)

    thres = get_double_threshold(zero_max, 0.03, 1)

    cv.imshow("Image", thres)
    cv.waitKey(0)
    cv.destroyAllWindows()


def get_highest_intensity(grad, angle):
    zero_max = np.zeros((grad.shape[0], grad.shape[1]), dtype=np.uint8)

    for i in range(1, len(grad) - 1):
        for j in range(1, len(grad[0]) - 1):
            before = 255
            after = 255
            if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                before = grad[i, j - 1]
                after = grad[i, j + 1]
            elif 22.5 <= angle[i, j] < 67.5:
                before = grad[i - 1, j + 1]
                after = grad[i + 1, j - 1]
            elif 67.5 <= angle[i, j] < 112.5:
                before = grad[i - 1, j]
                after = grad[i + 1, j]
            elif 112.5 <= angle[i, j] < 157.5:
                before = grad[i + 1, j - 1]
                after = grad[i - 1, j + 1]

            if (grad[i, j] >= before) and (grad[i, j] >= after):
                zero_max[i, j] = grad[i, j]
            else:
                zero_max[i, j] = 0
    return zero_max


def get_double_threshold(grad, low_int, high_int):
    high_thres = grad.max() * high_int
    low_thres = high_thres * low_int

    zero_max = np.zeros((grad.shape[0], grad.shape[1]), dtype=np.uint8)

    zero_max = np.where(grad >= high_thres, grad, np.int32(255))
    zero_max = np.where(grad < low_thres, grad, np.int32(0))
    zero_max = np.where(((grad <= high_thres) & (grad >= low_thres)), grad, np.int32(25))

    return zero_max
