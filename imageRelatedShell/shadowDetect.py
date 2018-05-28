from skimage import io, color, data
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import os

img_path="C:/Users/Administrator/Desktop/test/150401025034B.jpg"

def convert_2_HSV(img_path, i):
    img_data=cv2.imread(img_path)
    img_data=cv2.cvtColor(img_data, cv2.COLOR_BGR2HSV)
    img_save_path="C:/Users/Administrator/Desktop/test2/{}.jpg".format(str(i))
    cv2.imwrite(img_save_path,img_data)
    print(i, "done")

def deal_file_images(path):   
    g = os.walk(path)
    i=1
    for path,d,filelist in g:  
        for filename in filelist:
            if filename.endswith('jpg'):
                path1=os.path.join(path, filename)
                convert_2_HSV(path1, i)
                i+=1
                    
deal_file_images("C:/Users/Administrator/Desktop/test")

