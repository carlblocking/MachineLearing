from PIL import Image
from skimage.util.noise import random_noise
import numpy as np

def add_noise(img_path, i):
    img=Image.open(img_path)
    img=np.array(img)
    var=np.random.uniform(0,0.01)
    mean=np.random.uniform(0,0.1)
    noise_img=random_noise(img,  mean=mean, var=var)
    print(var, "\t", mean)
    Image.fromarray(np.uint8(noise_img*255)).save("C:/Users/Administrator/Desktop/train_B/{}.jpg".format(str(i)))
    print(i, "done")

    
def deal_file_images():   
    for i in range(1,2822):
        path="C:/Users/Administrator/Desktop/train_A/{}.jpg".format(str(i)) 
        add_noise(path, i)
                               

deal_file_images()

