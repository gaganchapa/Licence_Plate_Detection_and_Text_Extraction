# Licence Plate Detection and Text Extraction

License Plate Recognition (LPR) and Text Extraction using Deep Learning, specifically 
employing Convolutional Neural Networks (CNNs) and Transfer Learning with the VGG-16 
model, have demonstrated remarkable success in automating the detection and recognition of 
vehicle license plates. This abstract provides an overview of the application of CNNs and 
Transfer Learning in this field

Our code pipeline begins with the image reading process, followed by the extraction of the 
License Plate region of interest (ROI). This ROI is then passed to the EasyOCR API, a robust 
Optical Character Recognition tool, to extract the text from the license plate. This combined 
approach ensures the accuracy and reliability of text extraction from images
## Demo

[Hugging Face Link](https://huggingface.co/spaces/gagandwaz/SnapText)


Input Image


![alt text](https://github.com/gaganchapa/Licence_Plate_Detection_and_Text_Extraction/blob/main/car2.jpg)

Extracted Licence PLate


![alt text](https://github.com/gaganchapa/Licence_Plate_Detection_and_Text_Extraction/blob/main/plate_0.jpg)

Extracted Text



![alt text](https://github.com/gaganchapa/Licence_Plate_Detection_and_Text_Extraction/blob/main/result.jpg)


## Deployment



```bash
  streamlit run app.py
```



