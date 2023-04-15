# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 18:53:02 2021

@author: acer
"""
import cv2 
import numpy as np
#The implementation code is as follows:
def nearest_neighbor_resize(img, new_w, new_h):
    # height and width of the input img
    h, w = img.shape[0], img.shape[1]
    # new image with rgb channel
    ret_img = np.zeros(shape=(new_h, new_w, 3), dtype='uint8')
    # scale factor
    s_h, s_c = (h * 1.0) / new_h, (w * 1.0) / new_w

    # insert pixel to the new img
    for i in range(new_h):
        for j in range(new_w):
            p_x = int(j * s_c)
            p_y = int(i * s_h)

            ret_img[i, j] = img[p_y, p_x]

    return ret_img


#The test code is as follows:

#def test():
img_path = 'flower.jpg'
img = cv2.imread(img_path)
ret_img = nearest_neighbor_resize(img, 220, 220)

cv2.imshow("source image", img)
cv2.imshow("after bilinear image", ret_img)
cv2.waitKey()
cv2.destroyAllWindows()