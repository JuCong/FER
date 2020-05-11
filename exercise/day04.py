"""
OpenCV中图像像素读写操作

Python中的像素遍历与访问
- 数组遍历
"""

import cv2 as cv

src = cv.imread("../images/beauty.jpg")
cv.namedWindow("image",cv.WINDOW_AUTOSIZE)
cv.imshow("image",src)

# 获取彩色图片的高 宽 通道数
h,w,ch = src.shape

# 遍历像素值，对像素取反
for row in range(h):
    for col in range(w):
        b,g,r = src[row,col]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        src[row, col] = [b, g, r]

cv.imshow("output",src)


cv.waitKey(0)
cv.destroyAllWindows()