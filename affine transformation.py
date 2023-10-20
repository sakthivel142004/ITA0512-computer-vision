import cv2
import numpy as np
image_path = "alone.jpeg"
image = cv2.imread(image_path)
original_points = np.float32([[50, 50], [200, 50], [50, 200]])
transformed_points = np.float32([[10, 100], [200, 50], [100, 250]])
affine_matrix = cv2.getAffineTransform(original_points, transformed_points)
transformed_image = cv2.warpAffine(image, affine_matrix, (image.shape[1], image.shape[0]))
cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
