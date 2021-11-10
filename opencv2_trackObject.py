import cv2
import numpy as np
from matplotlib import pyplot as plt
from cv2 import *

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    ## we use HSV color space, where
    ## h = hue, the color (0 to 255)
    ## s = saturation
    ## v = brigthness
    HSV_FRAME = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    ## blue color
    lower_blue = np.array([101,50,50])
    upper_blue = np.array([110,255,255])

    ## create a mask wich only allows blue color to pass
    blueMask = cv2.inRange(HSV_FRAME, lower_blue, upper_blue)

    ## find the contour of the blue object
    cnts = cv2.findContours(blueMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    for c in cnts:
        ## Create the rectangle around it
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (36,255,12), 2)

    cv2.imshow('mask', blueMask)
    cv2.imshow('original', frame)

    ## show both the frame & the mask
    ##cv2.imshow('frame', frame)
    ##cv2.imshow('mask', blueMask)

    ## put together frame & mask, to only show the object with that color
    ##blue = cv2.bitwise_and(frame, frame, mask = blueMask)
    ##cv2.imshow('blue', blue)

    ## stop if we press q
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
