import cv2
import mediapipe as mp
from mediapipe.python.solutions import hands
from mediapipe.python.solutions import drawing_utils
 

mp_drawing = drawing_utils
hand_dectector = hands.Hands()

cam = cv2.VideoCapture(0)
while True:

    ret,frame = cam.read()

    #applying the hand tracking model
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #mediapipe uses RGB and opencv reads color in bgr to conversion is needed
    results = hand_dectector.process(frame)

    #draw on the image 
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR) #convert back to opencv format as now rest of the program will be handled by it
    if results.multi_hand_landmarks: #if any hand landmarks are even detected 
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame,hand_landmarks,connections=hands.HAND_CONNECTIONS)
            # hand_landmarks is the detected hand(s) and using the connections param we can determine which points on the detected
            # hand to connect which is a predefined list

    cv2.imshow("Hand Tracker",frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
