import streamlit as st
from PIL import Image

st.set_page_config(page_title="Metal")
st.title("Detected: Metal")

class_names = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]

plastic_info = {
    "Magnetic (steel, iron)": {
        "instruction": "Separate from non-magnetic metals. Check with your local center before dropping off, or drop them off at scrap yards, which will usually pay by weight."
    },
    "Non-magnetic (aluminum, copper)": {
        "instruction": "Labels can remain on, but make sure they are clean and dry. These can be recycled in curbside bins. Make sure aerosol cans are completely empty before disposing."
    },
    "E-Waste": {
        "instruction": "E-waste must be taken to certified recyclers. Do NOT throw in the trash or recycling bins. Some municipalities will also host collectione events."
    }
}

st.subheader("Disposal Instruction")
plastic_image = Image.open("metal.png")
st.image(plastic_image, caption="Source: Blue Earth County", width=700)
st.subheader("Empty, clean, and dry your trash before disposing!")

cols = st.columns(3)
with cols[0]:
    st.subheader("Magnetic (steel, iron)")
    st.write(plastic_info.get("Magnetic (steel, iron)", {}).get('instruction', 'N/A'))
with cols[1]:
    st.subheader("Non-magnetic (aluminum, copper)")
    st.write(plastic_info.get("Non-magnetic (aluminum, copper)", {}).get('instruction', 'N/A'))
with cols[2]:
    st.subheader("E-Waste")
    st.write(plastic_info.get("E-Waste", {}).get('instruction', 'N/A'))

st.subheader("Environmental Impacts")
st.write("Metal waste, when improperly disposed of, causes severe, long-lasting environmental damage by leaching toxic heavy metals (lead, mercury, cadmium) into soil and water, destroying ecosystems, and contaminating food chains. Because metals are non-biodegradable, they persist for centuries, creating dead zones, harming aquatic life, and requiring intensive mining for replacement materials.")
st.write("Metal recycling offers significant environmental and economic benefits by conserving natural resources, saving energy, and reducing landfill waste. It reduces the need for mining raw materials, cuts greenhouse gas emissions by up to 95% for certain metals like aluminum, and supports manufacturing by providing reusable materials, which lowers production costs and boosts economic growth.")

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