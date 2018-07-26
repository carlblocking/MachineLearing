#coding=utf-8
from osgeo import gdal
import numpy as np
import os

#准备将路径下的文件进行切分,目前支持tif、TIF、jpg和JPG格式文件
def cut_image_using_gdal(input_dir, output_dir, size):
    g=os.walk(input_dir)
    #定义一些常量
    datatype=gdal.GDT_Byte#保存为8位图像
    driver=gdal.GetDriverByName("Gtiff")#定义驱动
    k=1
    for path, _, filelist in g:
        for filename in filelist:
            if filename.endswith('tif') or filename.endswith('TIF') or filename.endswith('jpg') or  filename.endswith('JPG'):
                path1=os.path.join(path, filename)
                img_data=gdal.Open(path1)
                if img_data==None:
                    print("can not open file "+path1)
                    continue
                if img_data.RasterCount!=3:
                    print("not RGB image")
                    continue
                width=img_data.RasterXSize
                height=img_data.RasterYSize
                row=width//size
                col=height//size
                i=1
#                 print(row*col)
                for r in range(col):
                    for c in range(row):
                        save_path=output_dir+"/"+str(k)+"-{}.jpg".format(str(i))
                        dataset1=driver.Create(save_path, size, size, 3, datatype)
                        save_data=img_data.ReadAsArray(c*size, r*size, size,size)
                        for j in range(3):
                            dataset1.GetRasterBand(j+1).WriteArray(save_data[j])
                        del dataset1
                        del save_data
                        i+=1
            print(filename+" done")
            k+=1

#非成对数据的准备
def prepare_data_for_unpair_training(input_path, output_path, output_size=512):
    input_a_style_image_path=input_path+'/A'
    input_b_style_image_path=input_path+'/B'
    if not os.path.exists(input_a_style_image_path):
        print(input_a_style_image_path, "not exist, pleanse create it and make sure there are images in this folder")
        return 
    if not os.path.exists(input_b_style_image_path):
        print(input_b_style_image_path, "not exist, please create it and make sure there are images in this folder")
        return 
    output_a_style_path=output_path+'/trainA'
    output_b_style_path=output_path+'/trainB'
    if not os.path.exists(output_a_style_path):
        os.makedirs(output_a_style_path)
    if not os.path.exists(output_b_style_path):
        os.makedirs(output_b_style_path)
    #cut a style image
    cut_image_using_gdal(input_a_style_image_path, output_a_style_path, output_size)
    cut_image_using_gdal(input_b_style_image_path, output_b_style_path, output_size)
    print('data preparation done')
        


if __name__=='__main__':
    prepare_data_for_unpair_training("C:/Users/Administrator/Desktop/A","C:/Users/Administrator/Desktop/B")
    





























