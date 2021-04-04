import cv2


cap_video = cv2.VideoCapture("video_1.mp4")

while True:
    succes, play_video = cap_video.read()
    cv2.imshow("video", play_video)
    if cv2.waitKey(1) & 0xff == ord('e'):
        break

cap_webcam = cv2.VideoCapture(0)

while True:
    succes2, play_webcam = cap_webcam.read()
    cv2.imshow("webcam,", play_webcam)
    if cv2.waitKey(1) & 0xff == ord('e'):
        break      