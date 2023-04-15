"""
Created on Thu Oct 14 18:53:02 2021
@author: Umeshika
"""
#import the libraries
import cv2
import numpy as np
from datetime import datetime 
#The variable is create to get the starting time when the code is run
starttime=datetime.now()
#load the image
img = cv2.imread("a.jpg")
#The function is defined to zoom
def nearestneighbor(img,new_height,new_width):
    h,w,_=img.shape#height and width original image
    #RGB image zero matrix is taken
    rgbimg=np.zeros((new_height,new_width,3),dtype=np.uint8)
    for i in range(new_height-1):
        for j in range(new_height-1):
            # scale factor
            sh = (h * 1.0) / new_height
            sw = (w * 1.0) / new_width
            # insert pixel to the new img
            '''the zoom image coordinates(i, j) and pixelate it with 
            the coordinate of original image'''
            zoom_x=round(i*sh)
            zoom_y=round(j*sw)
            #rgb channel image is taken
            rgbimg[i,j]=img[zoom_x,zoom_y]
    return rgbimg

#image double size of height and width 
h2 = img.shape[0]*2
w2 = img.shape[1]*2
#the zoomed image is taken  
zoom = nearestneighbor(img,h2,w2)
cv2.imshow("The Zoom image using nethodnearest neighbor method", zoom)
cv2.imshow("Original image", img)
cv2.imwrite('Original_image.png', img)
cv2.imwrite('Zoomedimage.png', zoom)
cv2.waitKey(0)

"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-starttime)    

