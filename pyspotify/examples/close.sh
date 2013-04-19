#!/bin/bash
echo Please input list file name:
read listn
for file in `cat $listn`
do
send_file $file
done
