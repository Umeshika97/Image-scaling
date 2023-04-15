"""
Created on Mon Oct 18 08:23:46 2021
@author: Umeshika
"""
import cv2
import numpy as np
from skimage import  color
import matplotlib.pyplot as plt
#load the image
img=cv2.imread("a.jpg") 
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
limit= len(gray_histogram_values)
def OTSU(img_gray):
    max_g = 0
    suitable_th = 0
    th_begin = 0
    th_end = 256
    for threshold in range(th_begin, th_end):
        bin_img = img_gray > threshold
        bin_img_inv = img_gray <= threshold
        fore_pix = np.sum(bin_img)
        back_pix = np.sum(bin_img_inv)
        if 0 == fore_pix:
            break
        if 0 == back_pix:
            continue
 
        w0 = float(fore_pix) / img_gray.size
        u0 = float(np.sum(img_gray * bin_img)) / fore_pix
        w1 = float(back_pix) / img_gray.size
        u1 = float(np.sum(img_gray * bin_img_inv)) / back_pix
        # intra-class variance
        g = w0 * w1 * (u0 - u1) * (u0 - u1)
        if g > max_g:
            max_g = g
            suitable_th = threshold
 
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
cv2.destroyAllWindows()




#plt.imshow(binary_local,'Local thresholding')
#cv2.imshow("Bilinear Interpolation",binary_local)