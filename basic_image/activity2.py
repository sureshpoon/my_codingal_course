import cv2 
import numpy as np 
import matplotlib.pyplot as plt
image = cv2.imread('cat.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#rotating the img by 45 degrees
(h, w)= image.shape[:2] 
center = (w // 2, h // 2 )
m = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image , m, (w, h))
rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated image")
plt.show() 
#increase the brightness
brightness_matrix = np.ones(image.shape, dtype= "uint8") * 50
brighter = cv2.add(image, brightness_matrix)
brighter_rgb = cv2.cvtColor (brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb) 
plt.title("Bright image")
plt.show()
