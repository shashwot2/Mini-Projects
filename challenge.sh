#!/usr/bin/env bash

counter=0

while IFS='' read -r LINE
do
echo "LINE $COUNT: $LINE"
    if [ $COUNT -gt 9 ]
then
    break
fi
((COUNT++))
done < $1
