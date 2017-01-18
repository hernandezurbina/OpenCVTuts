import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('watch.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('watch', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()