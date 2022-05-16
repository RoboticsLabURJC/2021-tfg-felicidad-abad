import cv2
import numpy as np

cap = cv2.VideoCapture('xiyao.mp4')

if (cap.isOpened()== False):
  print("Error opening video  file")

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    cv2.imshow('Frame', frame)

    ## we use HSV color space, where
    ## h = hue, the color (0 to 255)
    ## s = saturation
    ## v = brigthness
    HSV_FRAME = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    ## blue color
    lower_blue = np.array([100,150,0])
    upper_blue = np.array([140,255,255])

    ## create a mask wich only allows blue color to pass
    blueMask = cv2.inRange(HSV_FRAME, lower_blue, upper_blue)

    ## show both the frame & the mask
    ##cv2.imshow('frame', frame)
    cv2.imshow('mask', blueMask)

    ## put together frame & mask, to only show the object with that color
    blue = cv2.bitwise_and(frame, frame, mask = blueMask)
    cv2.imshow('blue', blue)

    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  else:
    break

cap.release()
cv2.destroyAllWindows()
