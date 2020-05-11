"""
OpenCV中图像像素读写操作
Python中的像素遍历与访问
- 数组遍历
"""
import cv2 as cv
import numpy as np

src = cv.imread("../images/beauty.jpg")
cv.namedWindow("image",cv.WINDOW_AUTOSIZE)
cv.imshow("image",src)

# 克隆图像
m1 = np.copy(src)

# 赋值
m2 = src
# 截取一个白色窗口
src[100:200,200:300,:] = 255
cv.imshow("m2",m2)

m4 = np.zeros([512,512], dtype=np.uint8)       # 字节类型
cv.imshow("m4", m4)

m5 = np.ones(shape=[512,512,3], dtype=np.uint8)   # 创建一个三通道的图像
m5[:,:,0] = 255
cv.imshow("m5", m5)

cv.waitKey(0)
cv.destroyAllWindows()
