import cv2 as cv

src = cv.imread("../images/beauty.jpg")
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)

cv.waitKey(0)
cv.destroyAllWindows()