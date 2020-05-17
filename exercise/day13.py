# 图像翻转
"""
图像翻转的本质像素映射，OpenCV支持三种图像翻转方式
- X轴翻转，flipcode = 0
- Y轴翻转, flipcode = 1
- XY轴翻转, flipcode = -1

相关的API
flip
- src输入参数
- dst 翻转后图像
- flipcode
"""
import cv2 as cv
src = cv.imread("../opencv_tutorial/data/images/test.png")
cv.namedWindow("image",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)

# x 翻转 倒影
dst1 = cv.flip(src,0)
cv.imshow("x-flip",dst1);

# Y 翻转 镜像
dst2 = cv.flip(src,1)
cv.imshow("y-flip",dst2);

# xy 翻转 对角
dst3 = cv.flip(src,-1)
cv.imshow("xy-flip",dst3);

cv.waitKey(0)
cv.destroyAllWindows()