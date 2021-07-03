#!/bin/bash

array=(seno spare flax chaingreen chia)

for item in ${array[*]}
do
    printf "%s-----------------------\n" $item
    . /home/user/git/$item-blockchain/activate && $item farm summary
done

read -n 1 -s -r -p "Press any key to continue"
