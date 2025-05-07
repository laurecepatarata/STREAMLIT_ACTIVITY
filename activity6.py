# -*- coding: utf-8 -*-
"""
Created on Sun May  6 12:40:14 2025
@author: Administrator
"""

import cv2
import streamlit as st
import numpy as np
import time

# Setup
st.title("Real-Time Video Stream with OpenCV")
st.sidebar.title("Filter Controls")

# Slider for controlling Gaussian Blur parameters (kernel size)
kernel_size = st.sidebar.slider("Gaussian Blur - Kernel Size", 3, 15, 5, step=2)

# Initialize webcam capture
cap = cv2.VideoCapture(0)

# Placeholder for displaying the webcam frames
frame_placeholder = st.empty()

# Snapshot button
if st.button("Take Snapshot"):
    ret, frame = cap.read()
    if ret:
        snapshot_filename = f"snapshot_{int(time.time())}.png"
        cv2.imwrite(snapshot_filename, frame)
        st.image(frame, caption="Snapshot Taken", use_container_width=True)
        st.success(f"Snapshot saved as {snapshot_filename}")

# Video stream loop
while True:
    ret, frame = cap.read()
    if not ret:
        st.error("Failed to capture frame")
        break

    # Apply filter: Gaussian Blur
    blurred_frame = cv2.GaussianBlur(frame, (kernel_size, kernel_size), 0)

    # Display the frame with applied filter
    frame_placeholder.image(blurred_frame, channels="BGR", use_container_width=True)

    # Add delay to control the stream speed (useful for smoother display)
    time.sleep(0.05)

# Release the capture when done
cap.release()