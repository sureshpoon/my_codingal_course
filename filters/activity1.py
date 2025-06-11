import cv2
import numpy as np 

def apply_color_filter(image, filter_type):
    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:, :, 2] = np.clip(filtered_image[:, :, 2] + 50, 0, 255)
    elif filter_type == "blue_tint":
        filtered_image[:, :, 0] = np.clip(filtered_image[:, :, 0] + 50, 0, 255)  
    elif filter_type == "green_tint":
        filtered_image[:, :, 1] = np.clip(filtered_image[:, :, 1] + 50, 0, 255)
    elif filter_type == "sepia":
        sepia_filter = np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.392, 0.769, 0.189]])
        filtered_image == cv2.transform(filtered_image, sepia_filter)
        filtered_image = np.clip(filtered_image, 0, 255).astype(np.uint8)
    elif filter_type == "black_white":
        filtered_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2GRAY)
        filtered_image = cv2.cvtColor (filtered_image, cv2.COLOR_GRAY2BGR) 
    elif filter_type == "negative":
        filtered_image = 255 - filtered_image 
    return filtered_image
image_path = "abc.jpg"
image = cv2.imread(image_path)
if image is None:
    print ("Image not found")
else :
    filter_type = "original" 
    print("Press the following keys to apply filters : ")
    print("Red tint(r)")
    print ("Blue tint(b)")
    print("Green tint(g)") 
    print("Sepia(s)")
    print("Negative(n)")
    print("Black and white(w)")
    print("original image(o)")
    print("Quit(q)")
    while True :
        filtered_image = apply_color_filter(image, filter_type)
        cv2.imshow("filtered image", filtered_image)
        key = cv2.waitKey(1) & 0xFF 
        if key == ord('r') :
            filter_type = "red_tint"
        elif key == ord('b') :
            filter_type = "blue_tint"
        elif key == ord('g') :
            filter_type = "green_tint"
        elif key == ord('s') :
            filter_type = "sepia"
        elif key == ord('n'):
            filter_type = "negative"
        elif key == ord ('w') :
            filter_type = "black_white"
        elif key == ord('o'):
            filter_type = "original"
        elif key == ord('q'):
            print("Quitting")
            break
        else:
            pass
    print("Invaid input, please use keys like (r, b, g, s, w, n, o, q)")
cv2.destroyAllWindows()        










          

    