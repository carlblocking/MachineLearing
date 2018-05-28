#coding=gb2312
from PIL import Image
import cv2

img_path="C:/test/1.jpg"

#一阶拉普拉斯
def laplacian_1(img_path):
    im=cv2.imread(img_path)
    im=cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    [h,w]=im.shape[:2]
    h1=int(h/4)
    w1=int(w/4)
    im2=cv2.resize(im, (w1, h1))
    im2=cv2.resize(im2, (w, h))
    im=im-im2
    cv2.imwrite("C:/Users/Administrator/Desktop/1.png", im)
    
laplacian_1(img_path)