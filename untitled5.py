"""
Created on Mon Oct 18 08:23:46 2021
@author: Umeshika
"""
import cv2
import numpy as np
from skimage import  color
import matplotlib.pyplot as plt
#load the image


img = cv2.imread('b.jpg').astype(np.float32) 
#convert data to gray color
imggray=color.rgb2gray(img)

def grayhistogram_cal(image):
    #Image width and height
    h=image.shape[0]
    w=image.shape[1]
    grayhistogram=np.zeros(shape=(256,1))
    for i in range(h):
        for j in range(w):
            p=int(image[j][i])
            grayhistogram[p,0]=grayhistogram[p,0]+1
    return grayhistogram

gray_histogram_values=grayhistogram_cal(imggray)
print(gray_histogram_values)
limit= int (len(gray_histogram_values))

#ff=cv2.calcHist([imggray], [0], None, [255], [0,255])
def OTSU(img_gray):
    h=img_gray.shape[0]
    w=img_gray.shape[1]
    
    suitable_th = 0
    th_begin = 0
    #limit = 256
    within=[]
    for threshold in range(limit):
        x,y=np.split([limit],[threshold])
        #bin_img = img_gray > threshold
        #bin_img_inv = img_gray <= threshold
        x1=np.sum(x)/(h*w)
        y1=np.sum(y)/(h*w)
        x2=np.sum([j*t for j,t in enumerate(x)])/np.sum(x)
        y2=np.sum([j*t for j,t in enumerate(y)])/np.sum(y)
        x3=np.sum([(j-x2)**2*t for j,t in enumerate(x)])/np.sum(x)
        x3=np.nan_to_num(x3)
        print(3)
        y3=np.sum([(j-y2)**2*t for j,t in enumerate(y)])/np.sum(y)
        within.append(x1*x3+y1*y3)
        suitable_th=np.argmin(within)    
 
    return suitable_th

binary =imggray >0.5
#%%
# take the value of optimal otsu global thresh 
global_thresh= OTSU(imggray)
# take binary image using global thresholding
binary_global = imggray > global_thresh
#plot the binary image
cv2.imshow("Otsu dst", binary_global)
#cv.imwrite("D:/testimage/result-cxk.jpg",Otsu_dst)
cv2.waitKey(0)

