from numpy import * 
import matplotlib.pyplot as plt
import numpy
# x=random.rand(50)
# y=random.rand(50)
# print x
# print y
# colors=random.rand(50)
# area=numpy.pi*(random.randint(50))**2
# plt.scatter(x, y, c=colors)
# plt.show()
filePath='F:\\ML\\MLdata\\Ch06\\testSet.txt'
def loadDataSet(file):
    dataX=[]
    dataY=[]
    fr=open(file)
    for line in fr.readlines():
#         smallArray=line.strip().split('\t');
#         dataMat.append(smallArray)
        x=line.strip().split('\t')[0]
        y=line.strip().split('\t')[1]
        dataX.append(double(x))
        dataY.append(double(y))
    return dataX,dataY

dataX,dataY= loadDataSet(filePath)
x=dataX
y=dataY
color=random.rand(100)
plt.scatter(x, y, c=color )
plt.show()







