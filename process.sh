#!/bin/bash

#Get the training files first
Train=/home/jishnu/Datasets/Bengali/BTrain/*
Test=/home/jishnu/Datasets/Bengali/BTest/*

let "i=1"

#Rotate some images in training files
for file in $Train
do
    echo "Iteration $i: Processing training file $file"
    if [ $i -gt 3000 -a $i -lt 3500 ]
    then
        echo "Rotation by 90 degrees"
        convert $file -rotate 90 $file
    fi
    if [ $i -gt 3500 ]
    then
        echo "Rotation by 180 degrees"
        convert $file -rotate 180 $file
    fi
    let "i=i+1"
done

#Rotate some images in testing files
let "i=1"
for file in $Test
do
    echo "Iteration $i: Processing testing file $file"
    if [ $i -gt 1800 -a $i -lt 1900 ]
    then
        echo "Rotation by 90 degrees"
        convert $file -rotate 90 $file
    fi
    if [ $i -gt 1900 ]
    then
        echo "Rotation by 180 degrees"
        convert $file -rotate 180 $file
    fi
    let "i=i+1"
done

#./caffe/runit.sh
