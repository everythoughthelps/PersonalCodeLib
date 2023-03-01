
# list the local camera
ffmpeg -list_devices true -f dshow -i dummy

# push the local camera stream to rtsp address
ffmpeg -f dshow -i video="your camera name" -vcodec libx264 -preset:v ultrafast -tune:v zerolatency -rtsp_transport tcp -f rtsp rtsp://127.0.0.1/test

# push a local video stream to rtsp address
# -stream_loop -1 means loop the video stream
ffmpeg -stream_loop -1 -re -i C:\\Users\\panmeng\\Downloads\\video.mp4 -rtsp_transport tcp -vcodec h264 -f rtsp rtsp://localhost/test

# pull a video stream with ffplay
ffplay rtsp://127.0.0.1:554/stream

# crop a video to a spcific size
ffmpeg -i yourvideo.mp4 -vf crop=w:h:start_x:start_y out.mp4

#turn a batch of images to a video, use -pix_fmt yuv420p on windows platform
ffmpeg -i frame_000%3d.png -pix_fmt yuv420p out.mp4