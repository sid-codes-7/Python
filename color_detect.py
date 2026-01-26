import cv2
import numpy as np
from PIL import Image

def get_hsv_bounds(bgr):
    hsv = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)[0][0] #get the bgr value and hue values
    h = hsv[0]
    low = np.array([max(h - 10, 0), 100, 100], dtype=np.uint8) #get the max limit
    high = np.array([min(h + 10, 180), 255, 255], dtype=np.uint8)# min limit
    return low, high

color_bgr = [0, 255, 255]  # yellow
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise Exception("Camera not accessible")

lower, upper = get_hsv_bounds(color_bgr)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    mask = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), lower, upper) #make the mask for the required color range
    box = Image.fromarray(mask).getbbox() 
    if box:
        frame = cv2.rectangle(frame, box[:2], box[2:], (0, 255, 0), 5) #make the box to show where each pixel of that color is 

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
