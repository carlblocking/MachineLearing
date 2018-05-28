import cv2
import numpy as np
import gc

img_path="C:/Users/Administrator/Desktop/test/1111.jpg"

def image_reflection(img_path):
    source=cv2.imread(img_path)
#     [h,w]=source.shape[:2]
    source=np.array(source)
    #y_reflection
    source1=source[:,::-1]
    source2=np.hstack((source, source1))
    source3=np.hstack((source1,source2))
    del source1,source2
    #x_reflection
    source4=source3[::-1]
    source5=np.vstack((source4,source3))
    source6=np.vstack((source5,source4))
    del source3,source4, source5
    cv2.imwrite("C:/Users/Administrator/Desktop/test/111.png",source6)
    gc.collect()


source=image_reflection(img_path)
