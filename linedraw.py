import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np
img= cv2.imread('image/watch.jpg',cv2.IMREAD_COLOR)
#line draw on the image
cv2.line(img,(0,0),(250,250),(0,255,0),15)
# rectangle draw on the image
cv2.rectangle(img,(15,25),(200,150),(0,0,255),15)
#circle draw on the image
cv2.circle(img,(200,63),50,(0,255,250),-1)
#polygon draw on the image
pts=np.array([[100,50],[200,300],[700,200],[500,100]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,0,0),3)

#write a text in the image
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Welcome to jungle',(10,50),font,2,(200,255,155), 5, cv2.CV_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
