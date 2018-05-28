#coding=utf8
import cv2
import os

def convertVideo2Image(input_video, save_path):
    c=0
    vc=cv2.VideoCapture(input_video)
    val=vc.isOpened()
    while val:
        c=c+1
        val, frame=vc.read()
        if val :
            if c<2000:
    #             cv2.imwrite(save_path+'/'+str(c)+'.jpg', frame)
#                 cv2.imencode('.jpg', frame, [int(cv2.cv2.IMWRITE_JPEG_CHROMA_QUALITY),100])[1].tofile(save_path+'/'+str(c)+'.jpg') 
                cv2.imencode('.tiff', frame)[1].tofile(save_path+'/'+str(c)+'.tiff') 
                print(save_path+'/'+str(c)+'.jpg'+"done")
                cv2.waitKey(1)
        else:
            break
    vc.release()
    return

def deal(path):
    g=os.walk(path)
    for dirs, paths, files in g:
        for file in files:
            if file.endswith(".mp4"):
                path1=os.path.join(path, file)
#                 print(path1)
                save_path="E:/路面监控视频/新建文件夹/"+os.path.splitext(file)[0]
#                 if not os.path.exists(save_path):
#                     os.makedirs(save_path)
                convertVideo2Image(path1,save_path)
#                 print(save_path)
                print("done")

deal("E:/路面监控视频/新建文件夹/")