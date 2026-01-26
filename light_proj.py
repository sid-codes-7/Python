#Project: See real time light and color data through a webcam 

#webcam feature 
import cv2
import numpy as np

stream = cv2.VideoCapture(0)

if not stream.isOpened():
    print("No stream :(")
    exit()

fps = stream.get(cv2.CAP_PROP_FPS)
width = int(stream.get(3))
height = int(stream.get(4))

output = cv2.VideoWriter("assets/4_stream.mp4", cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps=fps, frameSize=(width, height), isColor=False)

def get_average_brightness_hsv(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #convert rgb to hsv(more accurate brightness calcs)
    v_channel = hsv_frame[:, :, 2]#get Value channel accuratlt get brightness level 
    average_brightness = cv2.mean(v_channel)[0] #calculate the mean for the brightness so we dont get extreme 
                                                #brightness values
    return average_brightness#and here we just return the brightness

while(True):
    ret, frame = stream.read()
    if not ret:
        print("No more stream :(")
        break

    output.write(frame)

    avg_brightness = get_average_brightness_hsv(frame)

    # Display the average brightness on the frame 
    text = f"Avg Brightness: {avg_brightness:.2f} LUX"
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Webcam!", frame)

    #'q' to close the webcam!!
    if cv2.waitKey(1) == ord('q'):
        break

stream.release()
cv2.destroyAllWindows()
