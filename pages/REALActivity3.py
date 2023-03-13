import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt

st.title("Image Editor")

# CHOICE 1
def translate_image(image, dx, dy):
    translation_matrix = np.float32([[1, 0, dx], [0, 1, dy]])
    translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
    return translated_image

# CHOICE 2
def rotate_image(image, angle):
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

# CHOICE 3
def scale_image(image, fx, fy):
    scaled_image = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
    return scaled_image

# CHOICE 4
def reflect_image(image, flip_direction):
    if flip_direction == '1':
        flipped_image = cv2.flip(image, 1)
    elif flip_direction == '2':
        flipped_image = cv2.flip(image, 0)
    elif flip_direction == '3':
        flipped_image = cv2.flip(image, -1)
    else:
        print("Invalid direction entered")
        return
    return flipped_image

# CHOICE 5
def shear_image(image, sx, sy):
    shear_matrix = np.float32([[1, sx, 0], [sy, 1, 0]])
    sheared_image = cv2.warpAffine(image, shear_matrix, (image.shape[1], image.shape[0]))
    return sheared_image

# MAIN FUNCTION
def main():
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
        st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Original Image", use_column_width=True)
        choice = st.selectbox("What do you want to do?", ["", "Image translation", "Image rotation", "Image scaling", "Image reflection", "Image shear"])
        if choice == "Image translation":
            dx = st.number_input("Enter the amount to translate along the X axis:", value=0, step=1)
            dy = st.number_input("Enter the amount to translate along the Y axis:", value=0, step=1)
            translated_image = translate_image(image, dx, dy)
            st.image(cv2.cvtColor(translated_image, cv2.COLOR_BGR2RGB), caption="Translated Image", use_column_width=True)
        elif choice == "Image rotation":
            angle = st.number_input("Enter the rotation angle in degrees:", value=0, step=1)
            rotated_image = rotate_image(image, angle)
            st.image(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB), caption="Rotated Image", use_column_width=True)
        elif choice == "Image scaling":
            scale_x = st.number_input("Enter the scaling factor along the X axis:", value=1.0, step=0.1)
            scale_y = st.number_input("Enter the scaling factor along the Y axis:", value=1.0, step=0.1)
            scaled_image = scale_image(image, scale_x, scale_y)
            st.image(cv2.cvtColor(scaled_image, cv2.COLOR_BGR2RGB), caption="Scaled Image", use_column_width=True)
        elif choice == "Image reflection":
            axis = st.selectbox("Select reflection axis:", ["", "Horizontal", "Vertical"])
        if axis == "Horizontal":
            reflected_image = reflect_image(image, 1)
            st.image(cv2.cvtColor(reflected_image, cv2.COLOR_BGR2RGB), caption="Horizontally Reflected Image", use_column_width=True)
        elif axis == "Vertical":
            reflected_image = reflect_image(image, 0)
            st.image(cv2.cvtColor(reflected_image, cv2.COLOR_BGR2RGB), caption="Vertically Reflected Image", use_column_width=True)
        elif choice == "Image shear":
            shear_x = st.number_input("Enter the shear factor along the X axis:", value=0.0, step=0.1)
            shear_y = st.number_input("Enter the shear factor along the Y axis:", value=0.0, step=0.1)
            sheared_image = shear_image(image, shear_x, shear_y)
            st.image(cv2.cvtColor(sheared_image, cv2.COLOR_BGR2RGB), caption="Sheared Image", use_column_width=True)
        else:
            st.warning("Please upload an image.")

if name == "main":
main()