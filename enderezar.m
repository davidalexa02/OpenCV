%A4
imagen=imread('folio.jpg');

imshow(imagen)
fixedPoints=[0,0;297,0;0,210;297,210]
movingPoints=[851, 698;126, 2160;3252, 638;3883, 2202]

tform=fitgeotrans(movingPoints,fixedPoints,'projective')
%tform=projective2d(movingPOints,fixedPoints)
%Y =imwarp(imagen,tform,'OutputView')
[Y,ref]=imwarp(imagen,tform);
imshow(Y)