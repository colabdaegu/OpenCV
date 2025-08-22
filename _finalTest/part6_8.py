import numpy as np, cv2




# 영상 읽기
image1 = cv2.imread("add1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류 발생")
title = ' dst'

# 영상 합성
alpha, beta = 0.6, 0.4                                       # 곱샘 비율
image3 = cv2.addWeighted(image1, alpha, image2, beta, 0)     # 두영상 비율에 따른 더하기

# 영상 3개가 들어갈 배열 생성하고 영상 넣기
w, h = image1.shape                                          # image1의 가로, 세로 길이
dst = np.zeros((w, h*3), np.uint8)                           # image1의 가로, 세로 * 3의 배열 생성
dst[0:h, 0:w] = image1[0:h, 0:w]                             # 배열의 맨 앞에 image1 넣기
dst[:, w*2:] = image2[0:h, 0:w]                              # 배열의 맨 뒤에 image2 넣기
dst[0:h, w:w*2] = image3[0:h, 0:w]                           # 배열의 가운데에 image3 넣기

cv2.imshow(title, dst)



cv2.waitKey(0)