#coding=utf-8
from osgeo import gdal
import numpy as np
import os

def readTif(fileName):
    dataset=gdal.Open(fileName)
    if dataset==None:
        print("can not open file "+fileName)
        return 
    im_width=dataset.RasterXSize
    im_height=dataset.RasterYSize
    im_channel=dataset.RasterCount 
    
#     im_data=dataset.ReadAsArray(0, 0, im_width, im_height)#获取数据
    im_geotrans=dataset.GetGeoTransform()#获得仿射矩阵信息
    im_proj=dataset.GetProjection()#获得投影信息
    print(im_geotrans)
    print(im_proj)
    print(im_width, im_height, im_channel)
    

def writeTiff(im_data, im_width, im_height, im_bands, im_geotrans, im_proj, path):
    if 'int8' in im_data.dtype.name:
        datatype=gdal.GDT_Byte
    elif 'int16' in im_data.dtype.name:
        datatype=gdal.GDT_UInt16
    else:
        datatype=gdal.GDT_Float32
    
    if len(im_data.shape)==3:
        im_bands, im_height, im_width=im_data.shape
    elif len(im_data.shape)==2:
        im_data=np.array([im_data])
    else:
        im_bands, (im_height, im_width)=1, im_data.shape
    
    driver=gdal.GetDriverByName("GTiff")
    dataset=driver.Create(path, im_width, im_height, im_bands, datatype)
    if(dataset!=None):
        dataset.SetGeoTransform(im_geotrans)
        dataset.SetProjection(im_proj)
    for i in range(im_bands):
        dataset.GetRasterBand(i+1).WriteArray(im_data[i])
    del dataset
    
def read_tif_write_to_jpg(fileName, out_path):
    dataset=gdal.Open(fileName)
    if dataset==None:
        print("can not open file "+fileName)
        return 
    if dataset.RasterCount!=3:
        print("not RGB image")
        return 
    datatype=gdal.GDT_Byte
    driver=gdal.GetDriverByName("Gtiff")
    dataset1=driver.Create(out_path, 512,512,3,datatype)
    im_data=dataset.ReadAsArray(0,0,512,512)
#     print(im_data.shape[0])
    for i in range(3):
        dataset1.GetRasterBand(i+1).WriteArray(im_data[i])
    del dataset1

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



if __name__=="__main__":
    in_path='C:/Users/Administrator/Desktop/lu'
    out_path='C:/Users/Administrator/Desktop/cut2'
    cut_image_using_gdal(in_path, out_path, 512)






























