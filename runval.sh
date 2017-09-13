#!/bin/bash

./makedata 0 0 300 2999
mv train.txt train1.txt
./makedata 0 299 600 2999
mv train.txt train2.txt
./makedata 0 599 900 2999
mv train.txt train3.txt
./makedata 0 899 1200 2999
mv train.txt train4.txt
./makedata 0 1199 1500 2999
mv train.txt train5.txt
./makedata 0 1499 1800 2999
mv train.txt train6.txt
./makedata 0 1799 2100 2999
mv train.txt train7.txt
./makedata 0 2099 2400 2999
mv train.txt train8.txt
./makedata 0 2399 2700 2999
mv train.txt train9.txt
./makedata 0 2699 0 0
mv train.txt train10.txt
