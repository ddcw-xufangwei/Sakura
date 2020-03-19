import cv2
#视频分帧
vidcap = cv2.VideoCapture('video/video.avi')
success,image = vidcap.read()
count = 0
success = True
while success:
    success,image = vidcap.read()
    cv2.imwrite("pic/frame%d.jpg" % count, image)  # save frame as JPEG file
    if cv2.waitKey(10) == 27:
        break
    count += 1
