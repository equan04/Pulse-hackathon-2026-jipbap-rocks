import streamlit as st
from PIL import Image

st.set_page_config(page_title="Glass")
st.title("Detected: Glass")

class_names = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]

    # Display disposal instruction
plastic_image = Image.open("Glass.png")
st.image(plastic_image, caption="Source: Blue Earth County", width=700)
st.subheader("Disposal Instruction")
st.write("1. Clean and rinse glass bottles, and make sure they are fully dry before recycling. Make sure to remove lids.")
st.write("2. Don't include non-container glass such as Pyrex, window panes, light bulbs, etc. ")
st.write("3. Glass may be recycled curbside, but to prevent breakage in transportation, try to drop off at a collection center whenever possible.")
st.write("Note: Broken glass should not be put in curbside bins! Check local guidelines, but it usually must be thrown away with regular trash.")

st.subheader("Environmental Impacts")
st.write("Glass waste poses significant environmental risks due to its non-biodegradable nature, taking centuries to decompose in landfills, and its heavy, non-combustible characteristics. While 100% recyclable, poor recycling rates (roughly 21% globally) lead to millions of tons of waste ending up in landfills, contributing to greenhouse gases and occupying space.")
st.write("Recycling glass provides significant environmental and economic benefits, primarily it can be reused endlessly without loss in quality. It reduces raw material consumption (saving sand, soda ash, and limestone), lowers energy usage by 40% due to lower melting temperatures, and reduces carbon emissions by roughly one ton for every five tons of glass recycled.")


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