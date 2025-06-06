import cv2
import matplotlib.pyplot as plt
image = cv2.imread('cat.jpg')
#converting bgr to rgb
image_rgb = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB image")
plt.show()
#converting to grey scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap= 'gray')
plt.title("Gray scale image")
plt.show()
#cropping the image
cropped_image = image [100:300,200:400]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB )
plt.imshow(cropped_rgb)
plt.title("Cropped image")
plt.show()