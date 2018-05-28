import os
from PIL import  Image, ImageStat
rootdir='C:/Users/Administrator/Desktop/source'
list=os.listdir(rootdir)
totalNumber=0
R=0
G=0
B=0


for i in range(0,len(list)):
    path=os.path.join(rootdir,list[i])
    if os.path.isfile(path):
        im02=Image.open(path)
        stat=ImageStat.Stat(im02)
        stat2=stat.mean
        if (not(stat2[0]==0 and stat2[1]==0 and stat2[2]==0)):
            R+=stat2[0]
            G+=stat2[1]
            B+=stat2[2]
            print(stat2[0],stat2[1],stat2[2])
            totalNumber+=1
            
print(totalNumber)
print(R/totalNumber)
print(G/totalNumber)
print(B/totalNumber)


    