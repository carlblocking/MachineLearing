#file related
import os as os
filePath='C:\\Users\\xxw\\Desktop\\test.txt'
fr=open(filePath)
arrayLines=fr.readlines()
for str in arrayLines:
    print str.strip()
