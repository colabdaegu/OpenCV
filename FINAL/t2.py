import cv2
def onTrackbar(th):
    th1 = cv2.getTrackbarPos('th1', 'canny edge')
    th2 = cv2.getTrackbarPos('th2', 'canny edge')
    canny2 = cv2.Canny(image, th1, th2)
    cv2.imshow("canny edge", canny2)
image = cv2.imread("images/prob2.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

cv2.imshow("canny edge", image)
cv2.createTrackbar("th1", "canny edge", 50, 300, onTrackbar)
cv2.createTrackbar("th2", "canny edge", 100, 300, onTrackbar)
onTrackbar(50)
cv2.waitKey(0)