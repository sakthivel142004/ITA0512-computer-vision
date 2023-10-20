import cv2
import numpy as np
image_path = "alone.jpeg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = cv2.magnitude(gradient_x, gradient_y)
scaling_factor = 1.5
sharpened_image = image + scaling_factor * gradient_magnitude
cv2.imshow('Original Image', image)
cv2.imshow('Gradient Magnitude', gradient_magnitude)
cv2.imshow('Sharpened Image (Gradient Masking)', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
