import cv2
import numpy as np

kernal = np.ones((5,5),np.uint8) 
img = cv2.imread("colorpic.jpg")
img_resize = cv2.resize(img,(500,300))
img_cropped = img_resize[0:100,100:300]


img_blur = cv2.GaussianBlur(img_resize,(7,7),3)
img_gray = cv2.cvtColor(img_resize,cv2.COLOR_BGR2GRAY)
img_canny = cv2.Canny(img_resize,100,100)
img_dilation = cv2.dilate(img_canny,kernal,iterations=1)
img_eroded = cv2.erode(img_dilation,kernal,iterations=1)

#cv2.imshow("dilated image", img_dilation)
#cv2.imshow("image", img_resize)
#cv2.imshow("cropped image",img_cropped)
#cv2.imshow("gray image",img_gray)
#cv2.imshow("blur image",img_blur)
#cv2.imshow("canny image",img_canny)
#cv2.imshow("eroded image", img_eroded)

cv2.waitKey(0)
