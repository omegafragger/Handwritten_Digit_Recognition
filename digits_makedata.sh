#!/bin/bash

#This script copies the given images to training and test folders

numParam=$# #contains the bounds of the training set, the rest is the test set

sourceFiles=/home/jishnu/Datasets/Bengali/BengaliJPGSML/*
destPath='/home/jishnu/Digits/Bengali/BengaliTrain/'
valPath='/home/jishnu/Digits/Bengali/BengaliTest/'

#handling two possible cases
let "i=0"
for file in $sourceFiles
do
    let "p=i%10"
    compPath=$destPath$p
    if (( $i >= 5000 ))
    then
        testPath=$valPath$p
        cp $file $testPath
    fi
    echo $compPath
    cp $file $compPath
    let "i=i+1"
done


