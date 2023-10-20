import cv2
import numpy as np
image_path ="alone.jpeg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
blurred_image = cv2.GaussianBlur(image, (5, 5), 2)
high_pass_image = cv2.subtract(image, blurred_image)
scaling_factor = 1.5
sharpened_image = cv2.addWeighted(image, 1 + scaling_factor, high_pass_image, -scaling_factor, 0)
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('High-Pass Image', high_pass_image)
cv2.imshow('Sharpened Image (Unsharp Masking)', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
