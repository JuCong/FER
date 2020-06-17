"""
图像直方图

图像直方图的解释
图像直方图是图像像素值的统计学特征、计算代价较小，具有图像平移、旋转、缩放不变性等众多优点，广泛地应用于图像处理的各个领域，
特别是灰度图像的阈值分割、基于颜色的图像检索以及图像分类、反向投影跟踪。常见的分为
- 灰度直方图
- 颜色直方图

Bins是指直方图的大小范围， 对于像素值取值在0～255之间的，最少有256个bin，此外还可以有16、32、48、128等，256除以bin的大小应该是整数倍。

OpenCV中相关API
calcHist(&bgr_plane[0], 1, 0, Mat(), b_hist, 1, bins, ranges);
cv.calcHist([image], [i], None, [256], [0, 256])


"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def custom_hist(gray):
    h, w = gray.shape
    hist = np.zeros([256], dtype=np.int32)
    for row in range(h):
        for col in range(w):
            pv = gray[row, col]
            hist[pv] += 1

    y_pos = np.arange(0, 256, 1, dtype=np.int32)
    plt.bar(y_pos, hist, align='center', color='r', alpha=0.5)
    plt.xticks(y_pos, y_pos)
    plt.ylabel('Frequency')
    plt.title('Histogram')

    # plt.plot(hist, color='r')
    # plt.xlim([0, 256])
    plt.show()


def image_hist(image):
    cv.imshow("input", image)
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()


src = cv.imread("../images/beauty.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
# cv.imshow("input",src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# custom_hist(gray)
image_hist(src)
cv.waitKey(0)
cv.destroyAllWindows()


