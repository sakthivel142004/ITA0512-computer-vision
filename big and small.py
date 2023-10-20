import cv2
image_path ="alone.jpeg"
image = cv2.imread(image_path)
bigger_scale_factor = 1.5
smaller_scale_factor = 0.7
bigger_dimensions = (int(image.shape[1] * bigger_scale_factor), int(image.shape[0] * bigger_scale_factor))
smaller_dimensions = (int(image.shape[1] * smaller_scale_factor), int(image.shape[0] * smaller_scale_factor))
bigger_image = cv2.resize(image, bigger_dimensions)
smaller_image = cv2.resize(image, smaller_dimensions)
cv2.imshow('Original Image', image)
cv2.imshow('Bigger Image', bigger_image)
cv2.imshow('Smaller Image', smaller_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
