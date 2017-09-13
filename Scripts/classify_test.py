""" Script to classify test set images based on a given trained LeNet model. """
import caffe
import lmdb
import os
import caffe.proto.caffe_pb2
from caffe.io import datum_to_array
import numpy as np
import sys

import caffe
caffe.set_mode_cpu()

#Creating the neural net on which the test is to be run
path1_model = "/home/jishnu/Models/Max pooling/lenet_iter_10000.caffemodel" #trained from lenet_train_test.prototxt
path2_model = "/home/jishnu/caffe/models/lenet_iter_10000.caffemodel" #trained from lenet.prototxt

path_prototxt = "/home/jishnu/caffe/examples/mnist/lenet.prototxt"

net = caffe.Classifier(path_prototxt, path1_model)

lmdb_env = lmdb.open('/home/jishnu/caffe/examples/imagenet/mymnist_test_lmdb')
lmdb_txn = lmdb_env.begin()
lmdb_cursor = lmdb_txn.cursor()
datum = caffe.proto.caffe_pb2.Datum()

i = 1

for key, value in lmdb_cursor:
    print ("-----------------------------------Iteration", i)
    #print ("key: ", key)    
    datum.ParseFromString(value)
    label = datum.label #l
    data = caffe.io.datum_to_array(datum) #f
    pred = net.predict(data)
    print pred
    #for d in data:
            #print d
            #print "label: ",label
    #for d in data:
    #    for i in d:
    #        print i
    #out = net.forward(**{net.inputs[0]: np.asarray([data])})
    #print "Output prob: ",out
    #print data
    print "Label: ",label
    i = i+1
