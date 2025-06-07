from advisory import get_advisory
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

@st.cache_resource
def load_my_model():
    return load_model("my_model.h5")

class_labels = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Strawberry___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

def predict_disease(img: Image.Image, model, class_labels):
    """
    Takes a PIL Image, preprocesses it, predicts disease class,
    and returns the predicted class label and confidence score.
    """
    img = img.resize((160, 160))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    prediction = model.predict(img_array)
    predicted_class = class_labels[np.argmax(prediction)]
    
    confidence = np.max(prediction) * 100
    return predicted_class, confidence

def app():
    st.title("🍃 Plant Disease Predictor")

    uploaded_file = st.file_uploader("Upload leaf image", type=["jpg","jpeg","png"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, width=400)

        model = load_my_model()
        predicted_class, confidence = predict_disease(img, model, class_labels)
        advisory = get_advisory(predicted_class)
        
        st.text(f"Prediction: {predicted_class} Confidence: {confidence:.2f}%")
        st.text(f"Predicted Disease:{advisory['disease_name']}")
        st.text(f"Description:{advisory['description']}")
        st.text(f"Treatment:{advisory['treatment']}")
        st.text(f"Prevention:{advisory['prevention']}")
        st.text(f"Youtube Link:{advisory['youtube_link']}")
        

