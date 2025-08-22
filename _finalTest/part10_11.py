import numpy as np, cv2, math
from Common.hough import accumulate, masking, select_lines

def houghLines(src, rho, theta, thresh):
    acc_mat = accumulate(src, rho, theta)  # 허프 누적 행렬 계산
    acc_dst = masking(acc_mat, 7, 3, thresh)  # 마스킹 처리 7행,3열
    lines = select_lines(acc_dst, rho, theta, thresh)  # 직선 가져오기
    return lines

def draw_houghLines(src, lines, nline):
    if len(src.shape) < 3:
        dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)  # 컬러 영상 변환
    else:
        dst = np.copy(src)
    min_length = min(len(lines), nline)

    for i in range(min_length):
        rho, radian = lines[i, 0, 0:2]  # 수직거리 , 각도 - 3차원 행렬임
        a, b = math.cos(radian), math.sin(radian)
        pt = (a * rho, b * rho)  # 검출 직선상의 한 좌표 계산
        delta = (-1000 * b, 1000 * a)  # 직선상의 이동 위치
        pt1 = np.add(pt, delta).astype('int')
        pt2 = np.subtract(pt, delta).astype('int')
        cv2.line(dst, tuple(pt1), tuple(pt2), (0, 255, 0), 1, cv2.LINE_AA)

    return dst

#image = cv2.imread('images/hough.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.imread('add1.jpg', cv2.IMREAD_COLOR) # 그레이말고 칼라로 읽어옴
if image is None: raise Exception("영상 파일 읽기 에러")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 일단 그레이로 저장
blur  = cv2.GaussianBlur(gray, (5, 5), 2, 2) # 가우시안블러링
canny = cv2.Canny(blur, 50, 150, 5) # 캐니에지 검출

rho, theta = 1,  np.pi / 180
# lines1 = houghLines(canny, rho, theta, 80)
lines2 = cv2.HoughLines(canny, rho, theta, 80) # 허프라인 생성
# dst1 = draw_houghLines(canny, lines1, 7)
# dst2 = draw_houghLines(canny, lines2, 7)
my_dst = draw_houghLines(canny, lines2, 20) # 캐니에지에 허프라인
dst2 = draw_houghLines(image, lines2, 20) # 이미지에 허프라인

cv2.imshow("image", image)
cv2.imshow("canny", canny)
cv2.imshow("my_dst", my_dst)
#cv2.imshow("detected lines", dst1)
cv2.imshow("detected lines_OpenCV", dst2)
cv2.waitKey(0)