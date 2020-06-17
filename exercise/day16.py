"""
OpenCV-day-016

图像ROI与ROI操作
图像ROI解释:
图像的ROI(region of interest)是指图像中感兴趣区域、在OpenCV中图像设置图像ROI区域，实现只对ROI区域操作。

1. 矩形ROI区域提取
2. 矩形ROI区域copy

3. 不规则ROI区域
- ROI区域mask生成
- 像素位 and操作
- 提取到ROI区域
- 加背景or操作
- add 背景与ROI区域
"""
import cv2 as cv
import numpy as np

src = cv.imread("../images/beauty.jpg")
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)
h,w = src.shape[:2]

# 获取ROI
cy = h//2
cx = w//2
roi = src[cy-100:cy+110,cx-100:cx+100,:]
cv.imshow("roi",roi)

# copy ROI
image = np.copy(roi)

# modify roi
roi[:,:,0] = 0
cv.imshow("result",src)

# modify copy roi
image[:, :, 2] = 0
cv.imshow("result", src)
cv.imshow("copy roi", image)

# example with ROI - generate mask
src2 = cv.imread("../images/beauty.jpg")
cv.imshow("src2", src2)
hsv = cv.cvtColor(src2, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv, (0, 0, 46), (180, 43, 220))
cv.imshow("mask",mask)

# extract person ROI
mask = cv.bitwise_not(mask)
person = cv.bitwise_and(src2, src2, mask=mask)
cv.imshow("person",person)

# generate background  生成蓝色的背景
result = np.zeros(src2.shape, src2.dtype)
result[:,:,2] = 255


# combine background + person 将人与蓝色背景组合
mask = cv.bitwise_not(mask)
dst = cv.bitwise_or(person, result, mask=mask)
dst = cv.add(dst, person)

cv.imshow("dst", dst)

cv.waitKey(0)
cv.destroyAllWindows()