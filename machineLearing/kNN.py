#encoding=utf-8
'''
Created on 2016年12月7日

@author: xxw
'''
# K邻近算法的步骤
# 对位置类别属性的数据集中的每个点执行以下操作
# 1）计算已知类别数据集中的点与当前点之间的距离
# 2）按照递增的次序一次排列
# 3）选取当前与数据点距离最小的K个点
# 4）确定前K个点类别的出现频率
# 5）返回K个点出现频率最大的点，返回其类别作为预测的类别
from numpy import *
import operator
from matplotlib.pyplot import axis
from numpy.oldnumeric.arrayfns import reverse
def createDataSet():
    group=([1.0,1.1],[1.0,1.0],[0,0],[0,0.1])
    labels=['A','A','B','B']
    return group,labels

#intX为用于分类的数据向量，dataSet为训练样本集，labels为标签向量，k为选择的K值
def classify0(intX,dataSet,labels,k):
    #计算距离
    dataSetSize=len(dataSet)
    diffMat=tile(intX, (dataSetSize,1))-dataSet
    sqDiffMat=diffMat**2
    sqDistance=sqDiffMat.sum(axis=1)
    distance=sqDistance**0.5
    sortedDistance=distance.argsort()
    classCount={}
    #选择距离最小的k个点
    for i in range(k):
        voteLabel=labels[sortedDistance[i]]
        classCount[voteLabel]=classCount.get(voteLabel,0)+1
    #排序
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

# group,labels=createDataSet()
# print group
# print labels

    
group,labels=createDataSet()
test=[1.1,1.3]
print classify0(test, group, labels, 3)





