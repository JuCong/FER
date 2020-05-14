# 视频读写
"""
VideoCapture 视频文件读取、摄像头读取、视频流读取
VideoWriter 视频写出、文件保存、
- CAP_PROP_FRAME_HEIGHT
- CAP_PROP_FRAME_WIDTH
- CAP_PROP_FRAME_COUNT
- CAP_PROP_FPS             每一秒处理了多少帧数据
不支持音频编码与解码保存，不是一个音视频处理的库！主要是分析与解析视频内容。保存文件最大支持单个文件为2G
"""
import cv2 as cv
import numpy as np
capture = cv.VideoCapture("../opencv_tutorial/data/images/video.avi")
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv.CAP_PROP_FPS)
print(height, width, count, fps)
# 视屏保存的路径，视频的编码格式mp4就是d i v x，fps 每秒种15帧，（h） ，（w），
out = cv.VideoWriter("../images/test.mp4", cv.VideoWriter_fourcc('D', 'I', 'V', 'X'), 15,
                     (np.int(width), np.int(height)), True)

while True:
    ret, frame = capture.read()
    if ret is True:
        cv.imshow("video-input", frame)
        out.write(frame)
        # 间隔50ms，监听键盘响应
        c = cv.waitKey(50)
        if c == 27: # ESC
            break
    else:
        break

capture.release()
out.release()
cv.destroyAllWindows()