from numpy import *
filePath='F:\\ML\\MLdata\\Ch06\\testSet.txt'
file=open(filePath)
dataArray=[]
for line in file.readlines():
    data=line.strip().split('\t')
    dataArray.append([float(data[0]),float(data[1])])
#print dataArray
dataArrayTest=mat(dataArray)
# m,n=shape(dataArray)
# print m,n


