from PIL import Image
import numpy as np

path = './test_images/gray_depth.png'

image = Image.open(path)
image.show()


array_image = np.array(image)
print(array_image.dtype)  # unit8
double_array_image = array_image / 255.0  # 将图像像素值变换到100...200 区间
print(array_image.dtype)  # float64
# 通过PIL中的fromarray方法将图片转换为uint8格式
uint8_array_image = Image.fromarray(np.uint8(double_array_image))
