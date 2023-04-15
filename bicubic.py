"""
Created on Thu Oct 14 21:55:30 2021
@author: Umeshika
"""
#import the libraries
import cv2
import numpy as np
from datetime import datetime 
#The variable is create to get the starting time when the code is run
starttime=datetime.now()
#load the image
img=cv2.imread("a.jpg") 
#define function for polynomial technique with two different formula
def Bicubic(x):
    x = np.abs(x)
    #consider the third oder degree polynoial function for 0=<x<1 range
    if 0 <= x < 1:
        return 1 - 2 * x * x + x * x * x
    '''consider the  another third oder degree 
        polynoial function for 0=<x<1 range'''
    if 1 <= x < 2:
        return 4 - 8 * x + 5 * x * x - x * x * x
    else:
        return 0
#The bicubic interpolation function is defined to zoom        
def bicubic_interpolation(img,new_height,new_width):
    #height and width original image
    height,width,channels =img.shape
    #RGB image zero matrix is taken
    zoom_img=np.zeros((new_height,new_width,channels),np.uint8)
    # scale factor
    sh=new_height/height
    sw=new_width/width
    for i in range(new_height):
        for j in range(new_width):
            #x,y coordinates with float values
            x = i/sh
            y = j/sw
            #x,y coordinates with integer values
            p=(i+0.0)/sh-x
            q=(j+0.0)/sw-y
            x=int(x)-2
            y=int(y)-2
            '''the zoom image coordinates(i, j) and pixelate it with 
            the coordinate of original image'''
            #first coeffient
            A = np.array([
                [Bicubic(1 + p), Bicubic(p), Bicubic(1 - p), Bicubic(2 - p)]])
            
            if x>=new_height-3:
                new_height-1
            if y>=new_width-3:
                new_width-1
            if x>=1 and x<=(new_height-3) and y>=1 and y<=(new_width-3):
                
            #second coeffient    
                B = np.array([
                    [img[x-1, y-1], img[x-1, y],img[x-1, y+1],img[x-1, y+1]],
                    [img[x, y-1],   img[x, y],img[x, y+1], img[x, y+2]],
                    [img[x+1, y-1], img[x+1, y],img[x+1, y+1], img[x+1, y+2]],
                    [img[x+2, y-1], img[x+2, y],img[x+2, y+1], img[x+2, y+1]],])
                
                #third coeffient
                C = np.array([
                    [Bicubic(1 + q)],   
                    [Bicubic(q)],
                    [Bicubic(1 - q)],
                    [Bicubic(2 - q)]])
                #rgb layers are taken
                B_n = np.dot(np.dot(A, B[:, :, 0]), C)[0, 0]
                G_n = np.dot(np.dot(A, B[:, :, 1]), C)[0, 0]
                R_n = np.dot(np.dot(A, B[:, :, 2]), C)[0, 0]
 
                #the values ajusts to be in [0,255]
                def adj(bin_size):
                    if bin_size > 255:
                        bin_size = 255
                    elif bin_size < 0:
                        bin_size = 0
                    return bin_size
                #rgb channel image is taken
                B = adj(B_n)
                G = adj(G_n)
                R = adj(R_n)
                zoom_img[i, j] = np.array([B, G, R], dtype=np.uint8)
 
 
    return zoom_img
#image double size of height and width 
h2 = img.shape[0]*2
w2 = img.shape[1]*2
#the zoomed image is taken   
zoom=bicubic_interpolation(img,h2,w2)
cv2.imshow("The Zoom image using bicubic interpolation method",zoom)
cv2.imshow("Original image",img)
cv2.waitKey(0)
"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-starttime)    