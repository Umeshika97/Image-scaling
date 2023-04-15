import numpy as np
import cv2

img = cv2.imread('a.jpg')
img_shape = (img.shape[0], img.shape[1])
dst_shape = (2*img_shape[0], 2*img_shape[1])


def bilinear(org_img, org_shape, dst_shape):
    print(org_shape)
    dst_img = np.zeros((dst_shape[0], dst_shape[1], 3))
    dst_h, dst_w = dst_shape
    org_h, org_w = org_shape
    for i in range(dst_h):
        for j in range(dst_w):
            src_x = j * float(org_w / dst_w)
            src_y = i * float(org_h / dst_h)
            src_x_int = j * org_w // dst_w
            src_y_int = i * org_h // dst_h
            a = src_x - src_x_int
            b = src_y - src_y_int

            if src_x_int+1 == org_w or src_y_int+1 == org_h:
                dst_img[i, j, :] = org_img[src_y_int, src_x_int, :]
                continue
            # print(src_x_int, src_y_int)
            dst_img[i, j, :] = (1. - a) * (1. - b) * org_img[src_y_int+1, src_x_int+1, :] + \
                            (1. - a) * b * org_img[src_y_int, src_x_int+1, :] + \
                            a * (1. - b) * org_img[src_y_int+1, src_x_int, :] + \
                            a * b * org_img[src_y_int, src_x_int, :]
    return dst_img



dst_img = bilinear(img, img_shape, dst_shape)
#cv2.imshow("source image", img)
cv2.imshow("after bilinear image", dst_img)
cv2.waitKey()
cv2.destroyAllWindows()
#cv2.imwrite('./428_487626_bilinear.jpg', dst_img)
