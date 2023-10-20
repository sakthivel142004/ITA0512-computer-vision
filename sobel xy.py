import cv2
import numpy as np
image_path ="alone.jpeg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
gradient_magnitude = np.uint8(gradient_magnitude)
cv2.imshow('Original Image', image)
cv2.imshow('Gradient Magnitude (Sobel XY)', gradient_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()
