from PIL import Image
import cv2 as cv
import matplotlib as mlp

path = ''

pil_image = Image.open(path)

cv_image = cv.imread(path)       # 读取图片,格式为BGR
cv.imshow('color_depth', cv_image)
cv.waitKey(0)

print("image_shape: ", cv_image.shape) # h, w, c
print(type(cv_image))                  # numpy.ndarray

#image = cv.cvtColor(cv_image, cv.COLOR_BGR2GRAY ) #转灰度
#image = cv.cvtColor(cv_image, cv.COLOR_BGR2RGB )

width = int(cv_image.shape[0] / 2)
height = int(cv_image.shape[1] / 2)
image = cv.resize(cv_image, (height, width), interpolation=cv.INTER_CUBIC)

cv.imshow('downsample', image)
cv.waitKey(0)
cv.imwrite('destination', image)
cv.destroyAllWindows()
