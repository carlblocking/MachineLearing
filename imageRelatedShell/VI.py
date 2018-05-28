import cv2
import matplotlib.pyplot as plt

img_path="C:/Users/Administrator/Desktop/test2/6.jpg"


def green(img_path):
    img=cv2.imread(img_path)
    h=img.shape[0]
    w=img.shape[1]
    for i in range(0,h):
        for j in range(0, w):
            b=img[i,j,0]
            g=img[i,j,1]
            r=img[i,j,2]
            value=(2*g-r-b)/(2*g+r+b)
            if(value>0.05):
                img[i,j]=[0,255,0]
    cv2.imwrite("C:/Users/Administrator/Desktop/test2/6.png", img)
    
green(img_path)