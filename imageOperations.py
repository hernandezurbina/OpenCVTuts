import numpy as np
import cv2

img = cv2.imread("watch.jpeg", cv2.IMREAD_COLOR)

# img[100:150, 100:250] = [255, 255, 255]

# watchFace = img[37:111, 107:194]
# img[0:74, 0:87] = watchFace

img1 = cv2.imread("img1.png")
img2 = cv2.imread("img2.png")
img3 = cv2.imread("img3.png")

# add = img1 + img2
# add = cv2.add(img1, img2)
# weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

# cv2.imshow("image", weighted)

rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

# cv2.imshow("image", mask)

maskInv = cv2.bitwise_not(mask)
img1BG = cv2.bitwise_and(roi, roi, mask=maskInv)
img3FG = cv2.bitwise_and(img3, img3, mask=mask)

dst = cv2.add(img1BG, img3FG)
img1[0:rows, 0:cols] = dst

cv2.imshow("image", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()


