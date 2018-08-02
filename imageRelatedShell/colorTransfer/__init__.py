# from osgeo import gdal
# import numpy as np
# import cv2
# import sys
# import math
# 
# epsilon=sys.float_info.epsilon
# img_path="C:/Users/Administrator/Desktop/1.jpg"
# 
# img_data=cv2.imread(img_path)/255
# img_data=np.array(img_data)
# 
# #three channels
# def figure_diff(input_image):
#     input_image_x=np.pad(input_image, ((0,0),(0,1),(0,0)), 'reflect')
#     input_image_y=np.pad(input_image, ((1,0),(0,0),(0,0)), 'reflect')
#     
#     diff_x=input_image_x[:,1:]-input_image_x[:,:-1]
#     diff_y=input_image_y[1:]-input_image_y[:-1]
#     
#     return diff_x, diff_y
# 
# def figure_matrix_sum(input_data):
#     diff_x, diff_y=figure_diff(input_data)
#     output=np.sqrt(np.sum(diff_x**2+diff_y**2,2))
#     return output
# 
# 
# output=figure_matrix_sum(img_data)
# psi=np.where(256*output/5>1,1,256*output/5)
# print(psi)
# output=30./(1+10*output)
# print(output)
# -----------------------------------------------------------------------------------------------
import numpy as np
data=np.random.randint(0,5,(5,5))
print(data)
print(data[0][:-1])





























