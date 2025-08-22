import numpy as np, cv2

image = np.ones((300, 300), np.uint8) * 255
def onMouse(event, x, y, flags, param):
    global title
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, pt, 5, 100, 1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(image, pt, pt+(30,30), 100, 2)
        cv2.imshow(title, image)


pt = (100, 100)

title = "Draw Event"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()