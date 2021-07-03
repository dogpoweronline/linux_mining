#!/bin/bash

array=(seno spare flax chaingreen)

for item in ${array[*]}
do
    printf "%s-----------------------\n" $item
    . /home/user/git/$item-blockchain/activate && $item start farmer
done

. /home/user/git/chia-blockchain/activate && chia start all
