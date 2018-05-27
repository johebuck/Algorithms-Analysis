#!/bin/bash

for ((i=500; i<=10000; i+=500));
do
    /usr/bin/time python3 insertion_sort_ordered.py $i > ./test/insertion_test_$i.txt
done

