#!/usr/bin/env bash

number=$1
x=1
while [ $x -le $number ]
do
    echo $x
    ((x++))
done

echo "Loop finished"
exit 0