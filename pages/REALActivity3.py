import numpy as np
import cv2
import matplotlib.pyplot as plt

# CHOICE 1
def translate_image():
    filename = input("Input image: ")
    image = cv2.imread(filename)
    dx = int(input("Enter the amount to translate along the X axis: "))
    dy = int(input("Enter the amount to translate along the Y axis: "))
    translation_matrix = np.float32([[1, 0, dx], [0, 1, dy]])
    translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
    plt.imshow(cv2.cvtColor(translated_image, cv2.COLOR_BGR2RGB))
    plt.title("Transformed Image")
    plt.show()

# CHOICE 2
def rotate_image():
    filename = input("Input image: ")
    image = cv2.imread(filename)
    angle = float(input("Enter the rotation angle in degrees: "))
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
    plt.title("Image Rotation")
    plt.show()

# CHOICE 3
def scale_image():
    filename = input("Input image: ")
    image = cv2.imread(filename)
    print("Please enter a number between decimals (0.05 ~ 1.5)") # REMEMBER PUT DECIMALS OR YOU FREEZE
    fx = float(input("Enter the scaling factor for X axis: "))
    fy = float(input("Enter the scaling factor for Y axis: "))
    scaled_image = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
    plt.imshow(cv2.cvtColor(scaled_image, cv2.COLOR_BGR2RGB))
    plt.title("Image Scaling")
    plt.show()

# CHOICE 4
def reflect_image():
    filename = input("Input image: ")
    image = cv2.imread(filename)
    print("Enter flip direction: ")
    print("1 for horizontal | 2 for vertical | 3 for both: ")
    flip_direction = input("")
    if flip_direction == '1':
        flipped_image = cv2.flip(image, 1)
    elif flip_direction == '2':
        flipped_image = cv2.flip(image, 0)
    elif flip_direction == '3':
        flipped_image = cv2.flip(image, -1)
    else:
        print("Invalid direction entered")
        return
    plt.imshow(cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB))
    plt.title("Image Reflection")
    plt.show()

# CHOICE 5
def shear_image():
    filename = input("Input image: ")
    image = cv2.imread(filename)
    print("Please enter a number between decimals (0.05 ~ 1.5)") # PUT DECIMALS OR IT FREEZES BECAUSE ITS TOO BIG
    sx = float(input("Enter the shear factor along the X axis: "))
    sy = float(input("Enter the shear factor along the Y axis: "))
    shear_matrix = np.float32([[1, sx, 0], [sy, 1, 0]])
    sheared_image = cv2.warpAffine(image, shear_matrix, (image.shape[1], image.shape[0]))
    plt.imshow(cv2.cvtColor(sheared_image, cv2.COLOR_BGR2RGB))
    plt.title("Image Shear")
    plt.show()

# PICK THEE CHOICES
def main():
    while True:
        print("What do you like to do?")
        print("1 - Image translation")
        print("2 - Image rotation")
        print("3 - Image scaling")
        print("4 - Image reflection")
        print("5 - Image shear")
        print("6 - Exit")
        choice = input("")
        if choice == '1':
            translate_image()
        elif choice == '2':
            rotate_image()
        elif choice == '3':
            scale_image()
        elif choice == '4':
            reflect_image()
        elif choice == '5':
            shear_image()
        elif choice == '6':
            break
        else:
            print("Invalid choice")

        # LOOP GOING BACK TO CHOICES
        while True:
            answer = input("Do you want to edit another image? (Y/N): ")
            if answer.lower() == 'y':
                break
            elif answer.lower() == 'n':
                print("--- E N D ---")
                return
            else:
                print("Invalid choice, please enter Y or N.")

if __name__ == "__main__":
    main()
        