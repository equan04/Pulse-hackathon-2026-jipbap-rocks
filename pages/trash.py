import streamlit as st
from PIL import Image

st.set_page_config(page_title="Trash")
st.title("Detected: Trash")

class_names = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]

trash_info = {
    "Non-Recyclable": {
        "instruction": "Non-recyclable materials like plastic bags/wrappers, Styrofoam, soiled paper, diapers, pet waste, clothing, dirty items such as napkins, and tissue papers, and other small items such as plastic utensils should be thrown away."
    },
    "Hazardous Materials and Electronics & Batteries": {
        "instruction": "DO NOT throw away. Hazardous materials such as paint, household cleaner, and aerosol cans should go to hazardous waste facilities. Electronics and batteries can cause fires. Make sure to take them to special drop-off locations in your area."
    },
    "Compostable Waste": {
        "instruction": "Compostable foods include fruit, vegetable scraps, coffee grounds (and paper coffee filters), non-plastic tea bags, and eggshells are compostable. Small amounts of bread, pasta, grains, and dairy products can be composted as well."
    },
    "Liquid Waste": {
        "instruction": "Non-hazardous liquid waste such as household sewage, sink, and laundry liquids should go down the drain. Hazardhous liquids such as oils and pesticides must go to household hazardous waste collection centers."
    }
}


# Display disposal instruction
st.subheader("Disposal Instruction")
trash_image = Image.open("trash.png")
st.image(trash_image, caption="Types of Trash", width=700)
st.subheader("Make sure to dispose of your trash at the right location!")

cols = st.columns(4)
with cols[0]:
    st.subheader("Non-Recyclable")
    st.write(trash_info.get("Non-Recyclable", {}).get('instruction', 'N/A'))
with cols[1]:
    st.subheader("Hazardous Materials and Electronics & Batteries")
    st.write(trash_info.get("Hazardous Materials and Electronics & Batteries", {}).get('instruction', 'N/A'))
with cols[2]:
    st.subheader("Compostable Waste")
    st.write(trash_info.get("Compostable Waste", {}).get('instruction', 'N/A'))
with cols[3]:
    st.subheader("Liquid Waste")
    st.write(trash_info.get("Liquid Waste", {}).get('instruction', 'N/A'))

st.subheader("Environmental Impacts")
st.write("Landfills produce methane, a greenhouse gas that is significantly more potent than carbon dioxide. Make sure to " \
        "recycle where possible before throwing trash away. Certain foods can be composted as well, which reduces methane " \
        "emissions, enriches soil health, and conserves water.")
st.write("Improperly disposed of hazardous waste causes severe environmental damage by contaminating soil and groundwater, " \
        "harming wildlife, and polluting the air. Throwing batteries and chemcicals into regular trash can also cause landfill " \
        "fires, toxic runoff, and long-term ecosystem destruction. Be sure to properly dispose of hazardous materials at " \
        "special dropoff locations. Check your area to see local dropoff locations.")
st.write("Recycling is important, but it is also important to not mis-sort waste by throwing non-recyclable trash into the " \
        "recycling. Mis-sorted waste can damage recycling systems equipment and render entire batches unrecyclable. This " \
        "leads to higher landfill volumes, environmental pollution, and health risks. Recycling properly decreases the time " \
        "spent at waste management facilities to go through mis-sorted waste and streamlines waste management.")


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