import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np
img= cv2.imread('image/watch.jpg',cv2.IMREAD_COLOR)
watch_face=img[37:111,107:194]
img[0:74,0:87]=watch_face
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
