import streamlit as st
import matplotlib as plt
import cv2
import numpy as np
from PIL import Image #Image Processing
harcascade = "haarcascade_russian_plate_number.xml"
min_area = 500
count = 0
import easyocr


st.image("anpr.jpg",use_column_width="always")
st.markdown("<h1 style='text-align: center; color: green;'>SnapText 😎</h1>", unsafe_allow_html=True)

# st.title(':blue[SnapText]')
st.subheader('Welcome to :blue[SnapText ] !! ')
st.subheader("Upload license plate photos of vehicles, and let us extract and rewrite the text for you. ")
st.divider()
uploaded_file = st.file_uploader("Upload your file here...", type=['jpg'])
# path="plate_0.jpg"
# img = cv.imread(uploaded_file)
if uploaded_file is not None:
    with st.spinner("Extracting Text and License PLate"):
        file_bytes = np.asarray(bytearray(uploaded_file.read()),dtype=np.uint8)
        img=cv2.imdecode(file_bytes,1)
        st.image(img,caption="Uploaded Raw Image")
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        plate_cascade = cv2.CascadeClassifier(harcascade)
        plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)
        for (x, y, w, h) in plates:
            area = w * h

            if area > min_area:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

                img_roi = img[y: y + h, x: x + w]

                # Save the cropped and annotated image
                cv2.imwrite("plate_0.jpg", img_roi)
                
                count += 1
                image = Image.open('plate_0.jpg')
                st.image(image, caption='Extracted License Plate')
                reader = easyocr.Reader(['en'])
                img = cv2.imread('plate_0.jpg')
                result = reader.readtext(img)
                st.success("Extracted Text: "+ result[0][-2].upper())













