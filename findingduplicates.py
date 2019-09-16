import hashlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import os
import cv2

'''for i in os.listdir('images/'):
    image = cv2.imread('images/' + i)
    image = cv2.resize(image, (400, 400))
    cv2.imwrite('images2/' + i, image)
'''

folder1 = 'images2/'
folder2 = 'images3/'

for i in os.listdir(folder1):
    count = 0
    org = cv2.imread(folder1 + i)
    for j in os.listdir(folder2):
        dup = cv2.imread(folder2 + j)

        difference = cv2.subtract(org, dup)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            count += 1

            if count > 1:
                os.remove(folder2 + j)
