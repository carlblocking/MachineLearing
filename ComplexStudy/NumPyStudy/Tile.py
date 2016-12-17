#encoding=utf-8
#学习tile函数
from numpy import tile
from matplotlib.pyplot import axis
from operator import itemgetter
import operator
# # a=([1.0,1.1],[1.0,1.0],[0,0],[0,0.1])
# # test=[1.0,1.3]
# # length=len(a)
# # diffMat=tile(test,(length,1))-a
# # print diffMat
# #tile函数主要用于重复某个函数
# b=[0,3,2]
# #将b重复两遍
# c=tile(b, 2)
# #同样重复[0,1,2]数组
# print tile(b, (1,2))
# print c
# #转换为二维数组
# print tile(b, (2,1))
# matTest=tile(b, (2,1))
# #矩阵的每一列相加
# print matTest.sum(axis=0)
# #矩阵的每一行相加
# print matTest.sum(axis=1)
# 
# #Python中排序常用到的sort 、sorted和argsort函数
# print matTest.sum(axis=0).argsort()
# ee=[1,2,3,6,5,456,12,34,564,1,321,2]
# ee1=[1,2,3,6,5,456,12,34,564,1,321,2]
# #sort会影响列表本身，而sorted不会
# ee.sort(cmp=None, key=None, reverse=False)
# print ee
# print sorted(ee1)

list1=[("lisa",90),("monica",88),("alana",98),("zara",66)]
#使用cmp函数排序
#根据第一个关键字排序
#根据第二个关键字排序
print sorted(list1,cmp=lambda x,y:cmp(x[0], y[0]))   
print sorted(list1,cmp=lambda x,y:cmp(x[1],y[1]))  
#使用key函数排序
print sorted(list1,key=lambda list1:list1[0])
print sorted(list1,key=lambda list1:list1[1])
#使用reverse排序
print sorted(list1,key=lambda list1:list1[1],reverse=True)
print sorted(list1,reverse=False)#默认用第一个元素排序
#使用operator.itemgetter排序
print sorted(list1,key=itemgetter(0))
print sorted(list1,key=itemgetter(0),reverse=True)
print sorted(list1,key=itemgetter(1))
print sorted(list1,key=itemgetter(1),reverse=True)
#打印元素
classCount={'carl':98,'monica':99,'tom':88}
print classCount.iteritems()
print "value:%s"%classCount.get('carl')
print "value:%s"%classCount.get('Sex','Never')
print classCount
print classCount['carl']
print classCount.items()
print classCount.iteritems()
#添加nana的元素
for k in 'python':
   classCount['nana']=classCount.get('nana',0)+1
#print classCount['nana']
sortedCountClass=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
print sortedCountClass
print sortedCountClass[0][0]
print sortedCountClass[0][1]









