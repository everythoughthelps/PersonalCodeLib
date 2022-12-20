img = imread('test.jpg'); % the type of img is uint8 (0~255)
I1  = im2double(img);    % uint8 to double (0~1）
I2  = double(img)/255;   % uint8 to double, same with im2double
