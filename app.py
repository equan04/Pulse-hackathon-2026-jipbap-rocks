import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI Waste Classifier")

st.title("♻ AI Waste Classification")
st.write("Upload an image or take a picture to classify waste.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
camera_image = st.camera_input("Or take a picture")

image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

elif camera_image is not None:
    image = Image.open(camera_image).convert("RGB")

if image is not None:
    st.image(image, caption="Selected Image", use_column_width=True)

    # Save image to session state
    st.session_state["image"] = image

    if st.button("Go to Classification"):
        st.switch_page("pages/1_result.py")