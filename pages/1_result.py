import streamlit as st
from PIL import Image
import random

st.set_page_config(page_title="Classification Result")
st.title("🔍 Classification Result")

# -------------------------
# Load class names
# -------------------------
with open("categories.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# -------------------------
# Dummy prediction function
# -------------------------
def predict_dummy(image: Image.Image):
    # Randomly pick a label and confidence
    label = random.choice(class_names)
    confidence = random.uniform(0.7, 0.99)
    return label, confidence

# -------------------------
# Trash info dictionary
# -------------------------
trash_info = {
    "Plastic": {
        "disposal": "Put in recycling bin ♻",
        "fact": "Plastic takes hundreds of years to decompose!"
    },
    "Paper": {
        "disposal": "Keep dry and place in paper recycling",
        "fact": "Recycling paper saves trees and energy."
    },
    "Metal": {
        "disposal": "Send to metal scrap recycling",
        "fact": "Metals can be recycled infinitely without loss."
    },
    "Organic": {
        "disposal": "Compost this waste 🌱",
        "fact": "Composting reduces methane emissions in landfills."
    }
}

# -------------------------
# Check if image exists
# -------------------------
if "image" not in st.session_state:
    st.warning("No image found. Please upload one first.")
    if st.button("Go Back"):
        st.switch_page("app.py")
else:
    image = st.session_state["image"]
    st.image(image, caption="Input Image", width=600)

    # Predict using dummy model
    label, confidence = predict_dummy(image)
    st.success(f"Detected: {label}")
    st.info(f"Confidence: {confidence*100:.2f}%")

    # Display disposal instruction
    st.subheader("Disposal Instruction")
    st.write(trash_info.get(label, {}).get("disposal", "Follow local waste guidelines."))

    # -------------------------
    # Selectbox to learn about other trash types
    # -------------------------
    st.subheader("Learn About Other Trash Types")
    selected_type = st.selectbox("Select a trash type:", class_names)

    if selected_type:
        st.write(f"**Disposal:** {trash_info.get(selected_type, {}).get('disposal', 'N/A')}")
        st.write(f"**Fun Fact:** {trash_info.get(selected_type, {}).get('fact', 'N/A')}")

    if st.button("Classify Another Image"):
        st.switch_page("app.py")