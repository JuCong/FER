"""
知识点： 色彩空间与色彩空间转换
- RGB色彩空间
独立于设备的色彩空间
- HSV色彩空间
直方图相关的算法，会取得比较好的效果
- YUV色彩空间
与设备有关的色彩空间
- YCrCb色彩空间

API知识点
- 色彩空间转换cvtColor
- 提取指定色彩范围区域inRange
"""
import cv2 as cv

src = cv.imread("../opencv_tutorial/data/images/test.png")
cv.namedWindow("rgb", cv.WINDOW_AUTOSIZE)
cv.imshow("rgb", src)

# RGB to HSV
hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

# RGB to YUV
yuv = cv.cvtColor(src, cv.COLOR_BGR2YUV)
cv.imshow("yuv", yuv)

# RGB to YUV
ycrcb = cv.cvtColor(src, cv.COLOR_BGR2YCrCb)
cv.imshow("ycrcb", ycrcb)

src2 = cv.imread("../opencv_tutorial/data/images/toux.jpg")
cv.imshow("src2", src2)
hsv = cv.cvtColor(src2, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv, (100, 43, 46), (124, 255, 255))
dst = cv.bitwise_and(src2,src2,mask=mask)  # mask也参加运算
# dst =cv.bitwise_not(dst)
cv.imshow("mask", mask)
cv.imshow("dst",dst)

cv.waitKey(0)
cv.destroyAllWindows()


