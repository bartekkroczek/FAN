for i in *; 
do
    inkscape $i --export-png=`echo $i | sed -e 's/svg$/png/'`;
done
rm -f *.svg

for i in *;      
do
    convert $i -rotate 90 `echo $i | sed -e 's/_0.png$/_90.png/'`;
done

for i in *;      
do
    convert $i -rotate 180 `echo $i | sed -e 's/_0.png$/_180.png/'`;
done

for i in *;      
do
    convert $i -rotate 270 `echo $i | sed -e 's/_0.png$/_270.png/'`;
done
