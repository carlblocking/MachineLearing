from osgeo import gdal
import numpy as np
import cv2

def read_big_data(img_path):
#     dataType=gdal.GDT_Byte
#     driver=gdal.GetDriverByName("Gtiff")
    img_data=gdal.Open(img_path)
    width=img_data.RasterXSize
    height=img_data.RasterYSize
    img_data=img_data.ReadAsArray(0,0,width, height)
    print(img_data)
    print(type(img_data))
    print(img_data.shape)
    
    out_data=np.stack([img_data[2], img_data[1], img_data[0]], axis=2)
    
    print(out_data.shape)
    print(type(out_data))
    cv2.imwrite("C:/Users/Administrator/Desktop/11.tif", out_data)
    
read_big_data("C:/Users/Administrator/Desktop/1/1.tif")


























