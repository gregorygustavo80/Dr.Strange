import cv2
import mediapipe as mp
import pyautogui
import time
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
import webbrowser

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

def screenshot():
    pyautogui.hotkey('win', 'shift', 's')
    
def mute():
    volume.SetMasterVolumeLevelScalar(0.0, None) 

def volume_up():
    volume.SetMasterVolumeLevelScalar(0.8, None) 

def whatsapp():
    url = "https://web.whatsapp.com/"
    webbrowser.open(url)

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def is_hand_closed(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    dist_thumb_index = thumb_tip.y - index_finger_tip.y
    dist_thumb_middle = thumb_tip.y - middle_finger_tip.y
    dist_thumb_ring = thumb_tip.y - ring_finger_tip.y
    dist_thumb_pinky = thumb_tip.y - pinky_tip.y

    if (dist_thumb_index < 0 and dist_thumb_middle < 0 and 
        dist_thumb_ring < 0 and dist_thumb_pinky < 0):
        return True
    else:
        return False

def index_finger(hand_landmarks):
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    middle_finger_dip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP]
    ring_finger_dip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP]
    pinky_dip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP]

    if (middle_finger_tip.y > middle_finger_dip.y and
        ring_finger_tip.y > ring_finger_dip.y and
        pinky_tip.y > pinky_dip.y):
        return True
    else:
        return False
    
def hello(hand_landmarks):
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]

    index_finger_dip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP]
    middle_finger_dip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP]
    ring_finger_dip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP]

    if (index_finger_tip.y > index_finger_dip.y and
        middle_finger_tip.y > middle_finger_dip.y and
        ring_finger_tip.y > ring_finger_dip.y):
        return True
    else:
        return False
    
def v_sign(hand_landmarks):
    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    ring_finger_dip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP]
    pinky_dip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP]

    if (ring_finger_tip.y > ring_finger_dip.y and 
        pinky_tip.y > pinky_dip.y):
        return True
    else:
        return False

while True:
    ret, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            if is_hand_closed(hand_landmarks):
                screenshot()
                time.sleep(2)
                
            elif index_finger(hand_landmarks):
                volume_up()
                time.sleep(2)
        
            elif v_sign(hand_landmarks): 
                mute()
                time.sleep(2)
                
            elif hello(hand_landmarks):
                whatsapp()
                time.sleep(2)
            
    cv2.imshow('Dr.Strange', frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()

