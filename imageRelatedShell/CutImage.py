#coding=gb2312
import os
from PIL import Image

def splitImage(img_path, width, height, order):
    img=Image.open(img_path)
    row=img.size[0]//width
    col=img.size[1]//height
    i=1
    for r in range(col):
        for c in range(row):
            box=(c*width, r*height, (c+1)*width, (r+1)*height)
            img.crop(box).save("C:/Users/Administrator/Desktop/lr/"+str(order)+"-{}.png".format(str(i)))
            i+=1
    print(order,".jpg done")

def deal_file_images(path):   
    g = os.walk(path)
    i=1
    for path,d,filelist in g:  
        for filename in filelist:
            if filename.endswith('tif'):
                path1=os.path.join(path, filename)
                splitImage(path1, 100, 100, i)
                i+=1
                               

deal_file_images("C:/Users/Administrator/Desktop/4")



    