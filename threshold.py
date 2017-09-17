import cv2
import numpy as np
img=cv2.imread('bookpage.jpg')
grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,threshold=cv2.threshold(grayscale,12,255,cv2.THRESH_BINARY)
#now we are using adaptive threshold
th=cv2.adaptiveThreshold(grayscale,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
#otsu threshold
retval2,threshold2 = cv2.threshold(grayscale,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('original image',img)
cv2.imshow('threshold image ', threshold)
cv2.imshow("adaptive threshold",th)
cv2.imshow("otsu threshold",threshold2)
cv2.waitKey(0)

cv2.destroyAllWindows()
