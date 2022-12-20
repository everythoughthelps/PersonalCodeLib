import cv2 as cv
import numpy as np

path = './test_images/gray_depth.png'

image = cv.imread(path)       # 读取图片,格式为BGR, three modes, cv2.IMREAD_COLOR for ignoring the alpha
                                # cv2.IMREAD_GRAYSCALE for gray mode, cv2.IMREAD_UNCHANGED for loading alpha
cv.imshow('color_depth', image)
cv.waitKey(0)

print("image_shape: ", image.shape) # h, w, c
print(type(image))                  # numpy.ndarray

#image = cv.cvtColor(cv_image, cv.COLOR_BGR2GRAY ) #转灰度
#image = cv.cvtColor(cv_image, cv.COLOR_BGR2RGB )

#downsample
width = int(image.shape[0] / 2)
height = int(image.shape[1] / 2)
image = cv.resize(image, (height, width), interpolation=cv.INTER_CUBIC)

#visualization:
gray_depth_visualization = np.uint8(image * 255.0 / image.max())
# use 255.0 rather 255 to avoid stack overflowing
# or use gray_depth_visualization = np.array(image * 255.0 / image.max(), dtype=’uint8′)


#save the image
cv.imwrite('destination', image)
cv.destroyAllWindows()
