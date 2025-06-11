import cv2
import numpy as np
import matplotlib.pyplot as plt
def display_image(title, image):
    plt.figure(figsize = (8, 6))
    if len(image.shape) == 3 :
        plt.imshow(image, cmap = 'gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show() 

def interactive_edge_detection(image_path):
    image = cv2.imread(image_path)
    if image is None :
        print("Error image not found!")
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    display_image("Original gray scale image", gray_image) 
    print("1. Sobel edge detection") #highlights the edges
    print("2. Canny edge detection") #smoothes out the image 
    print("3. Laplacion edge detection") #highlights the edges
    print("4. Gaussian smoothing")
    print("5. Median filtering")  
    print("6. Exit")
    while True :
        choice = input ("Enter your choice(1-6) : ")
        if choice == "1" :
            sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize = 3)
            sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize = 3)
            combine_sobel = cv2.magnitude(sobel_x, sobel_y)
            combine_sobel = np.uint8(np.absolute(combine_sobel).astype(np.uint8))
            display_image("Sobel edge detection", combine_sobel)
        elif choice == "2":
            print("Adjust threshold for canny(default : 100 & 200)")
            lower_thresh = int (input("Enter lower threshold : "))
            upper_thresh = int (input("Enter uper threshold : "))
            edges = cv2.Canny(gray_image, lower_thresh, upper_thresh)
            display_image("Canny egde detection", edges) 
        elif choice == "3":
            laplacion = cv2.Laplacion(gray_image, cv2.CV_64F) 
            edges = np.uint8(np.absolute(laplacion).astype(np.uint8))
            display_image("Laplacion edge detection", edges)
        elif choice == "4" :
            print("Adjust kernel size for gaussian blur (default = 15) ")
            kernel_size = int (input("Enter kernel size(odd number) : "))
            blur = cv2.GaussianBlur(gray_image, (kernel_size, kernel_size), 0)
            display_image("Gaussian smoothing", blur)
        elif choice == "5" :
            print ("Adjust kernel size for median filtering (default = 5)")
            kernel_size = int(input("Enter the kernel size(odd number) : "))
            median_filter = cv2.medianBlur(gray_image, kernel_size)
            display_image("Median filtering", median_filter)
        elif choice == "6":
            print("Exiting")
            break 
        else :
            print("Invalid choice, please select a number between (1-6)")
interactive_edge_detection('example.jpeg')

    
        


         



    

        

        



            
    