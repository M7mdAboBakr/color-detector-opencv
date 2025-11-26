import cv2
import numpy as np
from PIL import Image
from util import get_limits

yellow = [0, 255, 255] # Yellow in BGR
webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()

    # convert to HSV
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # getting color limits
    lower_limit, upper_limit = get_limits(yellow)

    # getting mask
    mask = cv2.inRange(frame_hsv, lower_limit, upper_limit)

    # convert to PIL
    mask_pil = Image.fromarray(mask)

    # boundry box of mask
    bbox = mask_pil.getbbox()

    # draw boundry box if yellow detected
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

    cv2.imshow('webcam', frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break


webcam.release()
cv2.destroyAllWindows()