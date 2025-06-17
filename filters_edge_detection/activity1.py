import cv2
import numpy as np
def apply_filter(image, filter_type) :
    filtered_image = image.copy()
    if filter_type == "red_tint" :
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 1] = 0
    elif filter_type == "green_tint" :
        filtered_image [:, :, 0] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "blue_tint":
        filtered_image [:, :, 1] = 0
        filtered_image [:, :, 2] = 0 
    elif filter_type == "sobel" :
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize = 3)
        sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize = 3)
        sobel_edges = np.sqrt(sobel_x**2, sobel_y**2)
        return sobel_edges.astype(np.uint8)
    elif filter_type == "canny" :
        gray_image = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
        canny_edges = cv2.Canny(gray_image, 100, 200)
        filtered_image = cv2.cvtColor(canny_edges, cv2.COLOR_GRAY2BGR)
    return filtered_image
image_path = "item2.jpg"
image = cv2.imread(image_path)
if image is None :
    print("Error : image is not found")
else :
    filter_type = "original"
    print("Press the folloeing keys to apply filters") 
    print ("r : red tint")
    print("g :green tint")
    print("b :blue tint")
    print("s : sobel edge detection")
    print("c : canny edge detection")
    print ("q : quit")
    while True :
        if filter_type == "original":
            display_image = image
        else :
            display_image = apply_filter(image, filter_type)
        cv2.imshow("Filtered image", display_image)    
        key = cv2.waitKey(1) & 0xFF
        if key == ord('r'):
            filter_type = "red_tint"
        elif key == ord ('g'):
            filter_type = "green_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('s'):
            filter_type = "sobel"
        elif key == ord('c'):
            filter_type = "canny"
        elif key == ord('q') :
            break 
        else :
            print("Invalid keys. Press r, g, b, s, c or q")
cv2.destroyAllWindows()

    
        
        

            
