import numpy as np
import cv2

cap = cv2.VideoCapture(0) #0 is the number is the number of the webcam you want to access (if there are multiple; 0 just accesses the first one)

while True:
    ret, frame = cap.read() 
    # cap.read() returns a numpy array which will represent the image being captured itself. ret just tells you if the capture is 
    # actually successful or not (in case it fails if webcam is used by another application at the same time) 

    width = int(cap.get(3)) # getting the value of '3' which is the identifier for width
    height = int(cap.get(4))

    image = np.zeros(frame.shape,np.uint8)
    #creates an empty array of zeros (just black) the same size as frame (frame.shape)
    smaller_frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)# x and y pixels multiplier instead of giving raw pixel size 
    image[:height//2,:width//2] = cv2.rotate(smaller_frame,cv2.ROTATE_180)#top left
    image[height//2:,:width//2] = smaller_frame#bottom left
    image[:height//2,width//2:] = cv2.rotate(smaller_frame,cv2.ROTATE_180)#top right
    image[height//2:,width//2:] = smaller_frame#bottom right
    
    cv2.imshow("Frame",image)
    if cv2.waitKey(1) == ord('q'): #ordinal just returns int value as waitKey compares key value in ASCII
        break

cap.release() #release the resource being used (camera)
cv2.destroyAllWindows()