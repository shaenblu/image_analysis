from __future__ import print_function
from sys import argv
import os.path
import cv2
import numpy as np

def otsu(src_path, dst_path):

    img = cv2.imread(src_path)
    assert img is not None
    height1, width1, channels1 = img.shape

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    sumPix = np.sum(hist)
    sumMean = 0

    for i in range(len(hist)):
        sumMean += i * hist[i]

    var = -1.0
    ther = 0
    curMean = 0
    sumBack = 0
    betVariance = 0
    meanFor = 0
    meanBack = 0

    for i in range(len(hist)):
        curMean += i * hist[i]
        sumBack += hist[i]
        sumFor = sumPix - sumBack

        if (sumFor != 0) and (sumBack != 0):
            meanBack = float(curMean / sumBack)
            meanFor = float((sumMean - curMean) / sumFor)
            betVariance = float(sumBack * sumFor * (meanBack - meanFor) ** 2)

            if (betVariance > var):
                var = betVariance
                ther = i

    for i in range(height):
        for j in range(width):
            if (gray.item(i, j) > ther):
                img.itemset((i, j, 0), 255)
                img.itemset((i, j, 1), 255)
                img.itemset((i, j, 2), 255)
            if (gray.item(i, j) <= ther):
                img.itemset((i, j, 0), 0)
                img.itemset((i, j, 1), 0)
                img.itemset((i, j, 2), 0)

    cv2.imwrite(dst_path, img)

if __name__ == '__main__':
    assert len(argv) == 3
    assert os.path.exists(argv[1])
    otsu(*argv[1:])