import time
import os
import cv2
import re


def resort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if int(re.findall(r'\d+', list[j])[0]) > int(re.findall(r'\d+', list[j+1])[0]):
                list[j], list[j+1] = list[j+1], list[j]
    return list


def picvideo(path, size):
    # path = r'C:\Users\Administrator\Desktop\1\huaixiao\\'#文件路径
    filelist = os.listdir(path)  # 获取该目录下的所有文件名
    filelist = resort(filelist)


    '''
    fps:
    帧率：1秒钟有n张图片写进去[控制一张图片停留5秒钟，那就是帧率为1，重复播放这张图片5次]
    如果文件夹下有50张 534*300的图片，这里设置1秒钟播放5张，那么这个视频的时长就是10秒
    '''
    fps = 24
    # size = (591,705) #图片的分辨率片
    file_path = 'video/new.mp4'  # 导出路径
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  # 不同视频编码对应不同视频格式（例：'I','4','2','0' 对应avi格式）

    video = cv2.VideoWriter(file_path, fourcc, fps, size)

    for item in filelist:
        if item.endswith('.jpg'):  # 判断图片后缀是否是.png
            item = path + '/' + item
            img = cv2.imread(item)  # 使用opencv读取图像，直接返回numpy.ndarray 对象，通道顺序为BGR ，注意是BGR，通道值默认范围0-255。
            video.write(img)  # 把图片写进视频

    video.release()  # 释放

#初始化视频的长*宽分辨率，根据自己的原始视频分辨率输入
picvideo(r'new', (480, 960))
