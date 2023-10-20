import cv2
import numpy as np
image_path = "alone.jpeg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
edges = cv2.Canny(blurred_image, threshold1=30, threshold2=100)
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
