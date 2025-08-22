import numpy as np
import cv2

image = np.zeros((300, 400), np.uint8)
image.fill(100)

title1 = 'AUTOSIZE'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)

cv2.imshow(title1, image)
cv2.resizeWindow(title1, 500, 600)
cv2.waitKey(0)
cv2.destroyAllWindows()