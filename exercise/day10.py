# 像素归一化
"""
OpenCV中提供了四种归一化的方法
- NORM_MINMAX
- NORM_INF
- NORM_L1
- NORM_L2
最常用的就是NORM_MINMAX归一化方法。

相关API函数：
normalize(
InputArray 	src, // 输入图像
InputOutputArray 	dst, // 输出图像
double 	alpha = 1, // NORM_MINMAX时候低值
double 	beta = 0, // NORM_MINMAX时候高值
int 	norm_type = NORM_L2, // 只有alpha
int 	dtype = -1, // 默认类型与src一致
InputArray 	mask = noArray() // mask默认值为空
)
"""

import cv2 as cv
import numpy as np

src = cv.imread("../opencv_tutorial/data/images/test.png")
cv.namedWindow("image",cv.WINDOW_AUTOSIZE)
cv.imshow("image",src)

gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)

gray = np.float32(gray)
print(gray)

dst = np.zeros(gray.shape,dtype=np.float32)
cv.normalize(gray,dst,alpha=0,beta=1,norm_type=cv.NORM_MINMAX)
print(dst)
cv.imshow("NORM_MINMAX",np.uint8(dst*255))




cv.waitKey(0)
cv.destroyAllWindows()

"""
计算时需要浮点数，然后在转换为整数
"""