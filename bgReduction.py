import cv2
import numpy as np

cap = cv2.VideoCapture("people-walking.mp4")
fgBg = cv2.createBackgroundSubtractorMOG2()

while True:
	ret, frame = cap.read()
	fgMask = fgBg.apply(frame)

	cv2.imshow("original", frame)
	cv2.imshow("fg", fgMask)

	k = cv2.waitKey(30) & 0xFF
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()
