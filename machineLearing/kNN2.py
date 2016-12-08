#encoding=utf-8
from numpy import *

import operator
filePath="F:\\ML\\MLdata\\Ch02\\datingTestSet2.txt"
def file2matrix(filename):
    #打开文件，得到文件的行数
    fr=open(filename)
    arrayOLines=fr.readlines()
    numberOfLines=len(arrayOLines)
    #创建以0填充的矩阵
    returnMat=zeros((numberOfLines,3))
    classLabelVector=[]
    index=0
    #循环处理文件中的每行数据
    for line in arrayOLines:
        #使用函数line.strip()截取掉所有的回车字符
        line=line.strip()
        #使用"\t"截取数据列表
        listFromLine=line.split('\t')
        #选取前3个元素，赋值到特征矩阵中
        returnMat[index,:]=listFromLine[0:3]
        #-1表示列表中最后一列元素，将其存入标签向量中
        classLabelVector.append(int(listFromLine[-1]))
        index+=1
    return returnMat,classLabelVector


#归一化特征值
def autoNorm(dataSet):
    minVals=dataSet.min(0)
    maxVals=dataSet.max(0)
    ranges=maxVals-minVals
    normDataSet=zeros(shape(dataSet))
    m=dataSet.shape[0]
    normDataSet=dataSet-tile(minVals, (m,1))
    normDataSet=normDataSet/tile(ranges, (m,1))
    return normDataSet,ranges,minVals    

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

#测试分类器效果
def datingclastest():
    hoRatio=0.10
    datetingDataMat,datingLabels= file2matrix(filePath)
    normDataSet,ranges,minVals=autoNorm(datetingDataMat)
    m=normDataSet.shape[0]
    numTestVects=int(m*hoRatio)
    errorCount=0.0
    for i in range(numTestVects):
        classifierResult=classify0(normDataSet[i,:], normDataSet[numTestVects:m,:], datingLabels[numTestVects:m], 3)
        print "the classifier came back with :%d, the real answer is:%d"%(classifierResult,datingLabels[i])
        if(classifierResult!=datingLabels[i]):
            errorCount+=1.0
    print "the total error rate is :%f"%(errorCount/float(numTestVects))


# datetingDataMat,datingLabels= file2matrix(filePath)
# normDataSet,ranges,minVals=autoNorm(datetingDataMat)
# print datetingDataMat
# print datingLabels[0:20]
# print normDataSet
#datingclastest()

#正式测试判断
def classifyPerson():
    resultList=['not at all','in small doses','in large doses']
    percenTats=float(raw_input("你花多少时间打游戏（小于等于100的数字）"))
    ffMiles=float(raw_input('你的飞行距离'))
    iceCream=float(raw_input('你的冰淇淋消耗量'))
    datingDataMat,datingLabels=file2matrix(filePath)
    normMat,ranges,minVals=autoNorm(datingDataMat)
    inArr=array([ffMiles,percenTats,iceCream])
    classifierResult=classify0((inArr-minVals)/ranges, normMat, datingLabels, 3)
    print "you will probaply like this person:",resultList[classifierResult-1]

classifyPerson()
    
    
    
    
    
    
    
    
    
    
    
    
           




