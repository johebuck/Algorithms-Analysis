for ((i=500; i<=10000; i+=500));
do
    /usr/bin/time python3 randomized_quick_sort_ordered.py $i > ./test/ordered/insertion_test_$i.txt
done
