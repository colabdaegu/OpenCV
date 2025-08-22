import numpy as np, cv2

def bilinear_value(img, pt):
    x, y = np.int32(pt)
    if x >= img.sape[1]-1: x = x - 1
    if y >= img.shape[0]-1: y = y - 1

    P1, P2, P3, P4 = np.float32(img[y:y+2, x:x+2].flatten())

    alpha, beta = pt[1] - y, pt[0] - x
    M1 = P1 + alpha * (P3-P1)
    M2 = P2 + alpha * (P4 - P2)
    P = M1 + beta * (M2 - M1)
    return np.clip(P, 0, 255)