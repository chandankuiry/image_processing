import cv2
import numpy as np

img=cv2.imread('download.jpg')


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([30,150,50])
upper_red = np.array([255,255,180])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img,img, mask= mask)

#lets remove noise from image
#1st method
kernel=np.ones((15,15), np.float32)/225
smooth=cv2.filter2D(res,-1,kernel)
#2nd method gaussian blur
blur = cv2.GaussianBlur(res,(15,15),0)
#3rd method median
median = cv2.medianBlur(res,15)
bilateral = cv2.bilateralFilter(res,15,75,75)



cv2.imshow('frame',img)
cv2.imshow('res',res)
cv2.imshow('smooth',smooth)
cv2.imshow('Gaussian Blurring',blur)
cv2.imshow('medianBlur',median)
cv2.imshow('bilateral Blur',bilateral)


cv2.waitKey(0)
cv2.destroyAllWindows()
