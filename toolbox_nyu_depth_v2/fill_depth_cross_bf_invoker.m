imgPath = '../physical_world/rgb/';       
imgDir  = dir([imgPath '*.png']); 
depthpath = '../physical_world/depth/';
depthdir = dir([depthpath '*.png']);
for i = 1:length(imgDir)          
    rgb = imread([imgPath imgDir(i).name]); 
    depth = imread([depthpath depthdir(i).name]);
    depth = im2double(depth);
    filled_depth = depth;

    for j = 1:6
        filled_depth = fill_depth_cross_bf(rgb, filled_depth, 3, 3);
    end
    imwrite(filled_depth, [depthpath depthdir(i).name(1:end-4) '_filled' '.png'])
end




