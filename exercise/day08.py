"""
知识点： 通道分离与合并
OpenCV中默认imread函数加载图像文件，加载进来的是三通道彩色图像，色彩空间是RGB色彩空间、通道顺序是BGR（蓝色、绿色、红色）、对于三通道的图像OpenCV中提供了两个API函数用以实现通道分离与合并。

- split // 通道分类
- merge // 通道合并

扩展一下：
在很多CNN的卷积神经网络中输入的图像一般会要求[h, w, ch]其中h是高度、w是指宽度、ch是指通道数数目、
OpenCV DNN模块中关于图像分类的googlenet模型输入[224,224,3]表示的就是224x224大小的三通道的彩色图像输入。

更正一下代码里面的内容关于mixchannels的 Python版本用法，参考如下代码即可：
dst = np.zeros(src.shape, dtype=np.uint8)
print(src.shape)
print(dst.shape)
cv.mixChannels([src], [dst], fromTo=[2, 0, 1, 1, 0, 2])
cv.imshow("output4", dst)
解释：
1. mixchannels使用前必须先分配好np图像对象
2. 前两个参数书图像数组，感谢一位同学向我反馈！
"""
import cv2 as cv
import numpy as np

src = cv.imread("../opencv_tutorial/data/images/flower.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

# 蓝色通道为零
mv = cv.split(src)
mv[0][:, :] = 0
dst1 = cv.merge(mv)
cv.imshow("output1", dst1)

# 绿色通道为零
mv = cv.split(src)
mv[1][:, :] = 0
dst2 = cv.merge(mv)
cv.imshow("output2", dst2)

# 红色通道为零
mv = cv.split(src)
mv[2][:, :] = 0
dst3 = cv.merge(mv)
cv.imshow("output3", dst3)

# cv.mixChannels(src, dst3, [2, 0])
# cv.imshow("output4", dst3)

dst = np.zeros(src.shape, dtype=np.uint8)
print(src.shape)
print(dst.shape)
cv.mixChannels([src], [dst], fromTo=[2, 0, 1, 1, 0, 2])  # 就是交换第一和第三通道
cv.imshow("output4", dst)

cv.waitKey(0)
cv.destroyAllWindows()
"""
mixChannels就是通道的交换与提取，【2,0】将输入矩阵的第三个通道数据复制到输出矩阵的第一个通道。
"""