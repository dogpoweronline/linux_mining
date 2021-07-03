#!/bin/bash

array=(seno spare chia flax chaingreen)

for item in ${array[*]}
do
    printf "%s-----------------------\n" $item
    . /home/user/git/$item-blockchain/activate && $item farm summary
done
