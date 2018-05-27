#!/bin/bash

for ((i=500; i<=10000; i+=500));
do
    /usr/bin/time python3 Counting_Sort_Random.py $i > ./test/random/random_test_$i.txt
done