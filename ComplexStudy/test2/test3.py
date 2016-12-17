#encoding=utf-8
#计算香农熵
from math import log
filePath="F:\\ML\\MLdata\\Ch03\\lenses.txt"
def createDataSet(filePath):
    fr=open(filePath)
    dataSet=[]
    for line in fr.readlines():
        str1= line.strip().split('\t')
        dataSet.append(str1)
    return dataSet

def calShannonEntropy(dataSet):
    numberLenth=len(dataSet)
    labelCounts={}
    for item in dataSet:
        currentLabel=item[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEntropy=0.0
    for keys in labelCounts:
            prob=float(labelCounts[keys])/numberLenth
            shannonEntropy-=prob*log(prob,2)
    return shannonEntropy

def calShannonEntropy2(dataSet,n):
    numberLenth=len(dataSet)
    labelCounts={}
    for item in dataSet:
        currentLabel=item[n]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEntropy=0.0
    for keys in labelCounts:
            prob=float(labelCounts[keys])/numberLenth
            shannonEntropy-=prob*log(prob,2)
    return shannonEntropy

def chooseBestFeature(dataSet):
    feature=len(dataSet[0])-1
    baseShannonEntropy=calShannonEntropy(dataSet)
    baseInfoGain=0.0
    bestFeature=-1
    for i in range(feature):
        new_list=[]
        for item in dataSet:
            new_list.append(item[i])
        tmpShannonEntropy=calShannonEntropy(new_list)
        print new_list
        infoGain=baseShannonEntropy-tmpShannonEntropy
        if(infoGain>baseInfoGain):
            baseInfoGain=infoGain
            bestFeature=i
    return bestFeature

def chooseBestFeature2(dataSet):
    feature=len(dataSet[0])-1
    baseShannonEntropy=calShannonEntropy(dataSet)
    baseInfoGain=0.0
    bestFeature=-1
    for i in range(feature):
        tmpShannonEntropy=calShannonEntropy2(dataSet,i)
        infoGain=baseShannonEntropy-tmpShannonEntropy
        if(infoGain>baseInfoGain):
            baseInfoGain=infoGain
            bestFeature=i
    return bestFeature
         
dataSet=createDataSet(filePath)
# # print calShannonEntropy(dataSet)
# print chooseBestFeature(dataSet)

# dataSet=[[1,1,'yes'],
#          [1,1,'yes'],
#          [1,0,'no'],
#          [0,1,'no'],
#          [0,1,'no']]

print calShannonEntropy(dataSet)
print chooseBestFeature2(dataSet)


        
        
        
        
        
        
