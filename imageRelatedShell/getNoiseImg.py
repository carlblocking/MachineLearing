import cv2

def get_noise(input_img1, input_img2, noise_save_path):
    img1=cv2.imread(input_img1)
    img2=cv2.imread(input_img2)
    noise=img1-img2
    cv2.imwrite(noise_save_path, noise)

def minus_noise(input_img1, input_img2, noise_save_path):
    img1=cv2.imread(input_img1)
    img2=cv2.imread(input_img2)
    noise=img1-img2
    cv2.imwrite(noise_save_path, noise)
    
for i in range(1,2822):
    input_img1_path="C:/Users/Administrator/Desktop/train_B/{}.jpg".format(str(i))
    input_img2_path="C:/Users/Administrator/Desktop/noise/{}.jpg".format(str(i))
    noise_path="C:/Users/Administrator/Desktop/test2/{}.jpg".format(str(i))
    get_noise(input_img1_path, input_img2_path, noise_path)
    print(i, "done")