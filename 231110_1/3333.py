import cv2

def onTrackbar(th, dummy):
    th1 = cv2.getTrackbarPos('th1', 'canny edge')
    th2 = cv2.getTrackbarPos('th2', 'canny edge')
    canny2 = cv2.Canny(image, th1, th2)
    cv2.imshow("canny edge", canny2)

image = cv2.imread("dog_test.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

cv2.imshow("canny edge", image)
cv2.createTrackbar("th1", "canny edge", 50, 300, lambda x: onTrackbar(x, 0))
cv2.createTrackbar("th2", "canny edge", 100, 300, lambda x: onTrackbar(x, 0))

onTrackbar(0, 0) # Initial display
cv2.waitKey(0)