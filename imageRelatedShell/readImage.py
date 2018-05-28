#coding=gb2312

import tensorflow as tf
from PIL import Image
from tensorflow.python.ops.image_ops_impl import ResizeMethod

#ʹ��PIL��ȡͼƬ��ʹ������ڲ���resize
def PIL_read_image(img_path):
    img_data=Image.open(img_path)
    img_data=img_data.resize((249,249), Image.NEAREST)#�����
#     img_data=img_data.resize((249,249), Image.BILINEAR)#˫����
    return img_data

#ʹ��tensorflow��ȡͼƬ�����أ�height, width, channel��ͼƬ
def tf_read_image(img_path):
    img_raw_data=tf.gfile.FastGFile(img_path, "rb").read()
    #��ȡpngͼƬ������ͨ�������������channel=1����ԭͼƬΪ�Ҷ�ͼ
    #��ֻ��ȡһ��ͨ��
    img_data=tf.image.decode_png(img_raw_data, channels=3)
    
#     #jpg������ͨ�������������channel=1����ԭͼƬΪ�Ҷ�ͼ
#     #��ֻ��ȡһ��ͨ��
#     img_data=tf.image.decode_jpeg(img_raw_data, channels=3)

    img_data=tf.cast(img_data, dtype=tf.float32)
    img_data=tf.image.resize_images(img_data, [249,249], method=ResizeMethod.NEAREST_NEIGHBOR)#����ڲ�����resize
    return img_data
    