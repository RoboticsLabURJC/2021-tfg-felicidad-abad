import cv2
import numpy as np

image = cv2.imread('lena.jpg')

## pasamos a gris la imagen
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_,binary = cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV)

cv2.imshow('thresholding',binary)

if cv2.waitKey(0):
    cv2.destroyAllWindows()
