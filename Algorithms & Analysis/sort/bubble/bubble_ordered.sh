for ((i=500; i<=10000; i+=500));
do
    /usr/bin/time python3 bubble_sort_ordered.py $i > ./test/ordered/bubble_test_$i.txt
done
