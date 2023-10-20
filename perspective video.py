import cv2
import numpy as np
cap = cv2.VideoCapture("D:/Samsung Galaxy A71/Movies/WhatsApp/VID-20230125-WA0039.mp4")
while True:
    ret, frame = cap.read()
    pts1 = np.float32([[200,300], [5, 2],[0, 4], [6, 0]])
    pts2 = np.float32([[0, 0], [4, 0],[0, 1], [4, 6]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (0, 0))
    cv2.imshow('frame', frame) # Initial Capture
    cv2.imshow('frame1', result) # Transformed Capture
    if cv2.waitKey(24) == 27:
        break
cap.release()
cv2.destroyAllWindows()
