import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt

st.title("Image Translation")

# Create a file uploader for selecting an image
uploaded_file = st.file_uploader("Select an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the uploaded image using OpenCV
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Defining the Bxold and Byold and the Tx and Ty in array
    # You can change the numbers inside the arrays however u want
    Bxold = np.array([2, 3, 4, 5, 6])
    Byold = np.array([5, 6, 7, 8, 9])
    Tx = np.array([6, 7, 8, 9, 10])
    Ty = np.array([2, 3, 4, 5, 6])

    # Create a grid of 2 rows and 5 columns, for a total of 10 subplots.
    fig, ax = plt.subplots(2, 5)

    # Loops for the images 5 times
    for i in range(5):
        # [i] gets from the np.arrays for easy use
        Bxnew = Bxold[i] + Tx[i]
        Bynew = Byold[i] + Ty[i]

        # Translate the image
        translation_matrix = np.float32([[1, 0, Bxold[i]], [0, 1, Byold[i]]])
        translated_img = cv2.warpAffine(img, translation_matrix, (img.shape[1], img.shape[0]))

        # Display the translated image in the top row
        ax[0, i].imshow(translated_img)
        ax[0, i].set_title("Image {} ({}, {})" .format(i+1, Bxold[i], Byold[i]))
        ax[0, i].axis('off')

        # Translate the image again using the new values for Bx and By
        translation_matrix = np.float32([[1, 0, Bxnew], [0, 1, Bynew]])
        translated_img = cv2.warpAffine(img, translation_matrix, (img.shape[1], img.shape[0]))

        # Display the translated image in the bottom row
        ax[1, i].imshow(translated_img)
        ax[1, i].set_title("Image {} ({}, {})" .format(i+6, Bxnew, Bynew))
        ax[1, i].axis('off')

    # Show the plot
    st.pyplot(fig)
