while read img;
  do scp "elgordo:./projects/convnet-demo/train/${img}.jpg" train;
done < catalogs/train.filenames

while read img;
  do scp "elgordo:./projects/convnet-demo/test/${img}.jpg" test;
done < catalogs/test.filenames
