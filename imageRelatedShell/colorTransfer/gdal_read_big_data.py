#coding=utf-8
import tensorflow as tf
import cv2
from PIL import Image
import numpy as np
from osgeo import gdal

color_image="C:/Users/Administrator/Desktop/1.tif"
gradient_image="C:/Users/Administrator/Desktop/2.tif"
save_dir="C:/Users/Administrator/Desktop/mean/"

def conver_image_to_tensor(img_path):
    #the image has been divided by 255
    img_data=gdal.Open(img_path)
    width=img_data.RasterXSize
    height=img_data.RasterYSize
    img_data=img_data.ReadAsArray(0,0,width, height)
    img_data=np.stack([img_data[2], img_data[1], img_data[0]], axis=2)
    img_data=tf.cast(img_data, tf.float32)/255
    return img_data

def image_gradient(img_data):
    #first, convert image to gray scale image
    #second: figure image's gradient in the direction of X and Y
    #third: multiply and sqrt
    #forth: convert one channel image into three channel image
    img_data=tf.image.rgb_to_grayscale(img_data)
    img_data_x=tf.pad(img_data, [[0,0],[0,1],[0,0]], mode='REFLECT')
    img_data_y=tf.pad(img_data, [[0,1],[0,0],[0,0]], mode='REFLECT')
    img_data_x=img_data_x[:,1:,:]-img_data_x[:,:-1,:]
    img_data_y=img_data_y[1:]-img_data_y[:-1]
    return img_data_x, img_data_y

def figure_phi_and_psi(img_data_x, img_data_y):
    step1=tf.multiply(img_data_x, img_data_x)+tf.multiply(img_data_y, img_data_y)
    step2=tf.sqrt(step1)
    step3=tf.concat([step2,step2,step2], axis=2)
    psi=tf.minimum(255.*step3/5., 1)
    phi=30./(1.+100.*step3)
    return psi, phi
    

# test_data1=np.random.randint(0,3,(2,2,3))
# test_data2=np.random.randint(0,3,(2,2,3))
# 
# test_data1=tf.cast(test_data1, tf.float32)
# test_data2=tf.cast(test_data2, tf.float32)
# 
# # result=tf.matmul(test_data1, test_data2)#错误的使用
# result=tf.multiply(test_data1, test_data2)#推荐使用

gradient_image_data=conver_image_to_tensor(gradient_image)
color_image_data=conver_image_to_tensor(color_image)
target_image=tf.Variable(color_image_data)

gradient_image_data_x,gradient_image_data_y=image_gradient(gradient_image_data)
color_image_data_x, color_image_data_y=image_gradient(target_image)

psi, phi=figure_phi_and_psi(gradient_image_data_x, gradient_image_data_y)

sum1=tf.square(color_image_data_x-gradient_image_data_x)+tf.square(color_image_data_y-gradient_image_data_y)
sum1=tf.multiply(sum1, phi)
sum2=tf.square(target_image-color_image_data)
sum2=tf.multiply(sum2,psi)

loss=tf.reduce_mean(sum1)+tf.reduce_mean(sum2)
# loss=tf.reduce_sum(sum1)+tf.reduce_sum(sum2)
train_step=tf.train.AdamOptimizer(0.001).minimize(loss)

# phi_mean, phi_variance=tf.nn.moments(phi, [0,1,2])
# phi_max=tf.reduce_max(phi)
# phi_min=tf.reduce_min(phi)
# 
# psi_mean, psi_variance=tf.nn.moments(psi, [0,1,2] )
# psi_max=tf.reduce_max(psi)
# psi_min=tf.reduce_min(psi)

with tf.Session() as sess:
    print("start")
    sess.run(tf.global_variables_initializer())
    for i in range(1,1001):
        sess.run(train_step)
        if i % 100==0:
            print(loss.eval())
#             print("phi的平均值是:", phi_mean.eval(), "\t方差为:", phi_variance.eval(), "\t最大值为：",phi_max.eval(), "\t最小值为：", phi_min.eval())
#             print("psi的平均值是:", psi_mean.eval(), "\t方差为:", psi_variance.eval(), "\t最大值为：",psi_max.eval(), "\t最小值为：", psi_min.eval())
            image_array=np.array(target_image.eval()*255, dtype='float32')
            image_array=np.abs(image_array)
            image_array=cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
            cv2.imwrite(save_dir+"{}.png".format(str(i)), image_array)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    