import streamlit as st
from PIL import Image

st.set_page_config(page_title="Plastic")
st.title("Detected: Plastic")

class_names = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]

plastic_info = {
    "#1 PET and #2 HDPE": {
        "instruction": "Prioritize these! Recycle in curbside bins."
    },
    "#3 PVC, #6 PS, and #7 Other": {
        "instruction": "Usually these need a special facility to be recycled and won't be collected curbside; check local guidelines."
    },
    "#4 LDPE and #5 PP": {
        "instruction": "Recycle at drop-off locations. Call ahead to see if your center processes these, otherwise they may need to be thrown away."
    }
}

if "image" not in st.session_state:
    st.warning("No image found. Please upload one first.")
    if st.button("Go Back"):
        st.switch_page("app.py")
else:
    image = st.session_state["image"]
    st.image(image, caption="Input Image", width=600)

    # Predict using dummy model
    st.info(f"Confidence: {0.00}%")

    # Display disposal instruction
    st.subheader("Disposal Instruction")
    plastic_image = Image.open("plastics.png")
    st.image(plastic_image, caption="Types of Plastics", width=900)
    st.subheader("Empty, clean, and dry your trash before disposing!")

    cols = st.columns(3)
    with cols[0]:
        st.subheader("#1 PET and #2 HDPE")
        st.write(plastic_info.get("#1 PET and #2 HDPE", {}).get('instruction', 'N/A'))
    with cols[1]:
        st.subheader("#3 PVC, #6 PS, and #7 Other")
        st.write(plastic_info.get("#3 PVC, #6 PS, and #7 Other", {}).get('instruction', 'N/A'))
    with cols[2]:
        st.subheader("#4 LDPE and #5 PP")
        st.write(plastic_info.get("#4 LDPE and #5 PP", {}).get('instruction', 'N/A'))

    st.subheader("Environmental Impacts")
    st.write("Plastic waste causes severe, long-lasting environmental damage by polluting oceans and landscapes, " \
            "entangling or killing over 1,500 species through ingestion, and breaking down into toxic microplastics. " \
            "It exacerbates climate change via greenhouse gas emissions during production, disposal, and incineration. " \
            "Plastic rarely biodegrades, persisting for centuries.")
    st.write("Recycling plastic helps the environment by reducing waste in landfills and oceans, " \
            "lowering greenhouse gas emissions by roughly 42 percent compared to virgin production, and conserving natural " \
            "resources. It saves energy—often 75 percent  less is needed to create products from recycled materials—and prevents " \
            "harmful chemicals from leaching into soil and water. ")


    # -------------------------
    # Selectbox to learn about other trash types
    # -------------------------
    st.subheader("Learn About Other Trash Types")
    selected_type = st.selectbox("Select a trash type:", class_names)

    if selected_type:
        st.switch_page(("pages/" + selected_type + ".py").lower())

    if st.button("Classify Another Image"):
        st.switch_page("app.py")