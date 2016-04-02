for i in *; 
do
    inkscape $i --export-png=`echo $i | sed -e 's/svg$/png/'`;
done

for i in *;      
do
    convert $i -rotate 90 `echo $i | sed -e 's/.png$/_90.png/'`;
done

