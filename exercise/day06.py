"""
知识点： Look Up Table(LUT)查找表
解释了LUT查找表的作用与用法，代码实现与API介绍

- applyColorMap(src, dst, COLORMAP)
- src 表示输入图像
- dst表示输出图像
- 匹配到的颜色LUT， OpenCV支持13种颜色风格的查找表映射

有一张是伪色彩增强的python运行颜色，大家可以自己下载代码尝试
图像是蝉蛹！ 最后一张是OpenCV中支持13色彩风格！都可以运用到伪彩色增强上去！

应用是将一个低对比的图像变为了高对比度的图像
查找表的作用就是减少图像运算的工作。

伪色彩增强和加快运算速度

人的生理视觉系统特征对微小的灰度变化感觉不敏感，而对彩色的微小差别极为敏感，利用这一特点就可以把人眼不敏感的灰度信号映射为人眼灵敏的彩色信号，以增强人对图像中细微变换的分辨率。
在图像处理技术中，彩色增强应用十分广泛且效果显著
常见的彩色增强技术主要有假彩色增强和伪彩色增强两大类
（1）假彩色增强
思路是将灰度分层几级，比如我们这里将灰度分为16级，然后每一级灰度对应一种彩色。在查看原图中某像素，找出它所属的灰度级，用相应的彩色代替就行了
（2）伪彩色处理
由灰度值根据一定的映射关系求出R,G,B的值，组成该点的彩色值.OpenCV现在提供了各种颜色映射，以增强计算机视觉应用程序中的可视化。
在OpenCV中，只需要applyColorMap就可以在给定的图像上应用颜色映射。
"""
import cv2 as cv
src = cv.imread("../opencv_tutorial/data/images/test.png")
cv.namedWindow("image",cv.WINDOW_AUTOSIZE)
cv.imshow("image",src)
dst = cv.applyColorMap(src, cv.COLORMAP_COOL)
cv.imshow("output", dst)

image = cv.imread("../opencv_tutorial/data/images/canjian.jpg")
color_image = cv.applyColorMap(image, cv.COLORMAP_JET)
cv.imshow("image", image)
cv.imshow("color_image", color_image)

cv.waitKey(0)
cv.destroyAllWindows()

"""
LUT(look up table)查找表
查找表的作用:
1.一般的灰度图像有256个灰度值,而有时候我们并不需要这么精确的
灰度级(严重影响运算时间),比如黑白图像.意味着我们以一个新的输
入值划分当前的颜色空间.
即降低灰度级从而提高运算速度
"""