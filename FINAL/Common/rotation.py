import numpy as np, math, cv2
from Common.interpolation import bilinear_value
from Common.functions import contain

def rotate_pt(img, degree, pt):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree/180) * np.pi
    sin, cos = math.sin(radian), math.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            jj, ii = np.subtract((j, i), pt)
            y = -jj * sin + ii * cos
            x = jj * cos + ii * sin
            x, y = np.add((x,y), pt)
            if contain((y, x), img.shape):
                dst[i, j] = bilinear_value(img, (x,y))
    return dst