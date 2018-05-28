from PIL import Image
import numpy as np

path="C:/Users/Administrator/Desktop/sRGB.jpg"

def read_image(img_path):
    img=Image.open(img_path)
    img=np.array(img)
    return img

img=read_image(path)
print(img)