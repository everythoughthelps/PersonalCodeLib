import cv2
import subprocess

rtsp = "rtsp://127.0.0.1/stream"
rtmp = 'rtsp://127.0.0.1/live'
#rtmp = 'rtmp://127.0.0.1/live'

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
           #'rtsp_transport', 'tcp',
           rtmp]
'''
command = ['ffmpeg',
           '-y',
           '-f', 'rawvideo',
           '-vcodec', 'rawvideo',
           '-pix_fmt', 'bgr24',
           '-s', sizeStr,
           '-r', '25',
           '-i', '-',
           '-c:v', 'libx264',
           '-preset', 'faster',
           '-f', 'flv',
           rtmp]    # rmtp推流时地址后面只能写live
'''
pipe = subprocess.Popen(command, shell=False, stdin=subprocess.PIPE)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        #cv2.imshow('frame', frame)
        '''
		对frame进行识别处理
		'''
        if cv2.waitKey(delay=100) & 0xFF == ord('q'):
            break
        pipe.stdin.write(frame.tobytes())
        '******'

cap.release()
pipe.terminate()

