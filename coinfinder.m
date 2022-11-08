coin = imread('monedas.jpg');
[centers,radii] = imfindcircles(coin,[100 200],'ObjectPolarity','dark', ...
    'Sensitivity',0.95,'Method','twostage','EdgeThreshold',0.1)
imshow(coin)
h=viscircles(centers,radii);