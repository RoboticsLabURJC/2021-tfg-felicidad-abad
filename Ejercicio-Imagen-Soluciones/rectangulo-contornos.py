import cv2
import numpy as np

image = cv2.imread('lena.jpg')

## pasamos a gris la imagen
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)

contornos,imagen1 = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image, contornos, -1, (0,255,0), 3)

for obj in contornos:
    rect = cv2.contourArea(obj)
    #if rect > 1000 and rect < 10000:
    (x, y, w, h) = cv2.boundingRect(obj)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1, cv2.LINE_AA)

cv2.imshow('recuadro objetos',image)

if cv2.waitKey(0):
    cv2.destroyAllWindows()
