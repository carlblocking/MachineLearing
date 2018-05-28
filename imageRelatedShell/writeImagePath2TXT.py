import os
from PIL import  Image, ImageStat
rootdir='D:/tf_image_segmentation/TF-My-Resnet-Car-head/img/label'
list=os.listdir(rootdir)
totalNumber=len(list)

def GetFileNameAndExt(filename):
    (filepath,tempfilename) = os.path.split(filename);
    (shotname,extension) = os.path.splitext(tempfilename);
    return shotname

f=open('C:/Users/Administrator/Desktop/train.txt','w')
for i in range(0,len(list)):
    path=os.path.join(rootdir,list[i])
    if os.path.isfile(path):
#         im02=Image.open(path)
#         stat=ImageStat.Stat(im02)
#         stat2=stat.mean
#         if (not(stat2[0]==0 and stat2[1]==0 and stat2[2]==0)):
#             print(stat2[0],stat2[1],stat2[2])
            namess=GetFileNameAndExt(list[i])
            print('/source/'+namess+'.jpg' +' '+'/label/'+namess+'.png')
            f.write('/source/'+namess+'.jpg' +' '+'/label/'+namess+'.png'+'\n')
f.close()
