import cv2 as cv

src = cv.imread("../images/beauty.jpg")
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)
# 保持窗口，直到有键盘响应
cv.waitKey(0)
# 销毁所有的窗口避免内存的泄露
cv.destroyAllWindows()