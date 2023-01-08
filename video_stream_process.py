import numpy as np
from torchvision.transforms import ToTensor
import cv2
import subprocess

rtsp = "rtsp://127.0.0.1/stream"
rtmp = 'rtmp://localhost:1935/test'

# 读取视频并获取属性
cap = cv2.VideoCapture(rtsp)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
sizeStr = str(size[0]) + 'x' + str(size[1])

command = ['ffmpeg',
           '-y', '-an',
           '-f', 'rawvideo',
           '-vcodec', 'rawvideo',
           '-pix_fmt', 'bgr24',
           '-s', sizeStr,
           '-r', '25',
           '-i', '-',
           '-c:v', 'libx264',
           '-pix_fmt', 'yuv420p',
           '-preset', 'ultrafast',
           '-f', 'rtsp',
           'rtsp_transport', 'tcp',
           rtmp]
pipe = subprocess.Popen(command, shell=False, stdin=subprocess.PIPE)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        cv2.imshow('frame', frame)
        '''
		对frame进行识别处理
		'''
        if cv2.waitKey(delay=100) & 0xFF == ord('q'):
            break
        pipe.stdin.write(frame.tostring())
        '******'

cap.release()
pipe.terminate()

