import tensorflow as tf
from PIL import Image
import numpy as np

img_path="C:/Users/Administrator/Desktop/summer/1.jpg"

def prepare_image_data(img_path):
    #return image_batch [batch, width, height, channel]
    img_raw_data=tf.gfile.FastGFile(img_path, 'rb').read()
    img_data=tf.image.decode_jpeg(img_raw_data, channels=3)
    img_data=tf.expand_dims(img_data, axis=0)
    img_data=tf.image.resize_bilinear(img_data, size=[512,512])
    return img_data

def prepare_image_data2():
    #return image_batch [batch, width, height, channel]
    img_data=np.random.randint(0,255,[1,4,4,6])
    img_data=tf.cast(img_data, dtype=tf.float32)
    return img_data

def phaseShift(inputs, shape_1, shape_2):
    X=tf.reshape(inputs, shape_1)
    X=tf.transpose(X, [0,1,3,2,4])
    return tf.shape(X, shape_2)

def pixelShuffle(inputs, scale=1):
    size=tf.shape(inputs)
    batch_size=size[0]
    h=size[1]
    w=size[2]
    c=size[3]
    
    channel_target=c//(scale*scale)
    channel_factor=c//channel_target
    
    shape_1=[batch_size, h, w, channel_factor//scale, channel_factor//scale]
    shape_2=[batch_size, h*scale, w*scale, 1]
    
    input_split=tf.split(inputs, channel_target, axis=3)
    output=tf.concat([phaseShift(x, shape_1, shape_2) for x in input_split], axis=3)
    
    return output

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    

    























