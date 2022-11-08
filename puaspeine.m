I = imread('peine1.jpg');
gI = rgb2gray(I);
imshow(gI)
bw = imbinarize(gI);
imshow(bw)
bw2 = bwareaopen(bw,2000);
imshow(bw2)
se = strel('disk',5);
J=imclose(bw2,se);
imshow(J)
I2 = bw2 - J;
I3 = not(I2); 
I3 = bwareaopen(not(I3),150);
I4 = not(I3);
imshow(I4)


cc = bwconncomp(not(I4),4)
cc.NumObjects
pua = false(size(I4));
pua(cc.PixelIdxList{1}) = true;
imshow(pua)
labeled = labelmatrix(cc);
whos labeled
RGB_label = label2rgb(labeled,'spring','c','shuffle');
imshow(RGB_label)

puadata = regionprops(cc,'basic')
pua_areas = [puadata.Area];
pua_areas(50)
[min_area, idx] = min(pua_areas)
pua = false(size(bw));
pua(cc.PixelIdxList{idx}) = true;
imshow(pua)
histogram(pua_areas)
title('Histogram of the colored pikes')
%imbinarize, imopen y strel%