from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

path="C:/Users/Administrator/Desktop/hunan/1.jpg"

def read_image(img_path):
    img_data=Image.open(img_path)
    img_data=np.array(img_data)
    return img_data

adobe_to_xyz = (
    0.57667, 0.18556, 0.18823, 0,
    0.29734, 0.62736, 0.07529, 0,
    0.02703, 0.07069, 0.99134, 0,
) # http://www.adobe.com/digitalimag/pdfs/AdobeRGB1998.pdf                                

xyz_to_srgb = (
    3.2406, -1.5372, -0.4986, 0,
    -0.9689, 1.8758, 0.0415, 0,
    0.0557, -0.2040, 1.0570, 0,
) # http://en.wikipedia.org/wiki/SRGB                                                     

def adobe_to_srgb(image):
    return image.convert('RGB', adobe_to_xyz).convert('RGB', xyz_to_srgb)

img_data=Image.open(path)
img_data=adobe_to_srgb(img_data)
img_data=np.array(img_data)
print(img_data)

