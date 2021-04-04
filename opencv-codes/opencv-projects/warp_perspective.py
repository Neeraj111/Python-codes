import cv2
import numpy as np

width, height = 700,400
counter = 0
array = np.zeros((4,2),int)

def click(event,x,y,flags,param):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),1,(0,0,0),2)
        print(x,y)
        array[counter] = x,y
        counter += 1 


img = cv2.imread("colorpic.jpg")
img = cv2.resize(img,(700,400))

while True:
    if counter == 4:
        pts1 = np.float32([array[0],array[1],array[2],array[3]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        warp_output = cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow("warp_perspective",warp_output)
    
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',click)

    cv2.imshow("image",img)
    if  cv2.waitKey(1) & 0xff ==ord('e'):
        break
    
