from __future__ import print_function

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sys import argv
import os.path


def gamma_correction(src_path, dst_path, a, b):
    img = cv2.imread(src_path)

    assert img is not None

    height, width, channels = img.shape
    for i in range(height):
        for j in range(width):
            img.itemset((i, j, 0), (float(a) * (img.item(i, j, 0) / 255.0) ** float(b)) * 255.0)
            img.itemset((i, j, 1), (float(a) * (img.item(i, j, 1) / 255.0) ** float(b)) * 255.0)
            img.itemset((i, j, 2), (float(a) * (img.item(i, j, 2) / 255.0) ** float(b)) * 255.0)

    cv2.imwrite(dst_path, img)


if __name__ == '__main__':
    assert len(argv) == 5
    assert os.path.exists(argv[1])

    gamma_correction(*argv[1:])

