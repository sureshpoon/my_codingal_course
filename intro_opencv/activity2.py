import cv2
image = cv2.imread('smile.jpg')
#convert the img to grey scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#resize the grey scale img to 224 x 224
resize_image = cv2.resize(gray_image, (224, 224))
#display the gray scale image 
cv2.imshow ('image', resize_image)
key = cv2.waitKey (0)
if key == ord('s'):
    cv2.imwrite('grayscale_img.jpg', resize_image)
    print ("image saved")
else : 
    print("Image not saved")

cv2.destroyAllWindows()
print (f"Gray scal image dimensions : {resize_image.shape}")        