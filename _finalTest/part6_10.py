import numpy as np
import cv2

image1 = np.zeros((50, 512), np.float32)
image2 = np.zeros((50, 512), np.float32)
rows, cols = image1.shape[:2]

for i in range(rows):
    for j in range(cols):
        image1[i, j] = j / 512  # 0부터 1까지 선형적으로 증가하는 값
        image2[i, j] = (j // 20) * 10 / 255.0  # 계단 현상을 만들기 위한 값

# 이미지를 0과 1 사이로 정규화
cv2.normalize(image1, image1, 0.0, 1.0, cv2.NORM_MINMAX)
cv2.normalize(image2, image2, 0.0, 1.0, cv2.NORM_MINMAX)

# 윈도우에 이미지 표시
cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.waitKey(0)