import cv2 
#load the img 
image = cv2.imread("smile.jpg")
#resize the window without chaning the img size
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 800, 500)
#display the img
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(f"image size: {image.shape}")