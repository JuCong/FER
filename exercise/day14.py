# 图像的插值
"""
图像插值(Image Interpolation)
就是图像的缩小 像素的变化
最常见四种插值算法
INTER_NEAREST = 0  # 临近点插值   速度最快
INTER_LINEAR = 1   # 双线性插值   速度最快
INTER_CUBIC = 2    # 立方插值 高质量使用
INTER_LANCZOS4 = 4 # 高质量使用
相关的应用场景
几何变换、透视变换、插值计算新像素
resize,
如果size有值，使用size做放缩插值，否则根据fx与fy
卷积、
"""
import cv2 as cv

src = cv.imread("../opencv_tutorial/data/images/test.png")
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)

h, w = src.shape[:2]
print(h, w)
# 两个参数不同时起作用，dsize先起作用,fx fy后起作用
dst = cv.resize(src, (w*2, h*2), fx=0.75, fy=0.75, interpolation=cv.INTER_NEAREST)
cv.imshow("INTER_NEAREST", dst)

dst = cv.resize(src, (w*2, h*2), interpolation=cv.INTER_LINEAR)
cv.imshow("INTER_LINEAR", dst)

dst = cv.resize(src, (w*2, h*2), interpolation=cv.INTER_CUBIC)
cv.imshow("INTER_CUBIC", dst)

dst = cv.resize(src, (w*2, h*2), interpolation=cv.INTER_LANCZOS4)
cv.imshow("INTER_LANCZOS4", dst)

cv.waitKey(0)
cv.destroyAllWindows()