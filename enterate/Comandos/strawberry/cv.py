#import cv2
#from matplotlib import pyplot as plt
#import numpy as np
#from math import cos, sin
#from __future__ import division
#image = berry.jpg
#def find_strawberry(image);

#image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

import numpy as np
import cv2

# Load an color image in grayscale
imgBW = cv2.imread('berry.jpg',0)
img2Color = cv2.imread('berry.jpg',1)
img3ColorAlpha = cv2.imread('berry.jpg',-1)
print(imgBW)
print(img2Color)
print(img3ColorAlpha)

cv2.imshow('imgBW',imgBW)
cv2.waitKey(100)
cv2.destroyAllWindows()