clear all   %limpiamos el historial de matlab

%contador de la cantidad en € en una imagen en función de las monedas y de su valor.

im_rgb=imread('monedas.jpg','jpg');    %leemos la imagen con las monedas
figure(1),imshow(im_rgb)               %Representamos la imagen original para poder compararla mas adelante
Im_bin=imbinarize(im_rgb,0.7);              %Cambiamos la imagen a tipo binario para poder manejarla con las siguientes secuencias
Im_bin=not(Im_bin);                    %negamos la imagen, es decir, cambiamos los 1 por 0 y viceversa en cada pixel de la misma.
monedasimagen=imfill(Im_bin,'hole');   %relleno el interior de las circulos en la imagen que se corresponden con las monedas.
figure(2),imshow(monedasimagen)
[a b]=bwlabel(monedasimagen,8);


propiedades=regionprops(a,'area','centroid','BoundingBox');
moneda1=0;moneda2=0;moneda5=0;moneda10=0;moneda20=0;moneda50=0;moneda100=0;moneda200=0;
[w v]=size(propiedades(:,1))
%calculo del area de las monedas( solo si aparecen todas las monedas en la
%imagen, en caso contrario tendriamos que hacer un script especifico para dicha imagen editando este script)
for (i=1:w)
    area(i)=propiedades(i).Area;
end
%eliminar elementos repetido del vector area:
area=sort(area);
salir=0;
i=1;
while salir==0
    if (i>(w-2))
        salir=1;
    end
    if (area(i+1)-area(1)/100)<=area(i) && area(i)<=(area(i+1)+area(1)/100);
        for j=i+1:w-1
            variable=area(j+1);
            area(j+1)=area(j);
            area(j)=variable;
        end
        w=w-1; 
    else
        i=i+1;
    end
    
end


 area1=area(1);
 area2=area(2);
 area10=area(3);
 area5=area(4);
 area20=area(5);
 area100=area(6);
 area50=area(7);
 area200=area(8);


%aqui se acaba el calculo del area y comienza la comparacion de las monedas
%para obtener su valor 
total=0;
for i=1:size(propiedades,1)
    rectangle('position',propiedades(i).BoundingBox,'edgecolor','r','linewidth',3)
    centro=propiedades(i).Centroid;
    x=centro(1);y=centro(2);
    propiedades(i).Area
    if  propiedades(i).Area<=area1+area(1)/100
        text(x-area(8)/2400,y,'1 ')
        total=total+0.01;
        moneda1=moneda1+1;
    elseif propiedades(i).Area<=area2+area(1)/100
        text(x-area(8)/2400,y,'2 ')
        total=total+0.02;
        moneda2=moneda2+1;
    elseif propiedades(i).Area<=area10+area(1)/100
        text(x-area(8)/2000,y,'10 ')
        total=total+0.10;
        moneda10=moneda10+1;
    elseif propiedades(i).Area<=area5+area(1)/100
        text(x-area(8)/2400,y,'5 ')
        total=total+0.05;
        moneda5=moneda5+1;
    elseif propiedades(i).Area<=area20+area(1)/100
        text(x-area(8)/1500,y,'20 ')
        total=total+0.20;
        moneda20=moneda20+1;
    elseif propiedades(i).Area<=area100+area(1)/100
        text(x-area(8)/1500,y,'100 ')
        total=total+1;
        moneda100=moneda100+1;
    elseif propiedades(i).Area<=area50+area(1)/100
        text(x-area(8)/1500,y,'50 ')
        total=total+0.5;
        moneda50=moneda50+1;
    elseif propiedades(i).Area<=area200+area(1)/100
        text(x-area(8)/1500,y,'200 ')
        total=total+2;
        moneda200=moneda200+1;
    end

end
    sprintf('total de dinero:%0.2f € ',total)