import cv2
import numpy as np
img=cv2.imread("dinesh.jpg",0)
row,col=img.shape
mat=np.float32([[1,0,100],[0,1,50]])
trans=cv2.warpAffine(img,mat,(col,row))
cv2.imshow('original',img)
cv2.imshow('translate',trans)
cv2.waitkey(0)
cv2.destroyAllWindows()
                          
