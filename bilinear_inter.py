"""
Created on Sat Oct 16 22:22:17 2021
@author: umeshika
"""
#import the libraries
import cv2
import numpy as np
from datetime import datetime 
#The variable is create to get the starting time when the code is run
starttime=datetime.now()
#load the image
img=cv2.imread("a.jpg")

#The bilinear interpolation function is defined to zoom
def bilinear_interpolation(img,new_height,new_width):
    #height and width original image
    height,width,channels =img.shape
    #RGB image zero matrix is taken
    zoom_img=np.zeros((new_height,new_width,channels),np.uint8)
    value=[0,0,0]
    # scale factor
    sh=new_height/height
    sw=new_width/width
    for i in range(new_height):
        for j in range(new_width):
            #x,y coordinates with float values
            x = i/sh
            y = j/sw
            p=(i+0.0)/sh-x
            q=(j+0.0)/sw-y
            #x,y coordinates with integer values
            x=int(x)-1
            y=int(y)-1
            '''the zoom image coordinates(i, j) and pixelate it with 
            the coordinate of original image'''
            for k in range(3):
                if x+1<new_height and y+1<new_width:
                   value[k]=  int(img[x,y][k]*(1-p)*(1-q)\
                                +img[x,y+1][k]*q*(1-p)\
                                +img[x+1,y][k]*(1-q)*p\
                                +img[x+1,y+1][k]*p*q)
            #rgb channel image is taken
            zoom_img[i, j] = (value[0], value[1], value[2])
    return zoom_img
#image double size of height and width 
h2 = img.shape[0]*2
w2 = img.shape[1]*2
#the zoomed image is taken  
zoom=bilinear_interpolation(img,h2,w2)
cv2.imshow("Bilinear Interpolation",zoom)
cv2.imshow("image",img)
cv2.waitKey(0)
"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-starttime)    