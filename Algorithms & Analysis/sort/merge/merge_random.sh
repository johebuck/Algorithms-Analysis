#!/bin/bash

for ((i=500; i<=10000; i+=500));
do
    /usr/bin/time python3 merge_sort_random.py $i > ./test/random/merge_test_$i.txt
done

