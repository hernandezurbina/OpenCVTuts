import cv2
import numpy as np

# opencv-template-matching-python-tutorial.jpeg
# opencv-template-for-matching.jpeg

imgBGR = cv2.imread("opencv-template-matching-python-tutorial.jpeg")
imgGray = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)

template = cv2.imread("opencv-template-for-matching.jpeg", 0)

width, height = template.shape[::-1]

res = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
	cv2.rectangle(imgBGR, pt, (pt[0]+width, pt[1]+height), (0,255,255), 2)

cv2.imshow("detected", imgBGR)
cv2.waitKey(0)
cv2.destroyAllWindows()

