for ((i=500; i<=10000; i+=500));
do
    /usr/bin/time python3 MaxSubArray_Random.py $i > ./test/random/max_test_$i.txt
done
