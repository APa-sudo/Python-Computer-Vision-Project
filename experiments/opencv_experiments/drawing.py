import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame,(0,0),(width,height),(255, 0,0),10) #starting coord, ending coord, color(in the form bgr NOT RGB!!), thickness in pixels
    img = cv2.line(img,(0,height),(width,0),(0, 255,0),5)

    img = cv2.rectangle(img,(100,100),(200,200),(128,128,128),5) #top left, bottom right, color , thickness (-1 to fill)

    img = cv2.circle(img,(300,300),60,(0,0,255),-1) #center postion,radius,color,fill/thickness

    font = cv2.FONT_HERSHEY_SIMPLEX
    img= cv2.putText(img,"This is OpenCV",(0,height-10),font,2,(0,0,0),4,cv2.LINE_AA) #text, bottom left coord of text, font type,font scale, color, thickness, line type(preferred LINE_AA even as per offical doc)
    cv2.imshow("Video Feed",img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()







