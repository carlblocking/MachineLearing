#coding=gb2312

import tensorflow as tf
from PIL import Image
from tensorflow.python.ops.image_ops_impl import ResizeMethod

#使用PIL读取图片并使用最近邻采样resize
def PIL_read_image(img_path):
    img_data=Image.open(img_path)
    img_data=img_data.resize((249,249), Image.NEAREST)#最近邻
#     img_data=img_data.resize((249,249), Image.BILINEAR)#双线性
    return img_data

#使用tensorflow读取图片，返回（height, width, channel）图片
def tf_read_image(img_path):
    img_raw_data=tf.gfile.FastGFile(img_path, "rb").read()
    #读取png图片，三个通道都解析，如果channel=1或者原图片为灰度图
    #则只读取一个通道
    img_data=tf.image.decode_png(img_raw_data, channels=3)
    
#     #jpg，三个通道都解析，如果channel=1或者原图片为灰度图
#     #则只读取一个通道
#     img_data=tf.image.decode_jpeg(img_raw_data, channels=3)

    img_data=tf.cast(img_data, dtype=tf.float32)
    img_data=tf.image.resize_images(img_data, [249,249], method=ResizeMethod.NEAREST_NEIGHBOR)#最近邻采样并resize
    return img_data
    