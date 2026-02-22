import streamlit as st
from PIL import Image

st.set_page_config(page_title="Cardboard")
st.title("Detected: Cardboard")

class_names = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]

cardboard_info = {
    "Corrugated Cardboard (Standard Shipping Box Cardboard)": {
        "instruction": "Highly recyclable! Remove packing tape/plastic, empty any Styrofoam, and flatten before recycling."
    },
    "Paperboard and Chipboard (Cereal Boxes, Shoe Boxes, etc)": {
        "instruction": "These are recyclable and often accepted with mixed paper or cardboard."
    },
    "Pizza Boxes": {
        "instruction": "Only clean, dry, non-greasy parts are recyclable. Heavily soiled boxes are unrecyclable due to contamination from food residue."
    },
    "Wax-Coated Cardboard (Produce and Frozen Food Boxes)": {
        "instruction": "DO NOT recycle. The wax does not dissolve in the pulping process so these cannot be recycled."
    }
}

# Display disposal instruction
st.subheader("Disposal Instruction")
cardboard_image = Image.open("cardboard.png")
st.image(cardboard_image, caption="Recycling Cardboard", width=700)
st.subheader("Flatten, clean, and dry your trash before disposing!")

cols = st.columns(4)
with cols[0]:
    st.subheader("Corrugated Cardboard (Standard Shipping Box Cardboard)")
    st.write(cardboard_info.get("Corrugated Cardboard (Standard Shipping Box Cardboard)", {}).get('instruction', 'N/A'))
with cols[1]:
    st.subheader("Paperboard and Chipboard (Cereal Boxes, Shoe Boxes, etc)")
    st.write(cardboard_info.get("Paperboard and Chipboard (Cereal Boxes, Shoe Boxes, etc)", {}).get('instruction', 'N/A'))
with cols[2]:
    st.subheader("Pizza Boxes")
    st.write(cardboard_info.get("Pizza Boxes", {}).get('instruction', 'N/A'))
with cols[3]:
    st.subheader("Wax-Coated Cardboard (Produce and Frozen Food Boxes)")
    st.write(cardboard_info.get("Wax-Coated Cardboard (Produce and Frozen Food Boxes)", {}).get('instruction', 'N/A'))

st.subheader("Environmental Impacts")
st.write("Cardboard has a reputation of being the eco-friendly option over plastic packaging. However, despite its " \
        "biodegradability, decomposing cardboard produces methane, a greenhouse gas that is significantly more " \
        "potent than carbon dioxie. Unrecycled cardboard also reduces space in landfills for other trash, " \
        "contributing to the solid waste crisis.")
st.write("Producing new cardboard increases deforestation; requires vast amounts of energy, water, and " \
        "resources; and releases harmful chemicals like chlorine and dioxins into water sources as well as generating " \
        "air pollution.")
st.write("Recycling cardboard helps the environment by reducing waste in landfills and reducing the production of " \
        "cardboard which saves energy and reduces pollution. It prevents the release of methane and can be recycled " \
        "5-7 times.")




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