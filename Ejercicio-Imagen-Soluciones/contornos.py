import cv2
import numpy as np

image = cv2.imread('lena.jpg')

## pasamos a gris la imagen
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gris,100,255,cv2.THRESH_BINARY)

contornos,imagen1 = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image, contornos, -1, (0,255,0), 3)

cv2.imshow('contornos',image)

if cv2.waitKey(0):
    cv2.destroyAllWindows()
