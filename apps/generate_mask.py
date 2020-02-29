# encoding:utf-8

import cv2
import numpy as np

img = cv2.imread("../sample_images/me.png", cv2.IMREAD_UNCHANGED)
print(img.shape[:3])
height, width = img.shape[:2]

mask = np.zeros((height, width, 3), np.uint8)
for j in range(0,height):
    for i in range(0,width):
        if img[j,i,3] > 0:
            mask[j,i] = [255, 255, 255]

cv2.imwrite("../sample_images/me_mask.png", mask)