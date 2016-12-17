#encoding=utf-8
from numpy import *
import re
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1是攻击性文字，0是正常言论
    return postingList,classVec

def createVocabList(dataSet):
    vocabSet=set([])
    for document in dataSet:
        vocabSet=vocabSet|set(document)
    return list(vocabSet)

def setOfWords2Vec(vocabList,inputSet):
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]=1
        else:
            print "the word :%s is not in my vocabulary"%word
    return returnVec

def trainNB0(trainMatrix,trainCategory):
    numTrainDocs=len(trainMatrix)
    numWords=len(trainMatrix[0])
    pAbusive=sum(trainCategory)/float(numTrainDocs)
    p0Num=ones(numWords);plNum=ones(numWords)
    p0Deom=2.0;p1Denom=2.0
    for i in range(numTrainDocs):
        if trainCategory[i]==1:
            plNum+=trainMatrix[i]
            p1Denom+=sum(trainMatrix[i])
        else:
            p0Num+=trainMatrix[i]
            p0Deom+=sum(trainMatrix[i])
    p1Vect=log(plNum/p1Denom)
    p0Vect=log(p0Num/p0Deom)
    return p0Vect,p1Vect,pAbusive

def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    p1=sum(vec2Classify*p1Vec)+log(pClass1)
    p0=sum(vec2Classify*p0Vec)+log(1.0-pClass1)
    if(p1>p0):
        return 1
    else:
        return 0
    
def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)

def bagOfWords2VecMN(vocabList,inputSet):
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]+=1
    return returnVec

# mySent='this book os the best book on pyhton ot M.L i have ever read'
# regex=re.compile('\\W*')
# emailText=open('F:\\ML\\MLdata\\Ch04\\email\\ham\\6.txt').read()
# listOfTokens=regex.split(emailText)
# print listOfTokens

def textParse(bigString):
    import re
    listOfTokens=re.compile('\\W*').split(bigString)
    return [tok.lower() for tok in listOfTokens if len(tok)>2]

def spamTest():
    docList=[];classList=[];fullTest=[]
    for i in range(1,26):
        wordList=textParse(open('F:\\ML\\MLdata\\Ch04\\email\\spam\\%d.txt'%i).read())
        docList.append(wordList)
        fullTest.extend(wordList)
        classList.append(1)
        wordList=textParse(open('F:\\ML\\MLdata\\Ch04\\email\\ham\\%d.txt'%i).read())
        docList.append(wordList)
        fullTest.extend(wordList)
        classList.append(0)
    vocabList=createVocabList(docList)
    trainingSet=range(50);testSet=[]
    for i in range(10):
        randIndex=int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat=[];trainClasses=[]
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0v,p1v,pSpam=trainNB0(array(trainMat), array(trainClasses))
    errorCount=0
    for docIndex in testSet:
        wordVector=setOfWords2Vec(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0v, p1v, pSpam)!=classList[docIndex]:
            errorCount+=1
    print 'the error rate is:',float(errorCount)/len(testSet)

spamTest()
































