import cv2
import numpy as np

cap = cv2.VideoCapture('xiyao.mp4')

if (cap.isOpened()== False):
  print("Error opening video  file")

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:

    gris = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gris,100,255,cv2.THRESH_BINARY)

    #ENcontrar los contornos
    contornos1,hierarchy1 = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
          cv2.CHAIN_APPROX_NONE)

    #Pintamos los contornos sobre el frame
    cv2.drawContours(frame, contornos1, -1, (0,255,0), 3)
    #Sacamos en una ventana nueva el video completo
    cv2.imshow('video',frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  else:
    break

cap.release()
cv2.destroyAllWindows()
