import numpy as np, cv2, math
from Common.hough import accumulate, masking, select_lines

def houghLines(src, rho, theta, thresh):
    acc_mat = accumulate(src, rho, theta)
    acc_dst = masking(acc_mat, 7, 3, thresh)
    lines= select_lines(acc_dst, rho, theta, thresh)
    return lines

def draw_houghLines(src,lines, nline):
    if len(src.shape) < 3:
        dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
    else:
        dst = np.copy(src)
    min_length = min(len(lines), nline)
    for i in range(min_length):
        rho, radian = lines[i, 0, 0:2]
        a, b= math.cos(radian), math.sin(radian)
        pt = (a*rho, b*rho)
        delta = (-1000*b, 1000*a)
        pt1 = np.add(pt, delta).astype('int')
        pt2 = np.subtract(pt, delta).astype('int')
        cv2.line(dst, tuple(pt1), tuple(pt2), (0, 255, 0) ,1 , cv2.LINE_AA)
    return dst

image = cv2.imread('images/prob3.jpg', cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 2, 2)
canny = cv2.Canny(blur, 50, 150, 5)
rho, theta = 1, np.pi/180
lines2 = houghLines(canny, rho, theta, 80)
dst2 = draw_houghLines(image, lines2, 20)

cv2.imshow("detected lines", dst2)
cv2.waitKey(0)