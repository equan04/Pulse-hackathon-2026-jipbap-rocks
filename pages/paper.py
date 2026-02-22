import streamlit as st
from PIL import Image

st.set_page_config(page_title="Paper")
st.title("Detected: Paper")

class_names = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]

plastic_image = Image.open("paper.jpeg")
st.image(plastic_image, caption="Source: Norfolk", width=700)
st.subheader("Disposal Instructions")
st.write("1. Verify the type of paper your recycling center accepts. Some types of paper are coated with plastic, or are made differently (newspaper vs printer paper). Shredded paper also may or may not be accepted.")
st.write("2. Keep the paper dry and clean. Wet or soiled paper must be thrown in the trash.")
st.write("3. Depending on your local recycling program, you may recycle curbside or at a center.")

st.subheader("Environmental Impacts")
st.write("Paper waste significantly impacts the environment, contributing to deforestation, accounting for roughly 26% of landfill waste, and producing methane, a potent greenhouse gas, as it decomposes. The paper industry is a major consumer of energy, water, and a driver of air and water pollution.")
st.write("Paper recycling provides significant environmental and economic benefits by conserving natural resources, saving energy, and reducing pollution. Recycling one ton of paper saves approximately 17 trees, 7,000 gallons of water, and 3.3 cubic yards of landfill space. It also reduces greenhouse gas emissions, cuts water pollution by 35%, and lowers air pollution by 74–95% compared to virgin paper production")


# -------------------------
# Selectbox to learn about other trash types
# -------------------------

st.subheader("Learn About Other Trash Types")

selected_type = st.selectbox(
    "Select a trash type:",
    ["Select..."] + class_names
)

if selected_type != "Select...":
    st.session_state["from_prediction"] = False 
    st.switch_page(("pages/" + selected_type + ".py").lower())

if st.button("Classify Another Image", type="primary"):
    st.switch_page("app.py")