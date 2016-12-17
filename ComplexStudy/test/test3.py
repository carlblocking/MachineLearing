#encoding=utf-8
#用于测试Matplotlib
import matplotlib.pyplot as plt
from matplotlib import *
import numpy as np
from numpy.matlib import rand
from numpy import ones, array
from matplotlib.mlab import find
from scipy.interpolate.interpolate import spltopp
# fig=plt.figure()
# for idx, color in enumerate("rgby"):
#     plt.subplot(321+idx,axisbg=color)
# plt.show()

# 
# plt.figure(1)#创建图表1
# plt.figure(2)#创建图表2
# ax1=plt.subplot(211)#在图表2中创建子图1
# ax2=plt.subplot(212)#在图表2中创建子图2
# x=np.linspace(0, 3, 100)
# for i in xrange(5):
#     plt.figure(1)
#     plt.plot(x,np.exp(i*x/3))
#     plt.sca(ax1)
#     plt.plot(x,np.sin(i*x))
#     plt.sca(ax2)
#     plt.plot(x,np.cos(i*x))
# plt.show()

# fig=plt.figure()
# n=1000
# x=np.random.randn(1,n)
# y=np.random.randn(1,n)
# T=np.arctan2(x,y)
# plt.scatter(x, y, c=T,s=25,alpha=0.4,marker='o')
# plt.show()

# x=np.arange(-np.pi,np.pi,0.01)
# y=np.sin(x)
# plt.plot(x,y,'b')
# plt.show()

# x=np.arange(-5,5,0.01)
# y=x**2+x*8+5
# #设置横坐标和纵坐标的范围
# plt.axis([-10,10,-100,100])
# plt.plot(x,y)
# plt.show()

# #在matplotlib中，除了axis设置坐标范围，还有以下方式来设置
# #xlim((xmin,xmax))或者xlim(xmin,xmax)来设置横坐标轴的最大最小值
# #ylim((ymin,ymax))或者ylim(ymin,ymax)来设置纵坐标轴的最大最小值
# x=np.arange(-5,5,0.01)
# y=x**3
# plt.xlim(-6,6)
# plt.ylim(-100,100)
# plt.plot(x,y)
# plt.show()

# x=np.arange(-5,5,0.01)
# y=x**3
# plt.xlim(-6,6)
# plt.ylim(-100,100)
# plt.plot(x,y,'r')
# #增加网格
# plt.grid(True)
# plt.show()

n=np.random.randn(1000,2)
p=np.random.rand(1000,3)
fg=plt.figure()
T=np.arctan2(n[:,0],n[:,1])
plt.scatter(n[:,0],p[:,1],c=T)
plt.show()





































