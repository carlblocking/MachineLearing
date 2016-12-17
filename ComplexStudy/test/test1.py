#encoding=utf-8
from numpy import *
from matplotlib.pyplot import axis
import operator
# group=array([[1.1,1.0],[1.0,1.2],[3.0,3.2],[3.5,0.2],[5.5,6.5],[4.3,5.3]])
# #numpy中的array,其shape[0]表示相应矩阵的行，shape[1]表示相应矩阵的列
# print group.shape[0]
# print group.shape[1]
# #axis=0表示列相加，1表示行相加
# print group.sum(axis=0)
# print group.sum(axis=1)
# #argsort返回的是从小到大排序结果的索引
# print group.sum(axis=1).argsort()
# #sorted函数中，第一个参数为要排序的对象，第二个使用operator包中的operator对象的itemgetter方法，该方法的参数为对应元素的下表，第三个参数为是否反转，默认为
# #false，即从小到大排列，当为True的时候，表示从打到小排列
# print sorted(group,key=operator.itemgetter(0),reverse=True)
# group2={'lisa':98,'minica':99,'hana':86}
# # print sorted(group2.iteritems(),key=operator.itemgetter(0),reverse=True)
# group2['lilllt']=group2.get('lilllt',0)
# group2['lisa']=group2.get('lisa',0)+1
# print group2
originMatrix=array([[1.2,6.3],[3.2,5.3],[4.5,4.6],[5.3,1.2],[1.2,1.9],[9.4,8.7],[5.6,7.1],[4.2,5.3],[5.5,6.3]])
testMatrix=array([1.2,6.5])
dataSetSize=originMatrix.shape[0]
diffMatrix=tile(testMatrix, (dataSetSize,1))-originMatrix
#print diffMatrix
sqDistanceMatrix2=diffMatrix**2
sqDistanceMatrix=sqDistanceMatrix2**0.5
#print sqDistanceMatrix
TotalDistanceMatrix=sqDistanceMatrix.sum(axis=1)
# print TotalDistanceMatrix
sortedOrder= TotalDistanceMatrix.argsort()
for i in range(3):
    print TotalDistanceMatrix[sortedOrder[i]]
    print originMatrix[sortedOrder[i]]
