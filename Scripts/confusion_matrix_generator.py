""" Script to generate confusion matrices following classification of test images."""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import caffe


#Command line parameters are of the form <model number> <number of rotated images>
#Set the mode of caffe use
caffe.set_mode_cpu()
path = "/home/jishnu/caffe/examples/mnist/lenet.prototxt"
#pathave = "/home/jishnu/caffe/examples/mnist/lenet_ave.prototxt"
#path2 = "/home/jishnu/Models/Max pooling/lenet_iter_10000.caffemodel"
#path2ave = "/home/jishnu/Models/Average Pooling/lenet_iter_10000.caffemodel"
#path3 = "/home/jishnu/caffe/models/lenet_iter_10000.caffemodel"

ls = sys.argv[1:]
model_num = int(ls[0])
num_rotated_images = int(ls[1])
model_path = "/home/jishnu/Trained models/model" + str(model_num) + ".caffemodel"


net_max = caffe.Net(path, model_path, caffe.TEST)
#net_ave = caffe.Net(pathave, path2ave, caffe.TEST)

#Names of the input layers in the net are given by the following
#print net.inputs
#net.blobs for input data etc and net.params a vector of blobs for weight and bias parameters

#im = np.array(Image.open('/home/jishnu/Datasets/Bengali/BTrain/bn00000.jpg'))
#im_input = im[np.newaxis, np.newaxis, :, :]
#net.blobs['data'].reshape(*im_input.shape)
#net.blobs['data'].data[...] = im_input

#net.forward()

#configuring the preprocessing of data
transformer_max = caffe.io.Transformer({'data': net_max.blobs['data'].data.shape})
#transformer.set_mean('data', np.load('python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1))
transformer_max.set_transpose('data', (2,0,1))
transformer_max.set_channel_swap('data', (2,1,0))
transformer_max.set_raw_scale('data', 255.0)

#transformer_ave = caffe.io.Transformer({'data': net_ave.blobs['data'].data.shape})
#transformer_ave.set_transpose('data', (2,0,1))
#transformer_ave.set_channel_swap('data', (2,1,0))
#transformer_ave.set_raw_scale('data', 255.0)

#Since we are classifying one image we set the batch size to 1
net_max.blobs['data'].reshape(1,3,32,32)
#net_ave.blobs['data'].reshape(1,3,32,32)

testpath = "/home/jishnu/Datasets/Bengali/BTest/"
fls = sorted(os.listdir("/home/jishnu/Datasets/Bengali/BTest"))
num_images = len(fls)

#Creating 2-d array for storing the confusion matrix
conf_mat = [[0 for x in range(10)] for x in range(10)]

for i in range(num_images - num_rotated_images, num_images):
    pathimage = testpath + fls[i]        
    im = caffe.io.load_image(pathimage)
    net_max.blobs['data'].data[...] = transformer_max.preprocess('data', im)
    out_max = net_max.forward();
    o1 = out_max['prob'].argmax()
    label = i%10
    conf_mat[label][o1] = conf_mat[label][o1] + 1
    
#Printing the confusion matrix
for i in range(10):
    for j in range(10):
        print conf_mat[i][j],
    print






"""
#Creating the file to store the results
fobj = open("res.txt", "w+")


#Loading the image in the data layer
x = 5500
for i in range(0,500):
    y = x + i
    image_path = '/home/jishnu/Datasets/Bengali/BTest/bn0'+str(y)+'.jpg'
    im = caffe.io.load_image(image_path)
    net_max.blobs['data'].data[...] = transformer_max.preprocess('data', im)
    net_ave.blobs['data'].data[...] = transformer_ave.preprocess('data', im)
    out_max = net_max.forward()
    out_ave = net_ave.forward()
    o1 = out_max['prob'].argmax()
    o2 = out_ave['prob'].argmax()
    label = i%10
    strn = str(i+1)+'\t'+str(o1)+'\t'+str(o2)+'\t'+str(o1)+'\t'+str(label)+'\n'
    fobj.write(strn)

fobj.close()

#compute classified result
#out = net.forward()

#print out['prob'].argmax()
"""

