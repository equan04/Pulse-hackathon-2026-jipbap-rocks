import streamlit as st
import torch
import torchvision.transforms as transforms
from PIL import Image

st.set_page_config(page_title="Classification Result")

st.title("🔍 Classification Result")

# -------------------------
# LOAD MODEL
# -------------------------
@st.cache_resource
def load_model():
    model = torch.load("model.pth", map_location=torch.device("cpu"))
    model.eval()
    return model

model = load_model()

# -------------------------
# LOAD CLASS NAMES
# -------------------------
with open("class_names.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# -------------------------
# IMAGE TRANSFORM
# -------------------------
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def predict(image):
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        outputs = model(image)
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
        confidence, predicted_class = torch.max(probabilities, 0)

    return class_names[predicted_class], float(confidence)

# -------------------------
# CHECK IF IMAGE EXISTS
# -------------------------
if "image" not in st.session_state:
    st.warning("No image found. Please upload one first.")
    if st.button("Go Back"):
        st.switch_page("app.py")
else:
    image = st.session_state["image"]
    st.image(image, caption="Input Image", use_column_width=True)

    label, confidence = predict(image)

    st.success(f"Detected: {label}")
    st.info(f"Confidence: {confidence*100:.2f}%")

    instructions = {
        "Plastic": "Put in recycling bin ♻",
        "Paper": "Keep dry and place in paper recycling",
        "Metal": "Send to metal scrap recycling",
        "Organic": "Compost this waste 🌱"
    }

    st.subheader("Disposal Instruction")
    st.write(instructions.get(label, "Follow local waste guidelines."))

    if st.button("Classify Another Image"):
        st.switch_page("app.py")