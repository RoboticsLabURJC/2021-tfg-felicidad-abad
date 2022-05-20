import cv2
import numpy as np

image = cv2.imread('lena.jpg')

## pasamos a gris la imagen
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imgUmbralizada = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('umbralizacion',imgUmbralizada)

if cv2.waitKey(0):
    cv2.destroyAllWindows()
