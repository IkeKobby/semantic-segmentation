import streamlit as st
from keras_segmentation.predict import model_from_checkpoint_path
from PIL import Image
import numpy as np
import os
import random
# from utils import extractData, loadModel

st.set_page_config(page_title="Prediction dashboard", page_icon=":money_with_wings:", layout="wide")
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("./style/style.css")


header = st.container()
prediction = st.container()
data = st.container()
display = st.container()
model = st.container()


# Extract data into `./data/interim/`
# extractData.extrarct_Data()

# move model to the folder `./model/mobileNet/interim/`
# loadModel.rename()

# get testing images path

testing_images_path = './images_test/'

seed  = np.random.choice(range(10000))
random.seed(seed)
random_image = np.random.choice(os.listdir(testing_images_path))

#########################
st.cache()
def get_model():
    savedModelPath = './interim/'
    return model_from_checkpoint_path(savedModelPath)

#########################

with header:
    st.title("Welcome to Semantic segmentation prediction dashboard.")
    

with prediction:
    st.write("---")
    imagePath = testing_images_path + random_image
    predictedMaskPath = './preds/out.png'
    loadedMobileNet = get_model()
    _ = loadedMobileNet.predict_segmentation(imagePath, predictedMaskPath)

    imageToPredict = Image.open(imagePath)
    predictedMask = Image.open(predictedMaskPath)

    metr = Image.open("./resource/mets.png")

    st.title("Performance")
    st.image(metr, width=512)


with display:
    st.write("---")
    st.subheader("Mobilenet UNET'S Prediction")
    st.write(f"Loading and preparing sample image with seed: {seed}")
    st.write("##")

    image_column, mask_column = st.columns((1, 2))
    with image_column:
        st.write("---Image---")
        st.image(imageToPredict, width=512)
    with mask_column:
        st.write("---Predicted Mask ---")
        st.image(predictedMask, width=512)
    



