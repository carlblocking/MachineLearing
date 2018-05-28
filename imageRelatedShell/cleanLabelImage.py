import cv2
from tqdm import tqdm
import numpy as np
import os, shutil
from PIL import Image

label_dir='C:/Users/Administrator/Desktop/label/'
new_label_dir='C:/Users/Administrator/Desktop/label2/'
label_files=os.listdir(label_dir)

