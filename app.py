import streamlit as st
from PIL import Image
import torch
from torchvision import transforms
import torch.nn as nn
from torchvision import models

st.set_page_config(page_title="AI Waste Classifier")
st.title("♻ AI Waste Classification")
st.write("Upload an image or take a picture to classify waste.")

# -------------------------
# Device
# -------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# -------------------------
# Load Model (cached)
# -------------------------
@st.cache_resource
def load_model():
    model = models.mobilenet_v3_small(pretrained=False)

    # Replace final classifier layer
    model.classifier[3] = nn.Linear(model.classifier[3].in_features, 6)

    model.load_state_dict(torch.load("model.pth", map_location=device))
    model.to(device)
    model.eval()
    return model

model = load_model()

# -------------------------
# Transforms (must match training)
# -------------------------
val_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

class_names = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]

# -------------------------
# Prediction Function
# -------------------------
def predict_image(image):
    image = val_transforms(image)
    image = image.unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(image)
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
        confidence, predicted = torch.max(probabilities, 1)

    return class_names[predicted.item()], confidence.item()

# -------------------------
# Image Input
# -------------------------
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
camera_image = st.camera_input("Or take a picture")

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
elif camera_image is not None:
    image = Image.open(camera_image).convert("RGB")

if image is not None:
    st.image(image, caption="Selected Image", width=600)
    st.session_state["image"] = image

    if st.button("Go to Classification"):

        label, confidence = predict_image(image)

        # Store results in session state
        st.session_state["prediction"] = label
        st.session_state["confidence"] = confidence

        # Dynamically switch page
        st.switch_page(f"pages/{label}.py")