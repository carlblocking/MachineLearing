import cv2
from tqdm import tqdm
import numpy as np
import os, shutil
from PIL import Image

label_dir='C:/Users/Administrator/Desktop/label/'
new_label_dir='C:/Users/Administrator/Desktop/label2/'
label_files=os.listdir(label_dir)

# palette = {(0,   0,   0) : 0 ,
#            (12,0,255):1,
#            (255,90,0):2
# #            (0,240,255):2,
# #            (0,0,255):3,
# #            (255,97,97):4,
# #            (0,135,137):5,
# #            (255,216,0):6,
# #            (150,0,255):7,
# #            (181,0,106):8,
# #            (255,0,240):9,
# #            (255,132,190):10,
# #            (132,190,255):11,
# #            (132,255,175):12
#            }

# palette = {(0,   0,   0) :0 ,
#            (0,255,30):1,
#            (0,240,255):2,
#            (0,120,255):3,
#            (0,0,255):4,
#             (255,97,97):5
# #            (199,144,84):6,
# #             (255,97,97):7,
# #             (132,255,175):8
# #             (255,97,97):4
# #            (0,135,137):5,
# #            (255,216,0):6,
# #            (150,0,255):7,
# #            (181,0,106):8,
# #            (255,0,240):9,
# #            (255,132,190):10,
# #            (132,190,255):11,
# #            (132,255,175):12
#            }

palette = {(0,   0,   0) :0 ,
           (255,255,255):1
           }

def convert_from_color_segmentation(arr_3d):
    arr_2d = np.zeros((arr_3d.shape[0], arr_3d.shape[1]), dtype=np.uint8)
    for c, i in palette.items():
        m = np.all(arr_3d == np.array(c).reshape(1, 1, 3), axis=2)
        arr_2d[m] = i
    return arr_2d

def change(arr_3d):
    arr_2d = np.zeros((arr_3d.shape[0], arr_3d.shape[1]), dtype=np.uint8)
    for i in range(0,np.array(arr_3d).shape[0]):
        for j in range(0,np.array(arr_3d).shape[1]):
            value=np.min(np.array(arr_3d)[i,j])
            arr_2d[i,j]=value
    return arr_2d   

for l_f in tqdm(label_files):
    arr=np.array(cv2.imread(label_dir+l_f))
    arr_2d = convert_from_color_segmentation(arr)
#     cv2.imwrite(new_label_dir + l_f, arr_2d)
    Image.fromarray(arr_2d).save(new_label_dir + l_f)
