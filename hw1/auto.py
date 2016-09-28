from __future__ import print_function
from sys import argv
import os.path
import cv2
import cv
import numpy as np
import math


def autocontrast(src_img_path, dst_img_path, white_perc, black_perc):
    img = cv2.imread(src_img_path)
    assert img is not None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    height, width, channels = gray.shape

    maxx = gray.item(0,0,0)
    minn = gray.item(0,0,0)
    for i in range(height):
        for j in range(width):
            if (gray.item(i,j,0) > maxx):
                maxx = gray.item(i,j,0)
            if (gray.item(i, j, 0) < minn):
                minn = gray.item(i, j, 0)

    k1 = maxx - math.ceil((maxx - minn)*float(white_perc))
    k2 = minn + math.ceil((maxx - minn)*float(black_perc))

    if (k1 < 255):
        for i in range(height):
            for j in range(width):
                if (gray.item(i, j, 0) >= k1):
                    gray.itemset((i,j,0), 255)

    if (k2 > 0):
        for i in range(height):
            for j in range(width):
                if (gray.item(i,j,0) <= k2):
                    gray.itemset((i,j,0), 0)


    for i in range(height):
        for j in range(width):
            if ((gray.item(i,j,0)>k2) and (gray.item(i,j,0)<k1)):
                gray.itemset((i,j,0), (gray.item(i,j,0) - minn)* 255 / (maxx - minn))


    imag = cv2.cvtColor(gray, cv2.COLOR_YUV2BGR)
    cv2.imwrite(dst_img_path,imag)


if __name__ == '__main__':
    assert len(argv) == 5
    assert os.path.exists(argv[1])
    assert 0 <= argv[3] > 1
    assert 0 <= argv[4] > 1

    autocontrast(*argv[1:])
