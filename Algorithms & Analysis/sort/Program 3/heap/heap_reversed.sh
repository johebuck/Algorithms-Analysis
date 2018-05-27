for ((i=500; i<=10000; i+=500));
do
    /usr/bin/time python3 heap_sort_reverse.py $i > ./test/reversed/insertion_test_$i.txt
done
