for ((i=500; i<=10000; i+=500));
do
    /usr/bin/time python3 selection_sort_ordered.py $i > ./test/ordered/selection_test_$i.txt
done
