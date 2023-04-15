"""
Created on Thu Oct 14 21:55:30 2021
@author: Umeshika
"""
#import the libraries
import numpy as np
import cv2
#load the image
img = cv2.imread('a.jpg')
#height and width original image
img_shape = (img.shape[0], img.shape[1])
zoom_size = (2*img_shape[0], 2*img_shape[1])

#The bilinear interpolation function is defined to zoom
def bilinear_interpolation(img1, img1_shape, zoom_size):
    print(img1_shape)
    #RGB image zero matrix is taken
    zoom_img = np.zeros((zoom_size[0], zoom_size[1], 3))
    new_h, new_w = zoom_size#height and width zoom image
    h,w = img1_shape#height and width original image
    for i in range(new_h):
        for j in range(new_w):
            # scale factor
            sw= w / new_w
            sh= h / new_h
            #x,y coordinates with float values
            float_x = j * float(sw)
            float_y = i * float(sh)
            #x,y coordinates with integer values
            zoom_x = j * w // new_w
            zoom_y = i * h // new_h
            #difference of x,y coordinates with integer and float values
            a = float_x - zoom_x 
            b = float_y - zoom_y

            '''coordinates of the zoom image (i, j) and fill it with 
            the coordinates in the original image'''
            if zoom_x +1 == w or zoom_y+1 == h:
                zoom_img[i, j, :] = img1[zoom_y, zoom_x , :]
                continue
            # print(zoom_x , zoom_y)
           
            #rgb channel image is taken
            zoom_img[i, j, :] = (1. - a) * (1. - b) * img1[zoom_y+1, zoom_x +1, :] + \
                            (1. - a) * b * img1[zoom_y, zoom_x +1, :] + \
                            a * (1. - b) * img1[zoom_y+1, zoom_x , :] + \
                            a * b * img1[zoom_y, zoom_x , :]
    return zoom_img


#the zoomed image is taken  
zoom_img = bilinear_interpolation(img, img_shape, zoom_size)
cv2.imshow("Original image", img)
cv2.imshow("The Zoom image using bilinear interpolation method", zoom_img)
cv2.waitKey()
cv2.destroyAllWindows()
#cv2.imwrite('The bilinear image.jpg', dst_img)