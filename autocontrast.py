from __future__ import print_function


import cv2
import numpy as np
import matplotlib
matplotlib.rcParams['backend'] = "Qt4Agg"
import matplotlib.pyplot as plt
from PIL import Image



path = '/Users/gulnur/PycharmProjects/MyProj/re.jpg'
img = cv2.imread(path)

assert img is not None

'''
for i in range(len(values)):
    c = (values[i][0]+values[i][1]+values[i][2])/3.0
    if (c > ((maxx[0]+maxx[1]+maxx[2])/3.0)):
        maxx = values[i]

print(maxx)

minn = values[0]
for i in range(len(values)):
    c = (values[i][0]+values[i][1]+values[i][2])/3.0
    if (c < ((minn[0]+minn[1]+minn[2])/3.0)):
        minn = values[i]

print(minn)
'''



white_dol = 0.2
black_dol = 0.2

'''
color = ('b','g','r')
for i, col in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()



cv2.imwrite("/Users/gulnur/PycharmProjects/MyProj/histogram.png",hist)

'''
height, width, channels = img.shape
count_max = 0
count_min = 0

minn = (img.item(0,0,0),img.item(0,0,1), img.item(0,0,2))
maxx = (img.item(0,0,0),img.item(0,0,1), img.item(0,0,2))

for i in range(height):
    for j in range(width):
        c = (img.item(i,j,0)+img.item(i,j,1)+img.item(i,j,2))/3.0
        mi = (minn[0]+minn[1]+minn[2])/3.0
        ma = (maxx[0]+maxx[1]+maxx[2])/3.0
        if (c > ma):
            maxx = (img.item(i,j,0), img.item(i,j,1), img.item(i,j,2))
        if (c < mi):
            minn =  (img.item(i,j,0), img.item(i,j,1), img.item(i,j,2))

print (maxx)
print(minn)


for i in range(height):
    for j in range(width):
        if ((maxx[0] == img.item(i,j,0)) and (maxx[1] == img.item(i,j,1)) and (maxx[2] == img.item(i,j,2))):
            count_max = count_max+1
        if ((minn[0] == img.item(i,j,0)) and (minn[1] == img.item(i,j,1)) and (minn[2] == img.item(i,j,2))):
            count_min = count_min+1

print(count_max)
print(count_min)


k1 = count_max*white_dol
print(k1)
k2 = count_min*black_dol
print(k2)
kk1 = 0
if (k1>0):
    for i in range(height):
        for j in range(width):
            if ((maxx[0] == img.item(i,j,0)) and (maxx[1] == img.item(i,j,1)) and (maxx[2] == img.item(i,j,2))):
                img.itemset((i, j, 0), 255)
                img.itemset((i, j, 1), 255)
                img.itemset((i, j, 2), 255)
                kk1 += 1
            if (kk1 == k1):
                break
        if (kk1 == k1):
            break

print(kk1)

cv2.imwrite("/Users/gulnur/PycharmProjects/MyProj/white.png",img)

kk2 = 0
if (k2>0):
    for i in range(height):
        for j in range(width):
            if ((minn[0] == img.item(i,j,0)) and (minn[1] == img.item(i,j,1)) and (minn[2] == img.item(i,j,2))):
                img.itemset((i, j, 0), 0)
                img.itemset((i, j, 1), 0)
                img.itemset((i, j, 2), 0)
                kk2 += 1
            if (kk2 == k2):
                break
        if (kk2 == k2):
            break

cv2.imwrite("/Users/gulnur/PycharmProjects/MyProj/black.png",img)

for i in range(height):
    for j in range(width):
        if (((img.item(i,j,0)!=255) and (img.item(i,j,1)!=255) and (img.item(i,j,2)!=0)) or
            ((img.item(i,j,0)!=0) and (img.item(i,j,1)!=0) and (img.item(i,j,2)!=0))):
            if (minn != maxx):
                img.itemset((i, j, 0), ((img.item(i, j, 0) - minn[0]) * 255/ (maxx[0]-minn[0])))
                img.itemset((i, j, 1), ((img.item(i, j, 1) - minn[1]) * 255/ (maxx[1]-minn[1])))
                img.itemset((i, j, 2), ((img.item(i, j, 2) - minn[2]) * 255/ (maxx[2]-minn[2])))



cv2.imwrite("/Users/gulnur/PycharmProjects/MyProj/res.png",img)
