path = '/test_images/gray_depth.png'
image = imread(path);
imshow(image);
imageinfo(image);
size = size(image);

double_image  = im2double(image);    % 把图像转换成double精度类型（0~1) or use double_image=double(img)/255; same as im2double(image)

uint8_image = im2uint8(double_image); %or use uint8_image=uint8(round(double_image*255));

imwrite(,'result.jpg');