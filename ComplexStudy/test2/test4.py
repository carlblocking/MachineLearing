from numpy import *
testArray=mat(zeros((6,2)))
validList=nonzero(testArray[:,1].A)[0]
print validList
print len(validList)
print testArray