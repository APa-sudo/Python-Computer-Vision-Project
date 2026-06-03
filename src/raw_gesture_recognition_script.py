def pinch_distance(index_y,index_x,thumb_y,thumb_x):
        return ((index_y-thumb_y)**2 + ((index_x-thumb_x)**2))**0.5



import cv2
from mediapipe.python.solutions import hands
from mediapipe.python.solutions import drawing_utils
# from _ctypes import cast,POINTER #getting low level APIs of windows as they are mostly writte in C/C++
# from comtypes import CLSCTX_ALL # searches everywhere(CLSCTX_ALL) in the required Windows files to activiate the com (component object module) objects
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume #helper/wrapper library to access Audio Utilities 

# devices = AudioUtilities.GetSpeakers()

# interface = devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
# volume = cast(interface,POINTER(IAudioEndpointVolume))

mp_draw = drawing_utils
hand_detector = hands.Hands()
cam = cv2.VideoCapture(0)
cam.set(3,1980)
cam.set(4,1080)
width = int(cam.get(3))
height = int(cam.get(4))
previous_gesture = "UNKNOWN"
detected_gesture = "UNKNOWN"
stable_gesture = "UNKNOWN"
pinch_on = 0.04
#pinch_off = 0.06

counter = 0

while True:
        ret,frame = cam.read()
        processed_frame = cv2.resize(frame,(640,480))
        processed_frame= cv2.cvtColor(processed_frame,cv2.COLOR_BGR2RGB)
        results =  hand_detector.process(processed_frame)
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        detected_gesture = "UNKNOWN"
        if stable_gesture == "UNKNOWN":
            cv2.putText(frame,stable_gesture,(30,50),font,2,(0,0,255),4,cv2.LINE_AA)
        else:
            cv2.putText(frame,stable_gesture,(30,50),font,2,(0,255,0),4,cv2.LINE_AA)

        processed_frame = cv2.cvtColor(processed_frame,cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame,hand_landmarks,hands.HAND_CONNECTIONS)
                thumb = hand_landmarks.landmark[4]
                thumb_mcp = hand_landmarks.landmark[2]
                thumb_cmc = hand_landmarks.landmark[1]
                index = hand_landmarks.landmark[8]
                index_pip = hand_landmarks.landmark[6]
                index_mcp = hand_landmarks.landmark[5]
                middle = hand_landmarks.landmark[12]
                middle_pip = hand_landmarks.landmark[10]
                middle_mcp = hand_landmarks.landmark[9]
                ring = hand_landmarks.landmark[16]
                ring_mcp = hand_landmarks.landmark[13]
                ring_pip = hand_landmarks.landmark[14]
                pinky = hand_landmarks.landmark[20]
                pink_mcp = hand_landmarks.landmark[17]
                pink_pip = hand_landmarks.landmark[18]

                #to avoid using old position coordinates for the fingers in case of noisy frames 
                if stable_gesture == "PINCH":
                      thumb_x = int(thumb.x*width)
                      thumb_y = int(thumb.y*height)
                      index_x = int(index.x*width)
                      index_y = int(index.y*height)
                      print(f"{pinch_distance(index.y,index.x,thumb.y,thumb.x):.3f}")
                      cv2.line(frame,(thumb_x,thumb_y),(index_x,index_y),(255,0,0),5)

                #FIST LOGIC
                if (index.y>index_pip.y) and (middle.y>middle_pip.y) and (ring.y>ring_pip.y) and (pinky.y>pink_pip.y):
                    detected_gesture = "FIST"

                #PALM LOGIC
                elif (index.y<index_pip.y<index_mcp.y) and (middle.y<middle_pip.y<middle_mcp.y) and (ring.y<ring_pip.y<ring_mcp.y) and (pinky.y<pink_pip.y<pink_mcp.y) and (thumb.y<thumb_mcp.y<thumb_cmc.y):
                    detected_gesture = "PALM"
                    
                #PINCH LOGIC
                elif pinch_distance(index.y,index.x,thumb.y,thumb.x)<pinch_on:
                    detected_gesture = "PINCH"
                else:
                        detected_gesture = "UNKNOWN"

                if detected_gesture == previous_gesture:
                    counter += 1
                else: counter = 1

                if counter>=10:
                    stable_gesture = detected_gesture
                    counter = 0

        previous_gesture = detected_gesture
                

        cv2.imshow("Gesture Detection",frame)

        if cv2.waitKey(1) == ord('q'):
            break
cam.release()
cv2.destroyAllWindows()
