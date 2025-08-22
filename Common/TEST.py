import numpy as np, cv2

# m1 = np.array([1, 2, 3, 1, 2, 3])
# m2 = np.array([3, 3, 4, 2, 2, 3])
# m3 = m1 + m2
# m4 = m1 - m2
#
# print("[M1] = %s" %m1)
# print("[M2] = %s" %m2)
# print("[M3] = %s" %m3)
# print("[M4] = %s" %m4)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
m1 = np.array(data).reshape(2, 2, 3)  # Reshape to (height, width, 3)

r, g, b = cv2.split(m1)

print("[m1] %s" % m1)
print("[r, g, b] = %s, %s, %s" % (r, g, b))