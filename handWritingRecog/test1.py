#encoding=utf-8
#使用k-近邻算法的手写识别系统
#1、收集数据：提供文本文件
#2、准备数据：编写函数classify0(),将图像格式转换为分类器使用的list格式
#3、分析数据：在Python命令提示符中检查数据，确保它符合要求
#4、训练算法：此步骤不适用于k-近邻算法
#5、测试算法：编写函数使用提供的部分数据集作为测试样本，测试样本与非测试样本的区别在与测试样本是已经完成分类的数据，如果预测分类与实际类别不同，
#                     则标记为一个错误
#6、使用算法：这个Demo没有完成这个步骤。

from numpy import *
import operator
import os
#准备工作：将图像转化为测试向量
def img2vector(filename):
    returnVector=zeros((1,1024))
    fr=open(filename)
    for i in range(32):
        lineStr=fr.readline()
        for j in range(32):
            returnVector[0,32*i+j]=int(lineStr[j])
    return returnVector

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


#测试手写识别系统
def handWritingClassTest():
    hwLabels=[]
    trainingFileList=os.listdir('trainingDigits')
    m=len(trainingFileList)
    trainingMat=zeros((m,1024))
    for i in range (m):
        fileNameStr=trainingFileList[i]
        fileStr=fileNameStr.split('.')[0]
        classNumStr=int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:]=img2vector('trainingDigits/%s'% fileNameStr)
    testFileList=os.listdir('testDigits')
    errorCount=0.0
    mTest=len(testFileList)
    for i in range(mTest):
        fileNameStr=testFileList[i]
        fileStr=fileNameStr.split('.')[0]
        classNumStr=int(fileStr.split('_')[0])
        vectorUnderTest=img2vector('testDigits/%s'% fileNameStr)
        classifierResult=classify0(vectorUnderTest,trainingMat,hwLabels,3)
        print "the classifier came back with:%d, the real answei is:%d "%(classifierResult,classNumStr)
        if(classifierResult!=classNumStr):errorCount+=1.0
    print "\n the total number of errors is :%d"%errorCount
    print "\n the total error rate is :%f"%(errorCount/float(mTest))

handWritingClassTest()











































































































