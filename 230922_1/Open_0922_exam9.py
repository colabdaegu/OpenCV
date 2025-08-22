import numpy as np, cv2

image = np.zeros((600, 400, 3), np.uint8)

title1 = 'WINDOW'
coordinate1 = (100,100)

cv2.rectangle(image, coordinate1, (coordinate1[0]+200, coordinate1[1]+300), (0,0,255), cv2.FILLED)

cv2.imshow(title1, image)
cv2.waitKey(0)
cv2.destroyAllWindows()