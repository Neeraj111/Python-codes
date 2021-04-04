import cv2
import numpy as np

img = np.zeros((400,400,3),np.uint8)
img[:] = (255,255,255)

cv2.line(img,(0,0),(400,400),(0,0,0),2)
cv2.rectangle(img,(0,0),(150,150),(0,0,0),2)
cv2.circle(img,(300,300),50,(0,0,0),2)
cv2.putText(img,"learning openCV",(220,20),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),2)
#img_rectangle = cv2.rectangle((0:200))

cv2.imshow("img",img)


cv2.waitKey(0)