#coding=gb2312
import os
f=open('D:/caffe-master/examples/car_direction/train.txt','w')
for i in range(0,8):
    sub_rootdir='D:/caffe-master/examples/car_direction/train/{}'.format(str(i))
    sub_list=os.listdir(sub_rootdir)
    for j in range(0, len(sub_list)):
        print(str(i)+"/"+sub_list[j]+" "+str(i))
        f.write(str(i)+"/"+sub_list[j]+" "+str(i)+"\n")
f.close()
