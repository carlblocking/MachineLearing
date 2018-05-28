import numpy as np
import tensorflow as tf

def weights_initializer(size, order=None):
    name="weights_{}".format(str(order))
    Weights=tf.Variable(tf.random_normal(size, name=name))
    return Weights

def net(inputs):
    weight1=weights_initializer([3,3,3,4], order=1)
    net=tf.nn.conv2d(inputs, weight1, strides=[1,1,1,1], padding='SAME', name='conv1')
    
    weight2=weights_initializer([3,3,4,8], order=2)
    net=tf.nn.conv2d(net, weight2, strides=[1,1,1,1], padding='SAME', name='conv2')
    
    weight3=weights_initializer([3,3,8,4], order=3)
    net=tf.nn.conv2d(net, weight3, strides=[1,1,1,1], padding='SAME', name='conv3')
    
    return net