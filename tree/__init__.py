#encoding=utf-8
from math import *
import operator
def calShannonEnt(dataSet):
    numEntries=len(dataSet)
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEnt=0.0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        shannonEnt-=prob*log(prob,2)
    return shannonEnt

def createDataSet():
    dataSet=[[1,1,'yes'],
             [1,1,'yes'],
             [1,0,'no'],
             [0,1,'no'],
             [0,1,'no']]
    labels=['no sutfing','flippers']
    return dataSet,labels

#按照给定特征划分数据集
#函数的三个参数：待划分的数据集、划分数据集的特征、需要返回的特征类型     
def splitDataSet(dataSet,axis,value):
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reduceFeacVec=featVec[:axis]
            reduceFeacVec.extend(featVec[axis+1:])
            retDataSet.append(reduceFeacVec)
    return retDataSet

def chooseBestFeatureToSplit(datsSet):
    numfeatures=len(datsSet[0])-1
    #print numfeatures
    baseEntropy=calShannonEnt(datsSet)
    bestInfoGain=0.0;bestFeature=-1
    for i in range(numfeatures):
        fearList=[example[i] for example  in datsSet]
        uniqueVals=set(fearList)
        newEntropt=0.0
        for value in uniqueVals:
            subDataSet=splitDataSet(datsSet, i, value)
            prob=len(subDataSet)/float(len(datsSet))
            newEntropt+=prob*calShannonEnt(subDataSet)
        infoGaub=baseEntropy-newEntropt
        if(infoGaub>bestInfoGain):
            bestInfoGain=infoGaub
            bestFeature=i
    return bestFeature

def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount=sorted(classCount.iteritems(),operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def createTrees(dataSet,labels):
    classList=[example[-1] for example in dataSet]
    if classList.count(classList[0])==len(classList):
        return classList[0]
    if len(dataSet[0])==1:
        return majorityCnt(classList)
    bestFeat=chooseBestFeatureToSplit(dataSet)
    beatFeatLabel=labels[bestFeat]
    myTree={beatFeatLabel:{}}
    del(labels[bestFeat])
    featValues=[example[bestFeat] for example in dataSet]
    uniqueValues=set(featValues)
    for value in uniqueValues:
        subLabels=labels[:]
        myTree[beatFeatLabel][value]=createTrees(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree

def storeTree(inputTree,filename):
    import pickle
    fw = open(filename,'w')
    pickle.dump(inputTree,fw)
    fw.close()
    
def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)  
    
dataSets,labels=createDataSet()
print calShannonEnt(dataSets)

# #修改数据后香农熵变大
# dataSets[0][-1]='maybe'
# print dataSets
#print calShannonEnt(dataSets)
#print splitDataSet(dataSets, 0, 0)
#print splitDataSet(dataSets, 0, 1)
print chooseBestFeatureToSplit(dataSets)
print createTrees(dataSets, labels)


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    