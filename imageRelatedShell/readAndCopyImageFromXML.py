from __future__ import absolute_import
#coding=utf-8
# from xml.dom.minidom import parse 
import xml.dom.minidom 
from PIL import Image


def test():
    DOMTree = xml.dom.minidom.parse("C:/Users/Administrator/Desktop/img7/train2_result.xml")
    Data = DOMTree.documentElement 
    Countrys = Data.getElementsByTagName("image") 
    img_dir='C:/Users/Administrator/Desktop/img7/'
    for country in Countrys:
        img_name=country.getAttribute('file')  
        file_name=img_dir+img_name
        img_data=Image.open(file_name)
        img_data.save("C:/Users/Administrator/Desktop/source/"+img_name)


test()



    

    

















            

