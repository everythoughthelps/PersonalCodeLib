rgb = ''
depth = ''

rgb = imread(rgb)
depth = imread(depth)

rgb = im2uint8(rgb)
depth = im2double(depth)

mex -setup c++
% use mex mex_cbf_windows.cpp cbf_windows.cpp if you are using a pc
mex mex_cbf.cpp cbf.cpp
fill_depth_cross_bf(rgb, depth, 3, 3)