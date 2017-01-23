import cv2
import numpy as np

img = cv2.imread("bookpage.jpeg")
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayScaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayScaled, 12, 255, cv2.THRESH_BINARY)

gauss = cv2.adaptiveThreshold(grayScaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
	cv2.THRESH_BINARY, 115, 1)

retval3, otsu = cv2.threshold(grayScaled, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("original", img)
cv2.imshow("thresholded", threshold)
cv2.imshow("thresholded BW", threshold2)
cv2.imshow("thresholded Gaussian", gauss)
cv2.imshow("thresholded Otsu", otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()
