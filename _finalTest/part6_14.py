import numpy as np, cv2

image = cv2.imread("add2.jpg", cv2.IMREAD_COLOR)
if image is None : raise Exception("영상파일 읽기 오류")
if image.ndim != 3 : raise Exception("영상파일 차원 오류")

#HSV 칼라 공간 변화. 이번에는 빠르게 내장함수 사용.
# 내장함수 안쓰는건 이전 포스팅에
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# two dim histogram 구현, uint8로 8비트 단일 채널로 imshow에 출력할거야.
two_dim_histo = np.zeros((image.shape[:2]), np.uint8)

# calcHist
for row in range(hsv_img.shape[0]):
    for col in range(hsv_img.shape[1]):
        two_dim_histo[hsv_img[row, col, 0], hsv_img[row, col, 1]] += 1

max_val = 23 # np.max(two_dim_histo)
two_dim_histo = (two_dim_histo/max_val) * 255
# round 불가능 -> np.array로 재정렬.
two_dim_histo = np.array(two_dim_histo, np.uint8)

color_histo = np.zeros(image.shape, np.uint8) #3차원의 칼라를 넣을 image와 같은 3차원의 shape 생성.

for row in range(color_histo.shape[0]):
    for col in range(color_histo.shape[1]):
        color_histo[row, col] = [row, col, two_dim_histo[row, col]]

for row in range(color_histo.shape[0]):
    for col in range(color_histo.shape[1]):

        if two_dim_histo[row, col]>50:
            color_histo1[row, col] = [row, col, two_dim_histo[row, col]]

        color_histo2[row, col] = [row, col, two_dim_histo[row, col]]

cv2.imshow("colorHist1", color_histo1)
cv2.imshow("colorHist2", color_histo2)

color_histo = cv2.cvtColor(color_histo, cv2.COLOR_HSV2BGR)
cv2.imshow("color hist BGR", color_histo)

cv2.imshow("hsv_plot", two_dim_histo)
cv2.imshow("hsv_img", hsv_img)
cv2.waitKey(0)