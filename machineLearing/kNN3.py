#encoding=utf-8
import matplotlib.pyplot as plt

from numpy import array
from machineLearing.kNN2 import filePath, file2matrix
#横坐标为每年获取的飞行常客里程数
#纵坐标为玩视频游戏所耗时间百分比
fig=plt.figure()
ax=fig.add_subplot(111)
returnMat,labelMat=file2matrix(filePath)
ax.scatter(returnMat[:,0],returnMat[:,1],15.0*array(labelMat),15.0*array(labelMat))
plt.show()