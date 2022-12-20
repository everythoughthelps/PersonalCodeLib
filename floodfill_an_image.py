import cv2
import numpy as np

def image_fill(image):
    image_floodfill= image.copy()   #先创建一个副本
    mask = np.zeros([image_floodfill.shape[0]+2, image_floodfill.shape[1]+2, 1], np.uint8)   #根据副本形状建一个掩膜， 注意，长和宽必须要+2，类型只能是uint8
    #cv2.floodFill(image_copy, mask, (60, 60), (0, 0, 255), (50,50,50), (50,50,50), cv2.FLOODFILL_FIXED_RANGE)
    cv2.floodFill(image_floodfill, mask, (0, 0), 255)
    #（60,60）代表起始点；（0,0，255）代表填充颜色；loDiff=（50,50，50）代表只能填充比填充颜色小对应数值的点，upDiff同理
    cv2.imshow('flood_fill', image_floodfill)
    #cv2.imshow('mask', mask)
    image_floodfill_inv = cv2.bitwise_not(image_floodfill)
    cv2.imshow('flood_fill_inv', image_floodfill_inv)

    # Combine the two images to get the foreground.
    im_out = image + image_floodfill_inv
    cv2.imshow('foreground', im_out)

image = cv2.imread('./test_images/color_depth.png')    #原图
cv2.imshow('image', image)
image_fill(image)
c = cv2.waitKey(0)
cv2.destroyAllWindows()
